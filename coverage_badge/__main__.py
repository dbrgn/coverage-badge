"""
Generate coverage badges for Coverage.py.
"""
# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import os
import sys
import argparse
import pkg_resources
try:
    import coverage
except ImportError:
    coverage = None


__version__ = '0.1.2'


class Devnull(object):
    """
    A file like object that does nothing.
    """
    def write(self, *args, **kwargs):
        pass


def get_total():
    """
    Return the rounded total as properly rounded string.
    """
    cov = coverage.Coverage()
    cov.load()
    total = cov.report(file=Devnull())
    return '{0:.0f}'.format(total)


def get_badge(total):
    """
    Read the SVG template from the package, update total, return SVG as a
    string.
    """
    template_path = os.path.join('templates', 'flat.svg')
    template = pkg_resources.resource_string(__name__, template_path).decode('utf8')
    return template.replace('{{ total }}', total)


def parse_args(argv=None):
    """
    Parse the command line arguments.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-o', dest='filepath',
            help='Save the file to the specified path.')
    parser.add_argument('-q', dest='quiet', action='store_true',
            help='Don\'t output any non-error messages.')
    parser.add_argument('-v', dest='print_version', action='store_true',
            help='Show version.')

    # If arguments have been passed in, use them.
    if argv:
        return parser.parse_args(argv)

    # Otherwise, just use sys.argv directly.
    else:
        return parser.parse_args()


def save_badge(badge, filepath):
    """
    Save badge to the specified path.
    """
    # Validate path (part 1)
    if filepath.endswith('/'):
        print('Error: Filepath may not be a directory.')
        sys.exit(1)

    # Get absolute filepath
    path = os.path.abspath(filepath)
    if not path.lower().endswith('.svg'):
        path += '.svg'

    # Validate path (part 2)
    if os.path.exists(path):
        print('Error: "{}" already exists.'.format(path))
        sys.exit(1)

    # Write file
    with open(path, 'w') as f:
        f.write(badge)

    return path


def main(argv=None):
    """
    Console scripts entry point.
    """
    args = parse_args(argv)

    # Print version
    if args.print_version:
        print('coverage-badge v{}'.format(__version__))
        sys.exit(0)

    # Check for coverage
    if coverage is None:
        print('Error: Python coverage module not installed.')
        sys.exit(1)

    # Generate badge
    try:
        total = get_total()
    except coverage.misc.CoverageException as e:
        print('Error: {} Did you run coverage first?'.format(e))
        sys.exit(1)
    badge = get_badge(total)

    # Show or save output
    if args.filepath:
        path = save_badge(badge, args.filepath)
        if not args.quiet:
            print('Saved badge to {}'.format(path))
    else:
        print(badge, end='')


if __name__ == '__main__':
    main()

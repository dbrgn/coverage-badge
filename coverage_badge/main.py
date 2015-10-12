"""
Generate coverage badges for Coverage.py.
"""
import os
import sys
import argparse
import pkg_resources
import coverage


class Devnull:
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
    template = pkg_resources.resource_string(__name__, template_path)
    return template.replace('{{ total }}', total)


def parse_args():
    """
    Parse the command line arguments.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-o', dest='filepath',
            help='Save the file to the specified path.')
    parser.add_argument('-q', dest='quiet', action='store_true',
            help='Don\'t output any non-error messages.')
    return parser.parse_args()


def save_badge(badge, filepath):
    """
    Save badge to the specified path.
    """
    # Validate path (part 1)
    if args.filepath.endswith('/'):
        print('Error: Filepath may not be a directory.')
        sys.exit(1)

    # Get absolute filepath
    path = os.path.abspath(args.filepath)
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


if __name__ == '__main__':
    args = parse_args()

    # Generate badge
    total = get_total()
    badge = get_badge(total)

    # Show or save output
    if args.filepath:
        path = save_badge(badge, args.filepath)
        if not args.quiet:
            print('Saved badge to {}'.format(path))
    else:
        print(badge)

# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import sys

import pytest

from coverage_badge import __main__


@pytest.fixture
def cb(monkeypatch):
    """
    Return a monkey patched coverage_badge module that always returns a percentage of 79.
    """
    def get_fake_total():
        return '79'
    monkeypatch.setattr(__main__, 'get_total', get_fake_total)
    return __main__


def test_version(cb, capsys):
    """
    Test the version output.
    """
    with pytest.raises(SystemExit) as se:
        cb.main(['-v'])
    out, _ = capsys.readouterr()
    assert out == 'coverage-badge v%s\n' % __main__.__version__


def test_svg_output(cb, capsys):
    """
    Test the SVG output.
    """
    cb.main([])
    out, _ = capsys.readouterr()
    assert out.startswith('<svg xmlns="http://www.w3.org/2000/svg" width="99" height="20">')
    assert '<text x="80" y="14">79%</text>' in out
    assert out.endswith('</svg>\n')


def test_color_ranges(cb, capsys):
    """
    Test color total value
    """
    for total, color in (('97', '#4c1'), ('93', '#97CA00'), ('80', '#a4a61d'), ('65', '#dfb317'),
            ('45', '#fe7d37'), ('15', '#e05d44'), ('n/a', '#9f9f9f')):
        __main__.get_total = lambda: total
        cb.main([])
        out, _ = capsys.readouterr()
        row = '<path fill="%s" d="M63 0h36v20H63z"/>' % color
        assert out.startswith('<svg xmlns="http://www.w3.org/2000/svg" width="99" height="20">')
        assert row in out
        assert out.endswith('</svg>\n')

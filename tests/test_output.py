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

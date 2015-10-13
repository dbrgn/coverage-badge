Coverage.py Badge
==================

A small script to generate coverage badges using Coverage.py.

Example of a generated badge:

.. image:: https://cdn.rawgit.com/dbrgn/coverage-badge/master/example.svg
    :alt: Example coverage badge

The badge template has been taken from shields.io_, therefore it should look
mostly good. (The spec is a bit stricter on the margins, but I can't easily do
text width calculations in Python so the margins might not always be 4px.)

.. _shields.io: http://shields.io/


Usage
-----

Change to a directory where coverage data (in the `.coverage` file) is
available. If you don't have this file yet, you need to run coverage first.

Then you can either return the badge SVG to stdout::

    $ coverage-badge

...or write it to a file::

    $ coverage-badge -o coverage.svg

The full usage text::

    usage: coverage_badge [-h] [-o FILEPATH] [-q]

    Generate coverage badges for Coverage.py.

    optional arguments:
      -h, --help   show this help message and exit
      -o FILEPATH  Save the file to the specified path.
      -q           Don't output any non-error messages.


License
-------

MIT License, see `LICENSE.txt` file..

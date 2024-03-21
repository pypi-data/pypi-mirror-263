========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |github-actions| |codecov|
    * - package
      - |version| |wheel| |supported-versions| |supported-implementations| |commits-since|
.. |docs| image:: https://readthedocs.org/projects/bakabaka/badge/?style=flat
    :target: https://readthedocs.org/projects/bakabaka/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/luzhongqiu/bakabaka/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/luzhongqiu/bakabaka/actions

.. |codecov| image:: https://codecov.io/gh/luzhongqiu/bakabaka/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://app.codecov.io/github/luzhongqiu/bakabaka

.. |version| image:: https://img.shields.io/pypi/v/bakabaka.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/bakabaka

.. |wheel| image:: https://img.shields.io/pypi/wheel/bakabaka.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/bakabaka

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/bakabaka.svg
    :alt: Supported versions
    :target: https://pypi.org/project/bakabaka

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/bakabaka.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/bakabaka

.. |commits-since| image:: https://img.shields.io/github/commits-since/luzhongqiu/bakabaka/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/luzhongqiu/bakabaka/compare/v0.0.0...main



.. end-badges

bakabaka ai common for someone who really know it's value

Installation
============

::

    pip install bakabaka

You can also install the in-development version with::

    pip install https://github.com/luzhongqiu/bakabaka/archive/main.zip


Documentation
=============


https://bakabaka.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

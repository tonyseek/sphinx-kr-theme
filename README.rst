|Build Status| |PyPI Version| |PyPI Downloads| |Wheel Status|

krTheme Sphinx Style
====================

This is the third-part package of Kenneth Reitz's krTheme_. You will not have
to copy the theme files into VCS or register it as submodule anymore.

Installation
------------

.. code-block:: sh

    pip install https://github.com/tonyseek/sphinx-kr-theme/archive/develop.zip

Of course the general usage is putting that into your ``docs/requirements.txt``
then it will be found and installed by the build system such as ReadTheDocs_.

Usage
-----

In your ``conf.py``:

.. code-block:: python

    import sphinx_kr_theme

    html_theme = 'kr'
    html_theme_path = [sphinx_kr_theme.get_html_theme_path(html_theme)]


.. _krTheme: https://github.com/kennethreitz/kr-sphinx-themes
.. _ReadTheDocs: https://readthedocs.org

.. |Build Status| image:: https://travis-ci.org/tonyseek/sphinx-kr-theme.svg?branch=master,develop
   :target: https://travis-ci.org/tonyseek/sphinx-kr-theme
   :alt: Build Status
.. |Wheel Status| image:: https://pypip.in/wheel/sphinx-kr-theme/badge.svg
   :target: https://pypi.python.org/pypi/sphinx-kr-theme
   :alt: Wheel Status
.. |PyPI Version| image:: https://img.shields.io/pypi/v/sphinx-kr-theme.svg
   :target: https://pypi.python.org/pypi/sphinx-kr-theme
   :alt: PyPI Version
.. |PyPI Downloads| image:: https://img.shields.io/pypi/dm/sphinx-kr-theme.svg
   :target: https://pypi.python.org/pypi/sphinx-kr-theme
   :alt: Downloads

|Build Status| |PyPI Version| |PyPI Downloads| |Wheel Status|

krTheme Sphinx Style
====================

This is the third-part package of Kenneth Reitz's krTheme_. You will not have
to copy the theme files into VCS or register it as submodule anymore.

Installation
------------

.. code-block:: sh

    pip install sphinx-kr-theme

Of course the general usage is putting that into your ``docs/requirements.txt``
then it will be found and installed by the build system such as ReadTheDocs_.

Usage
-----

In your ``conf.py``:

.. code-block:: python

    import sphinx_kr_theme

    html_theme = 'kr'  # or 'kr_basic'
    html_theme_path = [sphinx_kr_theme.get_html_theme_path()]

In Sphinx >= 1.2, you only need to set the theme name:

.. code-block:: python

    html_theme = 'kr_basic'


.. _krTheme: https://github.com/kennethreitz/kr-sphinx-themes
.. _ReadTheDocs: https://readthedocs.org


Releases
--------

0.2.0
~~~~~

Added new options to the ``kr_basic`` theme.

Now you can custom the URL and size of the "Fork me on GitHub" ribbon image.

.. code-block:: python

    html_theme_options = {
        'github_fork': 'tonyseek/sphinx-kr-theme',
        'github_fork_ribbon': 'http://aral.github.com/fork-me-on-github-retina-ribbons/right-graphite@2x.png',
        'github_fork_ribbon_width': '149px',
        'github_fork_ribbon_height': '149px',
    }

The size of index logo is customizable too.

.. code-block:: python

    html_theme_options = {
        'index_logo': 'logo@2x.png',
        'index_logo_width': '180px',
        'index_logo_height': '50px',
    }

Those options is useful to include Retina-friendly images in your documents.

0.1.0
~~~~~

Included the original repository (Kenneth Reitz's repository) with git-subtree
and uploaded it to PyPI.

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

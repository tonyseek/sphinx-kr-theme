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

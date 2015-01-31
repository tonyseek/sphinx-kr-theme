"""
    The kr-sphinx-themes wrapper.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Usage::

        # put in your conf.py

        import sphinx_kr_theme

        html_theme = 'kr'
        html_theme_path = [sphinx_kr_theme.get_html_theme_path()]
"""

import pkg_resources


__version__ = '0.1.0'


def get_html_theme_path():
    """Gets the html theme's path.

    :returns: the absolute path of theme location.
    """
    return pkg_resources.resource_filename(__package__, '')


def get_path():
    # the alias of ``get_html_theme_path``
    return get_html_theme_path()

"""
    The kr-sphinx-themes wrapper.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Usage::

        # put in your conf.py

        import sphinx_kr_theme

        html_theme = 'kr'
        html_theme_path = [sphinx_kr_theme.get_html_theme_path(html_theme)]
"""

import os


__version__ = '0.1.0.dev'


def get_html_theme_path(name):
    """Gets the html theme's path.

    :param name: the theme's name, which should be 'kr' or 'kr_small'.
    :returns: the absolute path of theme location.
    """
    root_dir = os.path.abspath(os.path.dirname(__file__))
    if name not in ('kr', 'kr_small'):
        raise ValueError('the theme name should be "kr" or "kr_small"')
    return os.path.join(root_dir, name)


def get_path(name):
    # the alias of ``get_html_theme_path``
    return get_html_theme_path(name)

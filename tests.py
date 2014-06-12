import os

from sphinx_kr_theme import get_html_theme_path


def test_path():
    assert get_html_theme_path('kr').endswith('sphinx_kr_theme/kr')
    assert get_html_theme_path('kr_small').endswith('sphinx_kr_theme/kr_small')


def test_files():
    kr_files = set(os.listdir(get_html_theme_path('kr')))
    kr_small_files = set(os.listdir(get_html_theme_path('kr_small')))
    required_files = {'static', 'layout.html', 'theme.conf'}

    assert required_files.issubset(kr_files)
    assert required_files.issubset(kr_small_files)


def test_static_files():
    kr_static = os.path.join(get_html_theme_path('kr'), 'static')
    kr_small_static = os.path.join(get_html_theme_path('kr_small'), 'static')

    kr_static_files = map(os.path.splitext, os.listdir(kr_static))
    kr_small_static_files = map(os.path.splitext, os.listdir(kr_small_static))

    kr_static_exts = {ext for _, ext in kr_static_files}
    kr_small_static_exts = {ext for _, ext in kr_small_static_files}

    assert kr_static_exts == {'.css', '.css_t'}
    assert kr_small_static_exts == {'.css_t'}

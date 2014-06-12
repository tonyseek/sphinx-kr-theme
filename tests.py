import os

from pytest import fixture
from sphinx_kr_theme import get_html_theme_path


@fixture
def html_theme_path():
    return get_html_theme_path()


def test_path(html_theme_path):
    assert html_theme_path.endswith('sphinx_kr_theme')
    assert {'kr', 'kr_small'}.issubset(set(os.listdir(html_theme_path)))


def test_files(html_theme_path):
    kr_files = set(os.listdir(os.path.join(html_theme_path, 'kr')))
    kr_small_files = set(os.listdir(os.path.join(html_theme_path, 'kr_small')))
    required_files = {'static', 'layout.html', 'theme.conf'}

    assert required_files.issubset(kr_files)
    assert required_files.issubset(kr_small_files)


def test_static_files():
    kr_static = os.path.join(get_html_theme_path(), 'kr/static')
    kr_small_static = os.path.join(get_html_theme_path(), 'kr_small/static')

    kr_static_files = map(os.path.splitext, os.listdir(kr_static))
    kr_small_static_files = map(os.path.splitext, os.listdir(kr_small_static))

    kr_static_exts = {ext for _, ext in kr_static_files}
    kr_small_static_exts = {ext for _, ext in kr_small_static_files}

    assert kr_static_exts == {'.css', '.css_t'}
    assert kr_small_static_exts == {'.css_t'}

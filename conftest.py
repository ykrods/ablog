from pathlib import Path

import docutils
import pytest
import sphinx

# Load app, status and warning fixtures.
pytest_plugins = ["sphinx.testing.fixtures"]


# inspired from sphinx's conftest.py
def pytest_report_header(config):
    header = f"libraries: Sphinx-{sphinx.__display_version__}, docutils-{docutils.__version__}"
    if hasattr(config, "_tmp_path_factory"):
        header += f"\nbase tempdir: {config._tmp_path_factory.getbasetemp()}"

    return header


@pytest.fixture(scope="session")
def rootdir():
    return Path(__file__).parent.absolute() / "roots"


@pytest.fixture(autouse=True)
def reset_blog_config():
    # Reset cached configurations to enable confoverrides
    from ablog.blog import Blog

    Blog._dict = {}

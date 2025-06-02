import {{cookiecutter.package_name}}


def test_version():
    """Check that __version__ exists and is a string."""
    assert isinstance({{cookiecutter.package_name}}.__version__, str)

from importlib import metadata

import arco_z2n


def test_package_imports() -> None:
    assert arco_z2n.__name__ == "arco_z2n"


def test_package_version_matches_metadata() -> None:
    assert arco_z2n.__version__ == metadata.version("arco-z2n")


def test_starter_symbol_exists() -> None:
    assert arco_z2n.hello() == "hello from arco_z2n"

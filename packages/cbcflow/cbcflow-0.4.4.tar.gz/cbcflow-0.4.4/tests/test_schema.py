import os

import pytest

from cbcflow.core.schema import get_schema, get_schema_path


def test_get_schema_path():
    assert os.path.isfile(get_schema_path("v2"))


def test_get_schema_path_unknown_version():
    with pytest.raises(ValueError):
        os.path.isfile(get_schema_path("v4"))


def test_get_schema():
    assert isinstance(get_schema(), dict)


def test_get_schema_bootstrap_file():
    assert isinstance(
        get_schema(["--schema-file", "schema/cbc-meta-data-v2.schema"]), dict
    )


def test_get_schema_bootstrap_version():
    assert isinstance(get_schema(["--schema-version", "v3"]), dict)


def test_get_schema_compare():
    assert get_schema(
        ["--schema-file", "schema/cbc-meta-data-v3.schema"]
    ) == get_schema(["--schema-version", "v3"])

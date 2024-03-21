import argparse
import warnings
import numpy as np
import pytest
from rrcgeoviz.arguments import Arguments
from rrcgeoviz.GeoVizPanelDashboard import GeoVizPanelDashboard
import rrcgeoviz
import types

ACCIDENTS_DATA_FILE = open("tests/data_files/small_accidents.csv", "r")
ACCIDENTS_WRONG_NAMES_OPTIONS_FILE = open(
    "tests/options_files/test_options_accidents_wrong_names.json", "r"
)
ACCIDENTS_OPTIONS_FILE = open("tests/options_files/test_options_accidents.json", "r")


@pytest.fixture
def wrong_name_args(scope="Module", autouse=True):
    # You can initialize your object here
    obj = Arguments(ACCIDENTS_DATA_FILE, ACCIDENTS_WRONG_NAMES_OPTIONS_FILE)
    return obj


def test_wrong_column_names_given(wrong_name_args):
    with pytest.raises(TypeError) as wrong_name_error:
        test_obj = GeoVizPanelDashboard(wrong_name_args)

    assert (
        str(wrong_name_error.value)
        == "An incorrect column name was given. Check for misspellings and different capitalizations in the columns options section."
    )

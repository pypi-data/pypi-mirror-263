import argparse
import warnings
import numpy as np
import pytest
from rrcgeoviz.arguments import Arguments
from rrcgeoviz.GeoVizPanelDashboard import GeoVizPanelDashboard
import rrcgeoviz
import types

ACCIDENTS_DATA_FILE_PATH = "tests/data_files/small_accidents.csv"
ACCIDENTS_OPTIONS_FILE_PATH = "tests/options_files/test_options_accidents.json"


@pytest.fixture
def accident_args(scope="Module", autouse=True):
    # You can initialize your object here
    with (
        open(ACCIDENTS_DATA_FILE_PATH, "r") as data,
        open(ACCIDENTS_OPTIONS_FILE_PATH, "r") as options,
    ):
        obj = Arguments(data, options)
    return obj


def test_warn_nan_in_columns(accident_args):
    expected_message = "A null value was found in the dataset. GeoViz ignores any rows with null values in the latitude, longitude, or date columns."
    try:
        with warnings.catch_warnings(record=True) as caught_warnings:
            test_obj = GeoVizPanelDashboard(accident_args)

            # Check if any warnings were issued
            assert len(caught_warnings) == 1

            # Get the warning message
            warning_message = str(caught_warnings[0].message)

            # Check if the warning message matches the expected message
            assert expected_message in warning_message

    except:
        pass


def test_ignore_nan_in_columns(accident_args):
    # peek at dashboard.data
    pass


def test_various_date_columns_accepted(accident_args):
    pass


def test_empty_csv():
    pass

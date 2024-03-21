from argparse import ArgumentError, ArgumentTypeError
import warnings
import pandas as pd
import pytest
from rrcgeoviz.geoviz_cli import main
from pandas.errors import EmptyDataError


def test_sysargs_fail_with_bad_paths():
    with pytest.raises(SystemExit):
        main(["thisisnt", "apath", "--test"])
    with pytest.raises(TypeError):
        main(
            [
                "./tests/options_files/optionstest.json",
                "./tests/options_files/optionstest.json",
                "--test",
            ]
        )
    with pytest.raises(TypeError):
        main(
            [
                "./tests/data_files/oneline.csv",
                "./tests/data_files/oneline.csv",
                "--test",
            ]
        )


def test_fails_with_three_d_enabled_and_not_enough_data():
    with pytest.raises(TypeError):
        main(
            [
                "./tests/data_files/oneline.csv",
                "./tests/options_files/optionstest.json",
                "--test",
            ]
        )


def test_happy_path():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning)
        main(
            [
                "./tests/data_files/clean_asam.csv",
                "./tests/options_files/simple_options.json",
                "--test",
            ]
        )


def test_fails_with_empty_csv():
    with pytest.raises(EmptyDataError):
        main(
            [
                "./tests/data_files/emptydataset.csv",
                "./tests/options_files/optionstest.json",
            ]
        )

import argparse
import os
from pathlib import Path
import pickle
import warnings
import numpy as np
import pytest
from rrcgeoviz.GeneratedData import GeneratedData
from rrcgeoviz.arguments import Arguments
from rrcgeoviz.GeoVizPanelDashboard import GeoVizPanelDashboard
import rrcgeoviz
import types


"""
Make mini arguments object for each test. Variables:
- cache_location set/notset
- cache_results set/notset
- use_cache set/notset
- data cache file exists/not exists

16 tests:
- cache_location set AND cache_results set AND use_cache set AND data cache exists: 
 --> raise error("Can't cache results and use cache at the same time.")

- cache_location set AND cache_results set AND use_cache set AND data cache NOT exists: 
 --> raise error("Can't cache results and use cache at the same time.")

- cache_location set AND cache_results set AND use_cache NOT set AND data cache exists: 
 --> all new generated data is BOTH used and cached at cache_location

 - cache_location set AND cache_results set AND use_cache NOT set AND data cache NOT exists: 
  --> all new generated data is BOTH used and cached at cache_location

- cache_location set AND cache_results NOT set AND use_cache set AND data cache exists: 
 --> use all cached data, assuming all data exists.

- cache_location set AND cache_results NOT set AND use_cache set AND data cache NOT exists: 
 --> data is generated JUST for missing stuff (warning given), rest is using cached data. New data is NOT cached.

- cache_location set AND cache_results NOT set AND use_cache NOT set AND data cache exists: 
 --> fresh data made for ALL features. New data is NOT cached.

- cache_location set AND cache_results NOT set AND use_cache NOT set AND data cache NOT exists: 
 --> fresh data made for ALL features. New data is NOT cached.

##
 
repeat 8 for cache_location defaulting to /.rrcgeovizcache
# somehow test that generateddata is called?? or just check the new data at location AND the generateddata.data_dict.stuff
    #assert gen_data_obj.getGeneratedData()[GENERATOR_NAME] == "is_old"
"""

# Test1: Add data (pickle file of dict?) to cache_location that says old, check args.generated_data["cache_tester"] uses new, check data at cache_location now is new
ACCIDENTS_DATA_FILE_PATH = "tests/data_files/small_accidents.csv"
ACCIDENTS_OPTIONS_FILE_PATH = "tests/options_files/test_options_accidents.json"

TEST_CACHE_PATH = "./testLocation"
GENERATOR_NAME = "cache_tester"


def create_arguments(
    cache_location, cache_results, use_cache, generator_name=GENERATOR_NAME
):
    # You can initialize your object here
    with (
        open(ACCIDENTS_DATA_FILE_PATH, "r") as data,
        open(ACCIDENTS_OPTIONS_FILE_PATH, "r") as options,
    ):
        obj = Arguments(data, options)

    obj._features = [generator_name]

    obj._caching["cache_location"] = cache_location

    if cache_results:
        obj._caching["cache_results"] = True
    else:
        obj._caching["cache_results"] = False

    if use_cache:
        obj._caching["use_cache"] = True
    else:
        obj._caching["use_cache"] = False

    return obj


def add_old_data(location, generator_name=GENERATOR_NAME):
    # TODO: Clear directory first?
    Path(location).mkdir(parents=True, exist_ok=True)
    data = {"type": "is_old"}
    filepath = location + "/" + str(generator_name) + ".pkl"
    if not os.path.isfile(filepath):
        file = open(filepath, "wb")
        pickle.dump(data, file)
        file.close()


@pytest.fixture(autouse=True)
def run_around_tests():
    # Code that will run before your test
    try:
        files = os.listdir(TEST_CACHE_PATH)
        for file in files:
            file_path = os.path.join(TEST_CACHE_PATH, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print("All files deleted successfully.")
    except OSError:
        print("Error occurred while deleting files.")

    # A test function will be run at this point
    yield
    # Code that will run after your test


def test_location_SET_cacheResults_SET_useCache_SET_dataCache_EXISTS():
    """raises error("Can't cache results and use cache at the same time.")"""
    args = create_arguments(TEST_CACHE_PATH, True, True)
    add_old_data(TEST_CACHE_PATH)

    # Make sure error is raised
    with pytest.raises(TypeError) as wrong_combo_error:
        gen_data_obj = GeneratedData(args)
    assert (
        str(wrong_combo_error.value)
        == "Can't cache results and use cache at the same time."
    )

    # Make sure cached data is untouched
    with open(TEST_CACHE_PATH + "/" + GENERATOR_NAME + ".pkl", "rb") as pickle_file:
        result = pickle.load(pickle_file)
    assert result["type"] == "is_old"


def test_location_SET_cacheResults_SET_useCache_SET_dataCache_NOTEXISTS():
    """raises error("Can't cache results and use cache at the same time.")"""
    args = create_arguments(TEST_CACHE_PATH, True, True)

    # Make sure error is raised
    with pytest.raises(TypeError) as wrong_combo_error:
        gen_data_obj = GeneratedData(args)
    assert (
        str(wrong_combo_error.value)
        == "Can't cache results and use cache at the same time."
    )

    # Make sure no data was cached
    assert len(os.listdir(TEST_CACHE_PATH)) == 0


def test_location_SET_cacheResults_SET_useCache_NOTSET_dataCache_EXISTS():
    """all new generated data is BOTH used and cached at cache_location"""
    args = create_arguments(TEST_CACHE_PATH, cache_results=True, use_cache=False)
    add_old_data(TEST_CACHE_PATH)

    gen_data_obj = GeneratedData(args)

    # Make sure cached data is changed
    with open(TEST_CACHE_PATH + "/" + GENERATOR_NAME + ".pkl", "rb") as pickle_file:
        result = pickle.load(pickle_file)
    assert result["type"] == "is_new"

    # Make sure passed data is the new stuff
    assert gen_data_obj.getData()[GENERATOR_NAME]["type"] == "is_new"


def test_location_SET_cacheResults_SET_useCache_NOTSET_dataCache_NOTEXISTS():
    """all new generated data is BOTH used and cached at cache_location"""
    args = create_arguments(TEST_CACHE_PATH, cache_results=True, use_cache=False)

    gen_data_obj = GeneratedData(args)

    # Make sure cached data is changed
    with open(TEST_CACHE_PATH + "/" + GENERATOR_NAME + ".pkl", "rb") as pickle_file:
        result = pickle.load(pickle_file)
    assert result["type"] == "is_new"

    # Make sure passed data is the new stuff
    assert gen_data_obj.getData()[GENERATOR_NAME]["type"] == "is_new"


def test_location_SET_cacheResults_NOTSET_useCache_SET_dataCache_EXISTS():
    """use all cached data, assuming all data exists."""
    args = create_arguments(TEST_CACHE_PATH, cache_results=False, use_cache=True)
    add_old_data(TEST_CACHE_PATH)
    gen_data_obj = GeneratedData(args)

    # Make sure cached data is unchanged
    with open(TEST_CACHE_PATH + "/" + GENERATOR_NAME + ".pkl", "rb") as pickle_file:
        result = pickle.load(pickle_file)
    assert result["type"] == "is_old"

    # Make sure passed data is the old stuff
    assert gen_data_obj.getData()[GENERATOR_NAME]["type"] == "is_old"


def test_location_SET_cacheResults_NOTSET_useCache_SET_dataCache_NOTEXISTS():
    """data is generated JUST for missing stuff (warning given), rest is using cached data. New data is NOT cached."""
    args = create_arguments(TEST_CACHE_PATH, cache_results=False, use_cache=True)
    expected_warning_message = "use_cache was set, but not all of the required cache data was found. Generating new data for:"

    with warnings.catch_warnings(record=True) as caught_warnings:
        gen_data_obj = GeneratedData(args)
        assert len(caught_warnings) >= 1
        warning_message = str(caught_warnings[0].message)
        assert expected_warning_message in warning_message

    # Make sure no new cache data was added
    assert len(os.listdir(TEST_CACHE_PATH)) == 0

    # Make sure passed data is the new stuff
    assert gen_data_obj.getData()[GENERATOR_NAME]["type"] == "is_new"


def test_location_SET_cacheResults_NOTSET_useCache_NOTSET_dataCache_EXISTS():
    """fresh data made for ALL features. New data is NOT cached."""
    args = create_arguments(TEST_CACHE_PATH, cache_results=False, use_cache=False)
    add_old_data(TEST_CACHE_PATH)
    gen_data_obj = GeneratedData(args)

    # Make sure cached data is unchanged
    with open(TEST_CACHE_PATH + "/" + GENERATOR_NAME + ".pkl", "rb") as pickle_file:
        result = pickle.load(pickle_file)
    assert result["type"] == "is_old"

    # Make sure passed data is the new stuff
    assert gen_data_obj.getData()[GENERATOR_NAME]["type"] == "is_new"


def test_location_SET_cacheResults_NOTSET_useCache_NOTSET_dataCache_NOTEXISTS():
    """fresh data made for ALL features. New data is NOT cached."""
    args = create_arguments(TEST_CACHE_PATH, cache_results=False, use_cache=False)
    gen_data_obj = GeneratedData(args)

    # Make sure no new cache data was added
    assert len(os.listdir(TEST_CACHE_PATH)) == 0

    # Make sure passed data is the new stuff
    assert gen_data_obj.getData()[GENERATOR_NAME]["type"] == "is_new"

import json
import string
import pandas as pd
from pandas.errors import EmptyDataError


class Arguments:
    generated_data = {}
    _columns = {}
    _features = {}
    _caching = {}
    _feature_customizations = {}

    def __init__(self, csvFile, jsonFile) -> None:
        self._data = self.loadData(csvFile, ".csv", "data", pd.read_csv)
        print("Data loaded...")
        self.options = self.loadData(jsonFile, ".json", "options", json.load)
        print("Options loaded...")

        self._columns = self.options["columns"]
        self._features = self.options["features"]
        if "caching" in self.options:
            self._caching = self.options["caching"]
        else:
            self._caching = {
                "cache_results": False,
                "use_cache": False,
            }
        if "features_customizations" in self.options:
            self._feature_customizations = self.options["features_customizations"]
        self._data_file_name = csvFile.name

    def loadData(self, file, fileExtension: string, argumentName: string, fileReader):
        if file.closed:
            raise ValueError("File is closed.")

        if fileExtension not in file.name.lower():
            raise TypeError(
                "File of type " + fileExtension + " not passed to " + argumentName + "."
            )

        with file:
            try:
                outfile = fileReader(file)
                return outfile
            except EmptyDataError as ed:
                raise EmptyDataError(ed)
            except:
                raise TypeError("Error reading data: " + file.name)

    def getData(self):
        return self._data

    def getColumns(self):
        return self._columns

    def getFeatures(self):
        return self._features

    def getCaching(self):
        return self._caching

    def getDataFileName(self):
        return self._data_file_name

    def getFeatureCustomizations(self):
        return self._feature_customizations

import json
import panel as pn
from io import BytesIO

from rrcgeoviz.features.FeatureAllMonths import FeatureAllMonths
from rrcgeoviz.features.FeatureBertopic import FeatureBertopic
from rrcgeoviz.features.FeatureHeatmap import FeatureHeatmap
from rrcgeoviz.features.FeatureOneYear import FeatureOneYear
from rrcgeoviz.features.FeatureOneYearMonths import FeatureOneYearMonths
from rrcgeoviz.features.FeaturePOI import FeaturePOI
from rrcgeoviz.features.FeatureSearch import FeatureSearch
from rrcgeoviz.features.FeatureThreeD import FeatureThreeD
from rrcgeoviz.features.FeatureYearlyRange import FeatureYearlyRange
from rrcgeoviz.arguments import Arguments

ALL_FEATURE_CLASSES = [
    FeatureHeatmap,
    FeatureYearlyRange,
    FeatureOneYear,
    FeatureAllMonths,
    FeatureOneYearMonths,
    FeatureThreeD,
    FeaturePOI,
    FeatureSearch,
    FeatureBertopic,
]

option_data = [
    {
        "path": "https://rincon-geoviz.readthedocs.io/en/latest/_images/year_month_heatmap.png",
        "description": "Shows a heatmap of the frequency of incidents by year (row) and month (column).",
        "feature": FeatureHeatmap,
    },
    {
        "path": "https://rincon-geoviz.readthedocs.io/en/latest/_images/year_range_map.png",
        "description": "Shows the incidents on a world map, with the years shown selected by a range.",
        "feature": FeatureYearlyRange,
    },
    {
        "path": "https://rincon-geoviz.readthedocs.io/en/latest/_images/one_year_map.png",
        "description": "Same as Year Range Map, but for one year at a time",
        "feature": FeatureOneYear,
    },
    {
        "path": "https://rincon-geoviz.readthedocs.io/en/latest/_images/month_freq.png",
        "description": "Histogram showing the frequency per month across all data points.",
        "feature": FeatureAllMonths,
    },
    {
        "path": "https://rincon-geoviz.readthedocs.io/en/latest/_images/month_freq_one_year.png",
        "description": "Month-to-Month Frequency, but for one year at a time..",
        "feature": FeatureOneYearMonths,
    },
    {
        "path": "https://rincon-geoviz.readthedocs.io/en/latest/_images/threed_viz.png",
        "description": "A 3D visualization of the data. Latitude, longitude, and time are each a dimension",
        "feature": FeatureThreeD,
    },
    {
        "path": "https://rincon-geoviz.readthedocs.io/en/latest/_images/threed_viz.png",
        "description": "A point of interest plot",
        "feature": FeaturePOI,
    },
    {
        "path": "https://rincon-geoviz.readthedocs.io/en/latest/_images/threed_viz.png",
        "description": "Searching DataFrame for Key Term",
        "feature": FeatureSearch,
    },
    {
        "path": "https://rincon-geoviz.readthedocs.io/en/latest/_images/threed_viz.png",
        "description": "Bertopic Visualizations",
        "feature": FeatureBertopic,
    },
]


class JavaCreator:
    def create_app(self):
        args = Arguments(
            open("tests/data_files/clean_asam.csv", "r"),
            open("tests/options_files/simple_options.json", "r"),
        )

        def generate_json():
            json_content = json.dumps(json_data, indent=3).encode()
            json_bytesio = BytesIO(json_content)
            return json_bytesio

        download_json_button = pn.widgets.FileDownload(
            label="Download JSON",
            callback=generate_json,
            filename="options_selected.json",
            button_type="success",
            icon="arrow-bar-to-down",
        )

        json_data = {
            "columns": {},
            "features": [],
            "features_customizations": {
                "hover_text_columns": [],
                "filter_one_year_column": "",
            },
            "caching": {"cache_results": False, "use_cache": False},
        }

        def update_json(feature, generate):
            if generate:
                json_data["features"].append(feature.getOptionName())
                required_columns = feature.getRequiredColumns()
                json_data["columns"].update({key: key for key in required_columns})

        option_widgets = []

        for data in option_data:
            feature = data["feature"]
            feature = feature(args)
            checkbox = pn.widgets.Checkbox(name=feature.getOptionName())
            binded_checkbox = pn.bind(update_json, feature=feature, generate=checkbox)
            image = pn.pane.Image(data["path"], width=500, caption=data["description"])
            column = pn.Column(checkbox, binded_checkbox, image)
            option_widgets.append(column)

        app_layout = pn.Column()
        for widget in option_widgets:
            row = pn.Row(pn.layout.HSpacer(), widget, pn.layout.HSpacer())
            app_layout.append(row)

        app_layout.append(download_json_button)
        return app_layout


java_creator = JavaCreator()

app = java_creator.create_app()
app.servable()

import panel as pn
from rrcgeoviz.features.ParentGeovizFeature import ParentGeovizFeature


class FeatureDataFrameEditor(ParentGeovizFeature):
    def getOptionName(self):
        return "dataframe_editor"

    def getRequiredColumns(self):
        return []

    def getHeaderText(self):
        return "View / Edit DataFrame"

    def _generateComponent(self):
        df_widget = pn.widgets.DataFrame(
            self.df, sizing_mode="stretch_both", name="DataFrame"
        )
        return df_widget

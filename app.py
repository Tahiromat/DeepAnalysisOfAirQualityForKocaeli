import pandas as pd
import streamlit as st
import plotly.express as px
from plotly import graph_objs as go

from Algorithms.anomaly import AnomalyDetectionAlgorithmsClass as ADAC
from Algorithms.forecast import ForecastingAlgorithmsClass as FAC
from Analysis.analysis import AnalysisTypesClass as ATP
from Visualization.visualization import VisualizationTypesClass as VTC
from Scraping.scraping import ScrapingClass as SC
from Preprocessing.preprocessing import PreprocessingClass as PRPC
from Pages.pages import PagesClass as PC

import warnings
warnings.simplefilter("ignore")

data = pd.read_excel('/home/tahir/Documents/DataScience/DeepAnalysis/Dataset/Kocaeli - Gebze - MTHM.xlsx')

# Pages Steps
# PC.

# Scraping Steps
# SC.

# Preprocessing Steps
PRPC.delete_unnecessary_rows(data)
PRPC.change_data_type(data)
PRPC.convert_xlsx2csv('/home/tahir/Documents/DataScience/DeepAnalysis/Dataset/', data)
PRPC.change_dataset_index(data)

# Rows and Columns Table
st.write(data.head(10))

# Visualization Steps
VTC.line_visualization(data, st, go, "PM10 ( µg/m3 )")
VTC.histogram_visualization(data, st, px, "PM10 ( µg/m3 )")

# Analysis Steps
ATP.monthly_analysis(data, st, pd, go, "PM10 ( µg/m3 )")
ATP.annual_analysis(data, st, go, "PM10 ( µg/m3 )")

# Anomaly Detection Steps
# ADAC.

# Forecasting Steps
# FAC.


import os
import pandas as pd
import pydeck as pdk
import streamlit as st
import plotly.express as px
from plotly import graph_objs as go
from streamlit_option_menu import option_menu

from Algorithms.anomaly import AnomalyDetectionAlgorithmsClass as ADAC
from Algorithms.forecast import ForecastingAlgorithmsClass as FAC
from Analysis.analysis import AnalysisTypesClass as ATP
from Visualization.visualization import VisualizationTypesClass as VTC
from Scraping.scraping import ScrapingClass as SC
from Preprocessing.preprocessing import PreprocessingClass as PRPC

# That import will ignore all warnings and run terminal will be more clean
import warnings
warnings.simplefilter("ignore")

# That command will manage the Streamlit layouts
st.set_page_config(page_title="Air Quality Analysis", page_icon="❗", layout="wide")
hide_streamlit_style = """ <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# PATHS
DATA_MAIN_PATH = "/home/tahir/Documents/DataScience/DeepAnalysis/Dataset/"
STATION_NAME = 'Kocaeli - Yeniköy-MTHM'
EXTANTION = '.xlsx'

data = pd.read_excel(DATA_MAIN_PATH + STATION_NAME + EXTANTION)
PRPC.delete_unnecessary_rows(data)
PRPC.change_data_type(data)
PRPC.change_dataset_index(data)

# Data columns list without time column
parameters = data.columns[1:]

# Choose Bar 
selected_page = option_menu(None, ["Home", "Visualization", "Analysis",  'Anomaly Detection', "Forecasting"], 
icons=['house', 'list-task', "list-task", 'list-task', 'list-task'], 
menu_icon="cast", default_index=0, orientation="horizontal")

if selected_page == "Home":
    st.title(STATION_NAME)
    st.markdown("#")
    # MAP View of specific station coordinates
    VTC.map_visualization(st, pdk, 40.8, 29.433333) # GEBZE MTHM -lat - long
    st.markdown("#")
    st.write(data.head(20))
    st.markdown("#")
    st.write("Each Pie on the chart show the mean of all the times for specific parameter for ------ " + STATION_NAME)
    VTC.pie_visualization(data, st, pd, px, parameters)

elif selected_page == "Visualization":
    st.title("Visualization For " + STATION_NAME)
    # Visualization Steps
    for param in parameters:
        col1, col2 = st.columns(2)
        with col1:
            VTC.line_visualization(data, st, go, param)
        with col2:
            VTC.histogram_visualization(data, st, px, param)

elif selected_page == "Analysis":
    st.title("Analysis For " + STATION_NAME)
    # Analysis Steps
    for param in parameters:
        col1, col2 = st.columns(2)
        with  col1:
            ATP.monthly_analysis(data, st, pd, go, param)
        with col2:
            ATP.annual_analysis(data, st, go, param)

elif selected_page == 'Anomaly Detection':
    st.title("Anomaly Detection For " + STATION_NAME)

else :
    st.title("Forecasting For " + STATION_NAME)



# Pages Steps
# PC.

# Scraping Steps
# SC.

# Preprocessing Steps








# Anomaly Detection Steps
# ADAC.

# Forecasting Steps
# FAC.


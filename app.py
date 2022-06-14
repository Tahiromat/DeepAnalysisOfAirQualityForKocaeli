# Deep-Analysis for Air Quality of Specific City from Turkey

import streamlit as st

from Algorithms.anomaly import AnomalyDetectionAlgorithmsClass as ADAC
from Algorithms.forecast import ForecastingAlgorithmsClass as FAC
from Analysis.analysis import AnalysisTypesClass as ATP
from Visualization.visualization import VisualizationTypesClass as VTC
from Scraping.scraping import ScrapingClass as SC
from Preprocessing.preprocessing import PreprocessingClass as PRPC
from Pages.pages import PagesClass as PC
from Constants.constants import ConstantsClass as CC

ADAC.test(st)

FAC.test(st)

ATP.test(st)

VTC.test(st)

SC.test(st)

PRPC.test(st)

PC.test(st)

CC.test(st)


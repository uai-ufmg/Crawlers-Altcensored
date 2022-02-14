import os
import datetime
import numpy as np
import pandas as pd
from statsmodels.distributions.empirical_distribution import ECDF
from langdetect import detect
from langdetect import DetectorFactory
DetectorFactory.seed = 0


#Reconhece o idioma de uma coluna do df
def lang_detect(df, text_column):
    list_series = []

    for index in df.index:
        text = df[text_column][index]
        text = str(text)

        if text != "NaN" and text != "-":
            try:
                language = detect(text)
                list_series.append(language)
            
            except:
                list_series.append("-")

        else:
            list_series.append("-")
    
    df["language"] = list_series


#Reconhece o idioma de uma coluna do df e salva o resultado em um arquivo .csv
def lang_detect_csv(df, text_column, csv_file):
    list_series = []

    for index in df.index:
        text = df[text_column][index]
        text = str(text)

        if text != "NaN" and text != "-":
            try:
                language = detect(text)
                list_series.append(language)

                csv_df = pd.DataFrame(list_series)
                csv_df.to_csv(csv_file)

            except:
                list_series.append("-")
                csv_df = pd.DataFrame(list_series)
                csv_df.to_csv(csv_file)
        else:
            list_series.append("-")
            csv_df = pd.DataFrame(list_series)
            csv_df.to_csv(csv_file)
    
    df["language"] = list_series


def gini(array):
    """Calculate the Gini coefficient of a numpy array."""
    # based on bottom eq:
    # http://www.statsdirect.com/help/generatedimages/equations/equation154.svg
    # from:
    # http://www.statsdirect.com/help/default.htm#nonparametric_methods/gini.htm
    # All values are treated equally, arrays must be 1d:
    array = array.flatten()
    if np.amin(array) < 0:
        # Values cannot be negative:
        array -= np.amin(array)
    # Values cannot be 0:
    array += 0.0000001
    # Values must be sorted:
    array = np.sort(array)
    # Index per array element:
    index = np.arange(1,array.shape[0]+1)
    # Number of array elements:
    n = array.shape[0]
    # Gini coefficient:
    return ((np.sum((2 * index - n  - 1) * array)) / (n * np.sum(array)))
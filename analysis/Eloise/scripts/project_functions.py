import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):
    
    df1 = (
    pd.read_csv('whreport.csv')
    .dropna()
    .reset_index(drop=True)
    .drop(columns =['Social support','Healthy life expectancy at birth','Freedom to make life choices','Generosity','Perceptions of corruption','Positive affect','Negative affect'])
    )
    
    df2 =(
    df1
    .loc[df1.year >= 2008]
    .loc[df1.year <= 2018]
    .reset_index(drop=True)
    .assign(GDP_per_capita= lambda x: np.exp(x['Log GDP per capita']))
    .rename(columns ={'GDP_per_capita':'GDP per capita'})
    )

    return df2 



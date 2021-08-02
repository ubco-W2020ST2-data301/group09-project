import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_profiling import ProfileReport

# Method chaining begins

# Method Chain 1 (Load data and clean data and process )


def load_and_process(url_or_path_to_csv_file):
    
    data=pd.read_csv(url_or_path_to_csv_file)

    df1 = (
              data[(data.year >=2008) & (data.year <=2018)]
             .drop(['Life Ladder', 'Log GDP per capita','Social support','Generosity','Perceptions of corruption','Positive affect', 'Negative affect'],axis=1) 
             .rename(columns={'Healthy life expectancy at birth':'life_expectancy','Freedom to make life choices':'Freedom_life_choices_in_percentage'})
             .assign(Freedom_life_choices_in_percentage=lambda x: x['Freedom_life_choices_in_percentage']*100)
             .assign(life_expectancy=lambda x: x['life_expectancy'].fillna(df1.groupby('Country name')['life_expectancy'].transform('mean')))
    )

#method chain 2 (Load data and clean data and process )

    df2 = (
            df1
            .assign(Freedom_life_choices_in_percentage=lambda x: x['Freedom_life_choices_in_percentage'].fillna(df1.groupby('Country name')['Freedom_life_choices_in_percentage'].transform('mean')))
            .fillna(0,axis='columns')
            .loc[(df1['life_expectancy'] != 0) ]
            .groupby('Country name')
            .filter(lambda x : len(x)>10)

         )
    
    return df2
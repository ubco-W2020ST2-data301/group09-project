import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def load_and_process(path):
    
    df0 = (
           pd.read_csv(path)
           .drop(['Life Ladder', 'Log GDP per capita','Social support','Generosity','Perceptions of corruption','Positive affect', 'Negative affect'],axis=1)
        
           )
    
    
    
    df1 = (
              df0
              .loc[df0.year >= 2008]
              .loc[df0.year <= 2018]
             .rename(columns={'Healthy life expectancy at birth':'life_expectancy','Freedom to make life choices':'Freedom_life_choices_in_percentage'})
             .assign(Freedom_life_choices_in_percentage=lambda x: x['Freedom_life_choices_in_percentage']*100)
            
           )

    df2 = (
            df1
            #.groupby('Country name')['life_expectancy'].apply(lambda x:x.fillna(x.mean()))
            #.groupby('Country name')['Freedom_life_choices_in_percentage'].apply(lambda x:x.fillna(x.mean()))
        
            .fillna(0,axis='columns')
            .loc[(df1['life_expectancy'] != 0) ]
            #.groupby('Country name')
            #.filter(lambda x : len(x)>10)
                   
 )

    return df2 
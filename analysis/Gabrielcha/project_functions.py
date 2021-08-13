import pandas as pd
import numpy as np
import matplotlib.pylab as plt
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

    return df1
    
# Following method chain, I have been try for a long time, it was working on the normal note book, but not with the import function



    #df2 = (
            # df1
            # .groupby('Country name')['life_expectancy'].apply(lambda x:x.fillna(x.mean()))    line #1
            # .groupby('Country name')['Freedom_life_choices_in_percentage'].apply(lambda x:x.fillna(x.mean()))   line #2
            # .dropna()                    line #3
           #  .groupby(('Country name').filter(lambda x : len(x)>10))     line #4
                   
 #)


# note
# line #1,2 for some region,some year have data, therefore filling with the acverage number 
# line #3 delete the country where do not any record within the given year period
# only keeping the country have more than 10 records

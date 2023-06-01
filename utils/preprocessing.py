import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as  pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import RobustScaler
from utils.model_io import dump_pickle, load_pickle


def read(filename:str,data_path:str='data/raw/')->pd.DataFrame:
    "Load a csv file from the file path, returning a DataFrame."
    df = pd.read_csv(f'{data_path}{filename}')
    
    df = df[df.ocean_proximity!='ISLAND'] 

    return df

def prepare(df:pd.DataFrame, fit: bool = False, data_path:str='data/preprocess/')->pd.DataFrame:
    "Prepare a raw dataframe, returning a prepare DataFrame"
    
    target = 'median_house_value'
    numerical = ['longitude', 'latitude', 'housing_median_age', 'total_rooms',
        'total_bedrooms', 'population', 'households', 'median_income']
    categorical = ['ocean_proximity']

    if fit:
        
        dv = DictVectorizer()
        scaler = RobustScaler().set_output(transform="pandas")
        df_scaled = scaler.fit_transform(df[numerical])
        
        
        dicts = df[categorical].to_dict(orient='records')
        dv = DictVectorizer()
        ohe = pd.DataFrame(dv.fit_transform(dicts).todense(), columns=dv.feature_names_)
         

        df_prepare = pd.concat([ohe.reset_index(drop=True),df_scaled.reset_index(drop=True),df[target].reset_index(drop=True)], axis=1)
        
        dump_pickle(dv,f'{data_path}dv.pkl')
        dump_pickle(scaler,f'{data_path}scaler.pkl')
        return df_prepare
    
    else:
        dv = load_pickle(f'{data_path}dv.pkl')
        scaler = load_pickle(f'{data_path}scaler.pkl')
        
        df_scaled = scaler.fit_transform(df[numerical])
        
        dicts = df[categorical].to_dict(orient='records')
        ohe = pd.DataFrame(dv.transform(dicts).todense(), columns=dv.feature_names_)
        
        df_prepare = pd.concat([ohe.reset_index(drop=True),df_scaled.reset_index(drop=True),df[target].reset_index(drop=True)], axis=1)
        
        return df_prepare
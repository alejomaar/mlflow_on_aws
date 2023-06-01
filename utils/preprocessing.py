import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as  pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import RobustScaler
from utils.model_io import dump_pickle, load_pickle


target = 'median_house_value'
numerical = ['longitude', 'latitude', 'housing_median_age', 'total_rooms',
    'total_bedrooms', 'population', 'households', 'median_income']
categorical = ['ocean_proximity']

def read(filename:str,data_path:str='data/raw/')->pd.DataFrame:
    "Load a csv file from the file path, returning a DataFrame."
    df = pd.read_csv(f'{data_path}{filename}')
    
    df = df[df.median_house_value<450000]
    df['ocean_proximity'] = df['ocean_proximity'].replace(r"\[|\]|<","",regex=True).str.lower().str.replace(r" ","_",regex=True)
    return df


def preprocessing(df:pd.DataFrame):
    # remove outliers in target value  
    q_75 = df[target].quantile(q=0.75)  
    q_25 = df[target].quantile(q=0.25)
    iqr = q_75 - q_25
    upper_bound = q_75 + 1.5 * iqr
    df = df[df.median_house_value< upper_bound]
    # remove ocean_proximity = ocean_proximity because has rare occurrence in dataset.
    df = df[df.ocean_proximity!='ocean_proximity']
    # fill na values with median.
    df['total_bedrooms'] = df['total_bedrooms'].fillna(df['total_bedrooms'].median())
    
    df['median_house_value'] = np.log1p(df['median_house_value'])
    return df
    

def transform(df:pd.DataFrame, fit: bool = False, data_path:str='data/preprocess/')->pd.DataFrame:
    "Transform a data frame to make it ready for training"
    
    if fit:
        # initialize DictVectorizer and RobustScaler
        dv = DictVectorizer()
        scaler = RobustScaler().set_output(transform="pandas")
        
        #Apply RobustScaler to numerical features
        df_scaled = scaler.fit_transform(df[numerical])        
        
        #Apply One Hot Encoding to categorical features
        dicts = df[categorical].to_dict(orient='records')
        dv = DictVectorizer()
        ohe = pd.DataFrame(dv.fit_transform(dicts).todense(), columns=dv.feature_names_)
         
        #Join preprocess features
        df_prepare = pd.concat([ohe.reset_index(drop=True),df_scaled.reset_index(drop=True),df[target].reset_index(drop=True)], axis=1)
        
        dump_pickle(dv,f'{data_path}dv.pkl')
        dump_pickle(scaler,f'{data_path}scaler.pkl')
        
        return df_prepare
    
    else:
        # load DictVectorizer and RobustScaler and apply to dataset
        dv = load_pickle(f'{data_path}dv.pkl')
        scaler = load_pickle(f'{data_path}scaler.pkl')
        
        df_scaled = scaler.fit_transform(df[numerical])
        
        dicts = df[categorical].to_dict(orient='records')
        ohe = pd.DataFrame(dv.transform(dicts).todense(), columns=dv.feature_names_)
        
        df_prepare = pd.concat([ohe.reset_index(drop=True),df_scaled.reset_index(drop=True),df[target].reset_index(drop=True)], axis=1)
        
        return df_prepare
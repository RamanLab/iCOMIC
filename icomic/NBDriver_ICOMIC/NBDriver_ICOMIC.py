#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 12:44:23 2021

@author: shayantan
"""
import pandas as pd
import sys
import glob
import warnings
warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)
import numpy as np
from sklearn import metrics
from sklearn.ensemble import VotingClassifier
from imblearn.metrics import sensitivity_score
from imblearn.metrics import specificity_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.metrics import confusion_matrix
from sklearn.metrics import make_scorer
from sklearn.utils import shuffle
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.preprocessing import MinMaxScaler
from imblearn.under_sampling import RepeatedEditedNearestNeighbours
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KernelDensity
from numpy import arange
from numpy import argmax


def read_model_params():
    vect=pd.read_pickle('./NBDriver_ICOMIC/pretrained_model_params/nbd_only_TFIDF_vect.sav')
    sc=pd.read_pickle('./NBDriver_ICOMIC/pretrained_model_params/nbd_only_scaler.sav')
    model=pd.read_pickle('./NBDriver_ICOMIC/pretrained_model_params/nbd_only_final_model.sav')
    cols=pd.read_pickle('./NBDriver_ICOMIC/pretrained_model_params/nbd_only_top_feats.sav')
    return vect,sc,model,cols
def to_labels(pos_probs, threshold):
    return (pos_probs >= threshold).astype('int')

from sklearn.base import BaseEstimator, ClassifierMixin


class KDEClassifier(BaseEstimator, ClassifierMixin):
    """Bayesian generative classification based on KDE
    
    Parameters
    ----------
    bandwidth : float
        the kernel bandwidth within each class
    kernel : str
        the kernel name, passed to KernelDensity
    """
    def __init__(self, bandwidth=1.0, kernel='gaussian'):
        self.bandwidth = bandwidth
        self.kernel = kernel
        
    def fit(self, X, y):
        self.classes_ = np.sort(np.unique(y))
        training_sets = [X[y == yi] for yi in self.classes_]
        self.models_ = [KernelDensity(bandwidth=self.bandwidth,
                                      kernel=self.kernel).fit(Xi)
                        for Xi in training_sets]
        self.logpriors_ = [np.log(Xi.shape[0] / X.shape[0])
                           for Xi in training_sets]
        return self
        
    def predict_proba(self, X):
        logprobs = np.array([model.score_samples(X)
                             for model in self.models_]).T
        result = np.exp(logprobs + self.logpriors_)
        return result / result.sum(1, keepdims=True)
        
    def predict(self, X):
        return self.classes_[np.argmax(self.predict_proba(X), 1)]


def preprocess(data,k):
    copy = [[x[i:i+k] for i in range(len(x)-k+1)] for x in data]
    copy=[" ".join(review) for review in copy]
    return copy
def run_nbdriver(df_test,vect,sc,model,cols):
    df_4_tf_test=annoate_mutations_using_nbdriver(vect,df_test['new_nbd'].tolist(),sc,df_test['Type'].tolist(),df_test['Chromosome'].tolist())
    preds=print_metrics(model,df_4_tf_test,cols)
    return preds
def annoate_mutations_using_nbdriver(vect,nbd_test,sc,Type_test,Chr_test):
    count_vector_test=vect.transform(preprocess(nbd_test,4))
    df_test=pd.DataFrame(count_vector_test.todense(),columns=vect['cv1'].get_feature_names())
    df_test=pd.DataFrame(sc.transform(df_test),columns=df_test.columns)
    df_test['Type']=Type_test
#    df_test['Label']=Label_test
    df_test['Chr']=Chr_test
    df_test = df_test.loc[:,~df_test.columns.duplicated()]
    df_test,to_delet=clean_dataset(df_test)

    return df_test
#,scaled_feats_test_1
def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_delete = df.isin([np.nan, np.inf, -np.inf]).any(1)
    indices_to_keep=~indices_to_delete
    return df[indices_to_keep].astype(np.float64),df[indices_to_delete].astype(np.float64)

def print_metrics(model,test,cols):
    #test_x=test.drop(['Label'],axis=1)
    #test_y=test['Label']
    y_probs = model.predict_proba(test[cols])[:,1]
    y_test_predictions = np.where(model.predict_proba(test[cols])[:,1] > 0.531, "Driver", "Passenger")
    return y_test_predictions

def main():
    file_name = sys.argv[1]
    data=pd.read_csv(file_name,sep='\t')
    vect,sc,model,cols=read_model_params()
    preds=run_nbdriver(data,vect,sc,model,cols)
    data['predictions']=preds
    data.to_csv('NBDriver_Predictions.csv',index=False)

if __name__ == "__main__":
      main()

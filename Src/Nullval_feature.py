# -*- coding: utf-8 -*- 
'''
Created on 2019年3月23日

@author: Greatpan
'''

def Getnullval_feature(filepath,savename):
    import pandas as pd

    df = pd.read_csv(filepath,encoding='gb18030')
    df.fillna(-1,inplace=True)
    df['null_val'] = (df<0).sum(axis=1)
    df['null_code'] = df.null_val
    df.loc[(df.null_code<=24),'null_code']=1
    df.loc[(df.null_code>24)&(df.null_code<=34),'null_code']=2
    df.loc[(df.null_code>34)&(df.null_code<=46),'null_code']=3
    df.loc[(df.null_code>46)&(df.null_code<=51),'null_code']=4
    df.loc[(df.null_code>51),'null_code']=5
    
    df[['Idx','null_val','null_code']].to_csv('../TempData/'+savename+'.csv',index=None)

if __name__ == '__main__':
    Getnullval_feature("../InputData/Training Set/PPD_Training_Master_GBK_3_1_Training_Set.csv","train_nullval_feature")
    Getnullval_feature("../InputData/Test Set/PPD_Master_GBK_2_Test_Set.csv","test_nullval_feature")

    
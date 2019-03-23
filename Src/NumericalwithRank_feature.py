# -*- coding: utf-8 -*- 

'''
Created on 2019年3月23日

@author: Greatpan
'''

def GetNumerical_feature(train_test):
    # 数值特征
    train = train_test[train_test.target!=-999]
    train.drop('target',axis=1,inplace=True)
    train.to_csv('../TempData/train_numeric_feature.csv',index=None)
    
    test = train_test[train_test.target==-2]
    test.drop('target',axis=1,inplace=True)
    test.to_csv('../TempData/test_numeric_feature.csv',index=None)

def GetRank_feature(train_test,numerical_feature):
    # Rank特征
    train_test_rank = train_test[['Idx','target']]
    for feature in numerical_feature:
        train_test_rank['r'+feature] = train_test[feature].rank(method='max')/float(len(train_test))

    train_rank = train_test_rank[train_test_rank.target!=-999]
    train_rank.drop('target',axis=1,inplace=True)
    train_rank.to_csv('../TempData/train_rank_feature.csv',index=None)
    
    test_rank = train_test_rank[train_test_rank.target==-999]
    test_rank.drop('target',axis=1,inplace=True)
    test_rank.to_csv('../TempData/test_rank_feature.csv',index=None)

if __name__ == '__main__':
    import pandas as pd
    
    feature_type = pd.read_excel('../InputData/Data type description.xlsx')
    feature_type.columns = ['feature','type']
    numerical_feature = list(feature_type[feature_type.type=='Numerical']['feature'])
    numerical_feature.remove('target')
    numerical_feature.remove('ListingInfo')
    
    train = pd.read_csv("../InputData/Training Set/PPD_Training_Master_GBK_3_1_Training_Set.csv",encoding='gb18030')[['Idx','target']+numerical_feature]
    test = pd.read_csv("../InputData\Test Set/PPD_Master_GBK_2_Test_Set.csv",encoding='gb18030')[['Idx']+numerical_feature]
    test['target'] = -999
    train_test = pd.concat([train,test],sort=False)
    
    train_test[train_test.target==1].fillna(train_test[train_test.target==1].median(),inplace=True)
    train_test[train_test.target==0].fillna(train_test[train_test.target==0].median(),inplace=True)
    train_test.fillna(train_test.median(),inplace=True)
    
    GetNumerical_feature(train_test)
    GetRank_feature(train_test,numerical_feature)

    
    
    
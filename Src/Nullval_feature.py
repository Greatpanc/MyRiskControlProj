# -*- coding: utf-8 -*- 
'''
Created on 2019年3月23日

@author: Greatpan
'''

def Getnullval_feature(filepath,savename):
    import pandas as pd

    df_tmp = pd.read_csv(filepath,encoding='gb18030')
    df=df_tmp.copy()
    df.fillna(-1,inplace=True)
    df['null_val'] = (df<0).sum(axis=1)
    df['null_code'] = df.null_val
    df.loc[(df.null_code<=24),'null_code']=1
    df.loc[(df.null_code>24)&(df.null_code<=34),'null_code']=2
    df.loc[(df.null_code>34)&(df.null_code<=46),'null_code']=3
    df.loc[(df.null_code>46)&(df.null_code<=51),'null_code']=4
    df.loc[(df.null_code>51),'null_code']=5
    
    df[['Idx','null_val','null_code']].to_csv('../TempData/'+savename+'.csv',index=None,encoding='gb18030')
    return df_tmp,df
    

def Visualize_nullval(train,train_nullval):
    import numpy as np
    import pandas as pd
    import matplotlib.pylab as plt
    
    train = pd.merge(train_nullval,train,on='Idx')
    train = train.sort_values(by=['null_val'])
    
    train_missing_gt130= train[train.null_val>130]
    train_missing_gt130.to_csv('../TempData/train_missing_gt130.csv',index=None,encoding='gb18030')
    
    print "Max feature loss num:"+str(len(train_missing_gt130))
    
    # 按行统计,排序后通过直线图展示
    plt.figure()
    y = train.null_val.values
    x = range(len(y))
    plt.scatter(x,y,c='k')
    plt.title('train set')
    plt.xlabel('Order Number(sort increasingly)')
    plt.ylabel('Number of Missing Attributes')  
    plt.ylim(0,170) 
    plt.show()
    
    # 按列统计,画直方图
    plt.figure()
    x = [97,97,63,63,63,10,10,6,6,6,6,1,1,1]
    index = np.arange(1,len(x)+1)
    bar_width = 0.35
    opacity = 0.7
    plt.bar(index, x, bar_width,alpha=opacity,color='#87CEFA')
    plt.xlabel('Attributes')
    plt.ylabel('Missing rate(%)')  
    plt.title('Missing rate of Attributes')  
    plt.xticks(index-0.5 + bar_width, ('WeblogInfo_1', 'WeblogInfo_3', 'UserInfo_11', 'UserInfo_12', 'UserInfo_13','WeblogInfo_19','WeblogInfo_21','WeblogInfo_2','WeblogInfo_4','WeblogInfo_5','WeblogInfo_8','UserInfo_2','UserInfo_4','WeblogInfo_23~49'),rotation=45)  
    plt.ylim(0,100)  
    plt.show()  

if __name__ == '__main__':
    train,train_nullval=Getnullval_feature("../InputData/Training Set/PPD_Training_Master_GBK_3_1_Training_Set.csv","train_nullval_feature")
    test,test_nullval=Getnullval_feature("../InputData/Test Set/PPD_Master_GBK_2_Test_Set.csv","test_nullval_feature")
    
    Visualize_nullval(train,train_nullval)
    

    
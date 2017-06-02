# -*- coding: utf-8 -*-

from pandas import  DataFrame,Series,merge
import pandas as pd
import numpy as np
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


origin_dir='/Users/liupeng/repos/tencent_ad/pre/origin/'

#####  merge origin data to train

# pd_train = pd.read_csv(origin_dir+'train.csv',header=0)
# pd_user = pd.read_csv(origin_dir+'user.csv',header=0)
# pd_ad = pd.read_csv(origin_dir+'ad.csv',header=0)
# pd_app_cateogry = pd.read_csv(origin_dir+'app_categories.csv',header=0)
# pd_positon = pd.read_csv(origin_dir+'position.csv',header=0)
#
# pd_ad=merge(pd_ad,pd_app_cateogry,on='appID',how='left')
#
# pd_train = merge(pd_train,pd_user,on='userID',how='left')
# pd_train = merge(pd_train,pd_ad,on='creativeID',how='left')
# pd_train = merge(pd_train,pd_positon,on='positionID',how='left')
#
# pd_train.to_csv('/Users/liupeng/Documents/tencent/pre/merge/merge_origin.csv',index=False)

########



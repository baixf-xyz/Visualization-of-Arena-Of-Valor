# coding=gbk
import pandas as pd
import time
import re
import numpy as np


# �����ȡ�����ݵ�����·��
csv_path = r'..\1.spider\tap_reviews.csv'
# ��ϴ������ݵı���·��
clean_path = r'tap_reviews-extend cleaned.csv'

# ��ȡ����
data = pd.read_csv(csv_path, header=0, index_col='id')

# # �鿴ǰ20�����ݺ�����
# print(data[:20])
# print(data.columns)

# ������ʱ����ʱ���ת����
data['updated_time'] = data['updated_time'].apply(lambda x: time.strftime('%Y-%m-%d', time.localtime(x)))
# ���۾�֧����
data['net_support'] = data['ups'] - data['downs']
# �����ȶ�
data['heat'] = data['ups'] + data['downs']
data['heat'] = (data['heat'] - data['heat'].min()) / (data['heat'].max() - data['heat'].min())
# ����
data['score'] = data['stars']*2

# ������ʱ��Ϊ0�ı�עΪȱʧֵ
data['spent'] = data['spent'].replace(0, np.nan)

# ����������ַ�
data['contents'] = data['contents'].apply(lambda x: re.sub('&[\w]+;', '', str(x)))
data['contents'] = data['contents'].apply(lambda x: re.sub('\(\s*\)', '', str(x)))
# ɾ���ò��ϵ���
data.drop(['ups', 'downs'], axis=1, inplace=True)
# �������ݣ�ת����utf-8����
data.to_csv(clean_path, encoding='utf_8_sig')

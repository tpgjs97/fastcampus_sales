import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from modules import remove_null_row, groupby_count_and_sort, groupby_sum_and_sort, categorize_by_chunk


plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('C:/Users/USER/Desktop/YeadDreamSchool/data/실습데이터.csv')

def groupby_count(df) :
    sorted_df = groupby_count_and_sort(df, '코스(상품) 이름', '거래id', ascending=False)

    chunk_size = 40
    categorize_df = categorize_by_chunk(sorted_df, chunk_size)['카테고리화']

    refund_df = remove_null_row(df,'환불금액')

    merge_df = pd.merge(refund_df, categorize_df, left_on='코스(상품) 이름', right_on = '코스(상품) 이름')
    mapping = {i : f'top{50*i}' for i in range(1, int(np.ceil((len(categorize_df)/chunk_size)))+1)}
    merge_df['카테고리화'] = merge_df['카테고리화'].map(mapping)

    sns.countplot(x = '카테고리화', data=merge_df)
    plt.show()


def groupby_sum(df) :
    sorted_df = groupby_sum_and_sort(df, '코스(상품) 이름', '거래id', ascending=False)

    chunk_size = 40
    categorize_df = categorize_by_chunk(sorted_df, chunk_size)['카테고리화']

    refund_df = remove_null_row(df,'환불금액')

    merge_df = pd.merge(refund_df, categorize_df, left_on='코스(상품) 이름', right_on = '코스(상품) 이름')
    mapping = {i : f'top{50*i}' for i in range(1, int(np.ceil((len(categorize_df)/chunk_size)))+1)}
    merge_df['카테고리화'] = merge_df['카테고리화'].map(mapping)

    sns.countplot(x = '카테고리화', data=merge_df)
    plt.show()

groupby_count(df)
groupby_sum(df)

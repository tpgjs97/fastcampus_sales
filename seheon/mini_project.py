import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from module import remove_null_row, groupby_count_and_sort, groupby_sum_and_sort, categorize_by_chunk

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('C:/Users/USER/Desktop/YearDreamSchool/data/실습데이터.csv')

def groupby_count(df) :
    sorted_df = groupby_count_and_sort(df, '코스(상품) 이름', '거래id', ascending=False)

    chunk_size = 40
    categorize_df = categorize_by_chunk(sorted_df, chunk_size)

    total_categorize_list = []
    for i in range(1, len(categorize_df['카테고리화'].unique())+1) : 
        total_categorize_list.append(categorize_df[categorize_df['카테고리화'] == i]['거래id'].sum())

    refund_df = remove_null_row(df,'환불금액')

    merge_df = pd.merge(refund_df, categorize_df['카테고리화'], left_on='코스(상품) 이름', right_on = '코스(상품) 이름')
    merge_categorize_df = merge_df.groupby('카테고리화').count()
    merge_categorize_df['환불비율'] = (merge_categorize_df['거래id']*100/ total_categorize_list)
    merge_categorize_df = merge_categorize_df.reset_index()
    merge_categorize_df

    sns.barplot(x = '카테고리화', y='환불비율', data = merge_categorize_df, ci=None)
    plt.show()

groupby_count(df)


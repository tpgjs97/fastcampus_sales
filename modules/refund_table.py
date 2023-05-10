import numpy as np

def remove_null_row(df, column_name) :
    '''
    특정 열에 -'값이 있는 행을 제거해주는 함수
    
    Parameters :
        df (DataFrame) : 작업을 수행할 대상 DataFrame
        column_name (str) : 기준이 되는 열(column)의 이름 
    
    Returns :
        df (DataFrame) : 제거가 완료된 DataFrame
    '''
    
    df = df[df[column_name] != '-']
    return df

def groupby_count_and_sort(df, group_column, sort_column, ascending=True):
    """
    주어진 DataFrame을 특정 열로 그룹화하고, 그룹별로 정렬까지 수행하는 함수

    Parameters:
        df (DataFrame): 작업을 수행할 대상 DataFrame
        group_column (str): 그룹화를 수행할 열(column)의 이름
        sort_column (str): 정렬을 수행할 열(column)의 이름
        ascending (bool, optional): 정렬 순서 (기본값: True)

    Returns:
        sorted_df (DataFrame): 그룹화 및 정렬이 완료된 DataFrame
    """
    
    grouped_df = df.groupby(group_column).count()
    sorted_df = grouped_df.sort_values(by=sort_column, ascending=ascending)
    return sorted_df

def groupby_sum_and_sort(df, group_column, sort_column, ascending=True):
    """
    주어진 DataFrame을 특정 열로 그룹화하고, 그룹별로 정렬까지 수행하는 함수

    Parameters:
        df (DataFrame): 작업을 수행할 대상 DataFrame
        group_column (str): 그룹화를 수행할 열(column)의 이름
        sort_column (str): 정렬을 수행할 열(column)의 이름
        ascending (bool, optional): 정렬 순서 (기본값: True)

    Returns:
        sorted_df (DataFrame): 그룹화 및 정렬이 완료된 DataFrame
    """
    
    grouped_df = df.groupby(group_column).sum()
    sorted_df = grouped_df.sort_values(by=sort_column, ascending=ascending)
    return sorted_df

def categorize_by_chunk(df, chunk_size):
    """
    주어진 DataFrame에서 지정된 개수의 행을 기준으로 카테고리화된 열을 추가하는 함수

    Parameters:
        df (DataFrame): 작업을 수행할 대상 DataFrame
        chunk_size (int, optional): 한 카테고리에 속하는 행의 개수 (기본값: 50)

    Returns:
        df (DataFrame): 카테고리화된 열이 추가된 DataFrame
    """
    num_chunks = int(np.ceil(len(df) / chunk_size))
    df['카테고리화'] = np.repeat(np.arange(1, num_chunks + 1), chunk_size)[:len(df)]
    return df
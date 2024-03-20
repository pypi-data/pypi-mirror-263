import numpy as np
import pandas as pd


def print_info(data, table_name):
    print("[ALIOTH - INFO - FEATURE_NAME] ")
    print("[" + ",".join(data) + "]")
    print(table_name)


def get_feature_info(data, table_name=""):
    """
        获取特征信息: 读取第一行/表头并输出
        :param data: 数组、字典、set、dataFrame、numpy.array、csv、excel（表格使用路径传入）
        :param table_name: 表名
        :return: 输出信息至控制台
    """
    # 判断格式
    data_type = type(data)
    if data_type == str:
        if data.endswith(".csv"):
            print_info(pd.read_csv(data), table_name)
        elif data.endswith(".xlsx"):
            print_info(pd.read_excel(data), table_name)
    elif data_type == list or data_type == set:
        print_info(list(map(str, data)), table_name)
    elif data_type == dict:
        print_info(pd.DataFrame(data).columns, table_name)
    elif data_type == pd.core.frame.DataFrame:
        print_info(data.columns, table_name)
    elif data_type == np.ndarray:
        print_info(list(map(str, data[0])), table_name)

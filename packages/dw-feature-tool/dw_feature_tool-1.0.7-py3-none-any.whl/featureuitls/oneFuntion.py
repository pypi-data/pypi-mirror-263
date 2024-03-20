import numpy as np
import pandas as pd

import featureuitls


def get_feature_info(data, table_name=""):
    # 判断格式
    try:
        data_type = type(data)
        print(data_type)
        if data_type == str:
            if data.endswith(".csv"):
                data = pd.read_csv(data)
            elif data.endswith(".xlsx"):
                data = pd.read_excel(data)
        elif data_type == list or data_type == set:
            print("[ALIOTH - INFO - FEATURE_NAME] ")
            print("[" + ",".join(list(map(str, data))) + "]")
            print(table_name)
            return
        elif data_type == dict:
            # dict_to_dataframe
            data = pd.DataFrame(data)
        elif data_type == pd.core.frame.DataFrame:
            data = data
        elif data_type == np.ndarray:
            print("[ALIOTH - INFO - FEATURE_NAME] ")
            print("[" + ",".join(list(map(str, data[0]))) + "]")
            print(table_name)
            return
        else:
            return
    except Exception as e:
        return
    if data.empty:
        return
    try:
        print("[ALIOTH - INFO - FEATURE_NAME] ")
        print("[" + ",".join(data.columns) + "]")
        print(table_name)
    except Exception as e:
        return
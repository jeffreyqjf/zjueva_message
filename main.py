import pandas as pd
import re

if __name__ == "__main__":
    pattern_name = "【ZJUEVA】(.+)同学您好"
    pattern_hash = "\d+"
    df = pd.read_csv("data.csv")
    # print(df["手机号"])
    match_data = df["发送内容"]
    name = []
    hash = []
    length = len(df["发送内容"])
    for i in range(length):
        result_name = re.findall(pattern_name, match_data[i])[0]
        # print(result_name)
        name.append(result_name)
        result_hash = re.findall(pattern_hash, match_data[i])[0]
        # print(result_hash)
        hash.append(result_hash)
    print(name)
    print(hash)
    df["name"] = name
    df["hash"] = hash
    print(df)
    result = df[["手机号", "name", "hash"]]
    result.to_excel("new_data.xlsx")

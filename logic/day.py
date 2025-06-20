# import pandas as pd
# from sklearn.linear_model import LinearRegression


# 传入刚洗刷好的数据，进行预测返回明天金额
# def forcast_tomorrow_amount(washed_data):
#     # 转成 DataFrame
#     df = pd.DataFrame(washed_data)
#     # 转换 date 字符串为 datetime
#     df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
#
#     # 计算距开始日期的天数
#     df["days_since_start"] = (df["date"] - df["date"].min()).dt.days
#
#     # 准备训练数据
#     X = df["days_since_start"].values.reshape(-1, 1)
#     y = df["amount"].values
#
#     # 训练线性回归模型
#     model = LinearRegression()
#     model.fit(X, y)
#
#     # 预测下一天
#     next_day = df["days_since_start"].max() + 1
#     predicted = model.predict([[next_day]])[0]
#
#     return round(float(predicted), 2)

import numpy as np
import datetime


def forcast_tomorrow_amount(washed_data):
    dates = []
    amounts = []

    for item in washed_data:
        dt = datetime.datetime.strptime(item["date"], "%Y-%m-%d")
        dates.append(dt)
        amounts.append(item["amount"])

    base = min(dates)
    days_since_start = [(d - base).days for d in dates]

    x = np.array(days_since_start)
    y = np.array(amounts)

    # 拟合 y = a * x + b
    a, b = np.polyfit(x, y, 1)

    # 预测明天
    next_day = max(days_since_start) + 1
    predicted = a * next_day + b

    return round(float(predicted), 2)

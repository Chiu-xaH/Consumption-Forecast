# import pandas as pd
# from sklearn.linear_model import LinearRegression


# 传入刚洗刷好的数据，进行预测返回下个月金额
# def forcast_next_month_amount(washed_data):
#     print(washed_data)
#     # 1. 转成 DataFrame
#     df = pd.DataFrame(washed_data)
#
#     # 2. month 字符串转 datetime
#     df["month"] = pd.to_datetime(df["month"], format="%Y-%m")
#
#     # 3. 计算从起始月开始的月份编号
#     df["months_since_start"] = (df["month"].dt.to_period("M") - df["month"].min().to_period("M")).apply(lambda x: x.n)
#
#     # 4. 训练模型
#     X = df["months_since_start"].values.reshape(-1, 1)
#     y = df["amount"].values
#
#     model = LinearRegression()
#     model.fit(X, y)
#
#     # 5. 预测下个月
#     next_month = df["months_since_start"].max() + 1
#     predicted = model.predict([[next_month]])[0]
#
#     return round(float(predicted), 2)

import numpy as np
import datetime


def forcast_next_month_amount(washed_data):
    # 1. 转成列表
    months = []
    amounts = []

    for item in washed_data:
        # 解析时间
        dt = datetime.datetime.strptime(item["date"], "%Y-%m")
        months.append(dt)
        amounts.append(item["amount"])

    # 数据不足无法预测
    if len(months) < 2:
        return round(float(amounts[0]) if amounts else 0.0, 2)

    # 2. 转换成从起始月开始的编号
    base = min(months)
    month_nums = [(m.year - base.year) * 12 + (m.month - base.month) for m in months]

    avg = average_amount(washed_data)
    diffs = [abs(a - avg) for a in amounts]
    max_diff_index = diffs.index(max(diffs))

    if len(amounts) > 2:  # 避免剔除后不足以预测
        del amounts[max_diff_index]
        del month_nums[max_diff_index]

    # 3. 用 numpy 实现线性拟合 y = a*x + b
    x = np.array(month_nums)
    y = np.array(amounts)

    a, b = np.polyfit(x, y, 1)

    # 4. 预测下个月
    next_month = max(month_nums) + 1
    predicted = a * next_month + b

    return round(float(predicted), 2)


def average_amount(washed_data):
    if not washed_data:
        return 0.0  # 避免除以0

    total = sum(item["amount"] for item in washed_data)
    avg = total / len(washed_data)
    return round(avg, 2)

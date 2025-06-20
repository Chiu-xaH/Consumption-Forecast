import pandas as pd
from sklearn.linear_model import LinearRegression


# 传入刚洗刷好的数据，进行预测返回下个月金额
def forcast_next_month_amount(washed_data):
    print(washed_data)
    # 1. 转成 DataFrame
    df = pd.DataFrame(washed_data)

    # 2. month 字符串转 datetime
    df["month"] = pd.to_datetime(df["month"], format="%Y-%m")

    # 3. 计算从起始月开始的月份编号
    df["months_since_start"] = (df["month"].dt.to_period("M") - df["month"].min().to_period("M")).apply(lambda x: x.n)

    # 4. 训练模型
    X = df["months_since_start"].values.reshape(-1, 1)
    y = df["amount"].values

    model = LinearRegression()
    model.fit(X, y)

    # 5. 预测下个月
    next_month = df["months_since_start"].max() + 1
    predicted = model.predict([[next_month]])[0]

    return round(float(predicted), 2)

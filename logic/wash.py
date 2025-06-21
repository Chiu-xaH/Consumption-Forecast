from collections import defaultdict

from datetime import datetime
import calendar


# date为"YYYY-MM-DD HH:MM:SS"

# 总数据洗刷为每月消费（根据date）如果不满一个月，则舍弃，最后返回类似列表[dict(date="2024-12",amount)]
# 改进 一个月消费天数大于15天则算有效月，否则有误差
# 为什么选15，为了舍弃寒暑假
def wash_data_to_month(list_data):
    # 1. 将数据按年月分组
    month_data = defaultdict(list)

    for date_str, amount, _ in list_data:
        dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        month_key = dt.strftime("%Y-%m")
        day = dt.day
        month_data[month_key].append((day, amount))

    # 2. 筛选出“满一个月”的数据，并计算总金额
    result = []
    for month, day_amount_list in month_data.items():
        days = {d for d, _ in day_amount_list}  # 用 set 去重
        if len(days) >= 15:  # 有效月规则
            total = sum(amount for _, amount in day_amount_list)
            result.append({
                "date": month,
                "amount": round(total, 2)
            })

    return result


# date为"YYYY-MM-DD HH:MM:SS"
# 总数据洗刷为每日消费（根据date）最后返回类似列表[dict(date="2024-12-01",amount)]
def wash_data_to_day(list_data):
    day_data = defaultdict(float)  # key: date字符串 yyyy-MM-dd，value: 累计金额

    for date_str, amount, _ in list_data:
        # 只保留日期部分
        dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        day_key = dt.strftime("%Y-%m-%d")

        day_data[day_key] += amount

    # 转成列表格式，按日期排序
    result = [{"date": day, "amount": round(total, 2)} for day, total in sorted(day_data.items())]

    return result
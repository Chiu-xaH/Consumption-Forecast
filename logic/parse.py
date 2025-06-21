
# json有三个key，date:String,amount:float,merchant:String
# 不记录电费，电费基本是一个寝室共用，无法代表个人消费
def parse_request(json):
    if not isinstance(json, list):
        raise ValueError("必须是 JSON 数组")
    result = []
    for item in json:
        merchant = item.get("merchant", "")
        if "电" in merchant:
            continue  # 跳过带“电”的记录

        date = item["date"]
        amount = float(item["amount"])
        result.append([date, amount, merchant])

    return result


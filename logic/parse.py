
# json有三个key，date:String,amount:float,merchant:String
def parse_request(json):
    if not isinstance(json, list):
        raise ValueError("必须是 JSON 数组")

    return [[item["date"], float(item["amount"]), item["merchant"]] for item in json]


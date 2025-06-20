import flask
from flask import request, jsonify, Response, Blueprint

import sys
import os

from api.result import ResultEntity, StatusCode
from logic.day import forcast_tomorrow_amount
from logic.month import forcast_next_month_amount
from logic.parse import parse_request
from logic.wash import wash_data_to_day, wash_data_to_month


# 将根目录添加到模块搜索路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = flask.Flask(__name__)


# 创建一个蓝图，并添加前缀
# api = Blueprint('api', __name__, url_prefix='/forecast/api')


# 接收一个JSON，返回一个double
@app.route('/forecast/api/day', methods=['POST'])
def api_day_forecast():
    try:
        json_data = request.get_json()
        data_list = parse_request(json_data)
        washed_data = wash_data_to_day(data_list)
        predicted_data = forcast_tomorrow_amount(washed_data)
        return jsonify(ResultEntity.success(data=predicted_data))
    except Exception as e:
        return jsonify(ResultEntity.fail(StatusCode.BAD_REQUEST, f"数据解析失败: {str(e)}"))


# 接收JSON列表。返回一个double
@app.route('/forecast/api/month', methods=['POST'])
def api_month_forecast():
    try:
        json_data = request.get_json()
        data_list = parse_request(json_data)
        washed_data = wash_data_to_month(data_list)
        predicted_data = forcast_next_month_amount(washed_data)
        return jsonify(ResultEntity.success(data=predicted_data))
    except Exception as e:
        return jsonify(ResultEntity.fail(StatusCode.BAD_REQUEST, f"数据解析失败: {str(e)}"))


# 聚合
@app.route('/forecast/api/', methods=['POST'])
def api_all_forecast():
    try:
        json_data = request.get_json()
        data_list = parse_request(json_data)
        washed_day_data = wash_data_to_day(data_list)
        predicted_day_data = forcast_tomorrow_amount(washed_day_data)
        washed_month_data = wash_data_to_month(data_list)
        predicted_month_data = forcast_next_month_amount(washed_month_data)
        return jsonify(ResultEntity.success(data={
            "month": {
                "predicted_data" : predicted_month_data,
                "statistical_data" : washed_month_data
            },
            "day": {
                "predicted_data": predicted_day_data,
                "statistical_data": washed_day_data
            }
        }))
    except Exception as e:
        return jsonify(ResultEntity.fail(StatusCode.BAD_REQUEST, f"数据解析失败: {str(e)}"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

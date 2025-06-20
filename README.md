# 饭卡消费预测

## 目录结构
/api与/logic均为Flask服务，部署在Vercel，向API POST JSON，然后进行洗刷并预测，将预测值返回

/local为本地运行的，先用运行file.py将原始数据洗刷并保存为csv，在/local/day和/local/month分别预测明日、下月消费并画出折线图

## 实际应用
[后续版本上线到此APP](https://github.com/Chiu-xaH/HFUT-Schedule)

## API文档

**POST /forecast/api/day**

**POST /forecast/api/month**

**POST /forecast/api/**

都提交JSON即可，JSON格式如下：
```JSON
[
  {
    "date" : "2025-06-20 12:00:00",
    "amount" : "11.00",
    "merchant" : "某某餐厅"
  }
]
```
返回JSON格式如下：
```JSON
{
  "data" : {
    "day" : {
      "predicted_data" : 26.77,
      "statistical_data" : [
        {
          "date" : "2025-06-20 12:00:00",
          "amount" : "11.00",
          "merchant" : "某某餐厅"
        }
      ]
    },
    "month" : {
      "predicted_data" : 26.77,
      "statistical_data" : [
        {
          "date" : "2025-06",
          "amount" : "700.80"
        }
      ]
    }
  },
  "msg" : "success",
  "state" : 200
}
```
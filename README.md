# 饭卡消费预测

## 目录结构
/api与/logic均为Flask服务，部署在Vercel，向API POST JSON，然后进行洗刷并预测，将预测值返回

/local为本地运行的，先用运行file.py将原始数据洗刷并保存为csv，在/local/day和/local/month分别预测明日、下月消费并画出折线图

## 实际应用
[后续版本上线到此APP](https://github.com/Chiu-xaH/HFUT-Schedule)
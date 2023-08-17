# wc_stat

- 回测指定时间段指定条件股票名单

# 功能

## 支持时间段
1. 在 ./program/config.yaml的start_date和end_date那一栏
2. 时间段是闭区间，包含起始日和结束日
3. 在问句里的关键词为 "当天" "当天前一天"

## 支持轮询
1. 在 ./program/config.yaml的querys那一栏
2. 问句要换行写，前面加个 - 

## 支持自选股
1. 在 ./program/config.yaml的limits那一栏
2. 股票代码要写中括号内并加引号，用逗号隔开

## 工作日志
1. 记录在./program/work.log里
2. 记录 起止、股票和异常

## 使用专业版来突破查询字数限制
1. 在浏览器端登录问财专业版账号
2. 按ctrl+shift+j打开控制台
3. 在控制台输入document.cookie
4. 将得到的字符串输入 ./program/config.yaml的cookie那一栏

## 代理
1. 如果不使用代理 proxy_url 填 ~

# 部署

## 配置（下载环境依赖）
1. 安装 python == 3.8 和 nodejs v16.17.0.环境
2. 在终端中输入pip install -r requirements.txt

## 打包成exe
1. 修改pywencai.headers: ua = UserAgent(use_external_data=True)
2. 在终端输入pyinstaller ./code/run.py --noconfirm
3. 在run.spec里修改datas=[('./code/config.yaml','.'),('./code/hexin-v.bundle.js','./pywencai/')]
4. 在终端输入pyinstaller run.spec --noconfirm

# 依赖

- python>=3.8
- nodejs
- chinesecalendar [chinesecalendar库使用](https://github.com/LKI/chinese-calendar)
- pywencai [pywencai库使用](https://github.com/zsrl/pywencai)
- openpyxl
- PyExecJS
- PyYAML
- requests
- pyinstaller
- pandas
- ...

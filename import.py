# 引入模块

# 例子：使用statistics模块里的median方法求中位数

# 第一种引入方法
# import 语句
import statistics
print(statistics.median([19,15,36]))

# from...import...语句
from statistics import median, mean
print(median([19,15,36]))
print(mean([19,15,36]))

# from...import*语句
# 引入模块的所有函数
from statistics import *
print(median([19,15,36]))
print(mean([19,15,36]))

# 引入第三方库的模块
# https://pypi.org/
# pip install 安装第三方库
#例子：安装AKShare模块

import akshare as ak
stock_sse_summary_df = ak.stock_sse_summary()
print(stock_sse_summary_df)
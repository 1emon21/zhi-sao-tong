#日志工具
import logging
import os
import datetime
from utils.path_tools_路径工具 import get_abs_path
#定义获取日志器的函数，名字：app，日志级别为INFO
def setup_file_logger(name='app', level=logging.INFO,message=""):
    #获取日志保存的目录
    logging_path=get_abs_path('logs')
    #判断日志目录的存在
    if not os.path.exists(logging_path):
        #如果不存在则创建日志目录
        os.makedirs(logging_path)
    #设置日志文件名
    log_file=os.path.join(logging_path, f"{name}.log")
    #获取当前时间并格式化
    now_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #拼接日志内容
    log_content=f"{now_time}-{logging.getLevelName(level)}-{message}\n"
    print(log_content)
    #追加内容
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_content)


    

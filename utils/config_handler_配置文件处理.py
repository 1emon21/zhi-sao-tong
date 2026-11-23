#配置文件处理
import os
from utils.logger_handler_日志工具 import  setup_file_logger
from utils.path_tools_路径工具 import get_abs_path


def load_congfig():
	global content
	# 记录日志
	setup_file_logger(message="配置文件处理")
	# 获取配置文件路径
	config_path = get_abs_path('config/.env')
	# 判断文件是否存在
	if not os.path.exists(config_path):
		os.makedirs(config_path)  # 不存在则创建
	# 获取配置文件列表
	with open(config_path, 'r', encoding='utf-8') as f:
		content = f.read().split('\n')
	# 去除注释和空白
	for line in content:
		if line.startswith('#') or len(line) == 0:
			content.remove(line)
	# 创建字典
	config_dict = {}
	for line in content:
		lines = line.split('=', 1)
		key = lines[0]
		value = lines[1]
		config_dict[key] = value
	return config_dict
if __name__ == '__main__':
    config = load_congfig()
    print(config, type(config))



	


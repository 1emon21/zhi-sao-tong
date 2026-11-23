'''
路径工具：
 为整个工程提供统一的绝对路径
'''
import os

#获取项目路径
def get_project_root():
	#获取文件的路径
	current_file=os.path.abspath(__file__)
	#获取项目的绝对路径
	current_dir=os.path.dirname(current_file)
	#根
	root_path=os.path.dirname(current_dir)
	return root_path
#获取绝对路径
def get_abs_path(path:str)->str:
	root_path=get_project_root()
	return os.path.join(root_path,path)
	


 
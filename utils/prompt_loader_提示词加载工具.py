#提示词加载工具
from utils.path_tools_路径工具 import get_abs_path
file_path = get_abs_path("prompts/rag_template.txt")#获取文件路径
def load_add_prompt():
	#打开文件
	with open(file_path,'r',encoding='UTF-8') as f:
		template = f.read()
		tem_list=[]
		tem=template.replace("\n", "").split("【用户问题】")
		tem_list.append(("system",tem[0]))
		tem_list.append(("user","【用户问题】"+tem[1]))
		return tem_list
		

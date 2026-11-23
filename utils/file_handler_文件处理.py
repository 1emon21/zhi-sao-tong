# 文件处理工具
import re
from pathlib import Path
from langchain_community.document_loaders import CSVLoader, PyPDFLoader, TextLoader
from langchain_core.documents import Document
from utils.path_tools_路径工具 import get_abs_path


# 对文件进行切片处理
def prcoess_file(path: str):
	file_path = get_abs_path(path)  # 获取文件的绝对路径
	ext = Path(file_path).suffix  # 获取文件扩展名
	chunks = []  # 用来存储文档
	# 对表格csv格式进行文档处理
	if ext == ".csv":
		loader_csv = CSVLoader(
			file_path=file_path,
			csv_args={
				"delimiter": ",",
				"quotechar": '"',
			}
		)
		for document in loader_csv.lazy_load():
			document.page_content = document.page_content.replace('\\n', '')  # 去掉文本中的反斜杠n
			document.page_content = document.page_content.replace('\n', '')  # 去掉真实换行符，合并成一行
			chunks.append(document)
		return chunks
	# 对pdf进行切片处理
	elif ext == ".pdf":
		loader_pdf = PyPDFLoader(
			file_path=file_path,
			mode='single',
		)
		doc = loader_pdf.load()[0]  # 加载pdf并取第一页完整内容
		full_text = doc.page_content
		full_text = full_text.replace('\x0c', '')  # 清理分页符
		segments = re.split(r'\n(?=\d+\.\s?\*\*)', full_text)  # 通过正则对文本进行切分，按数字编号切条目
		for seg in segments:  # 对列表进行遍历
			if seg.strip() == '':  # 跳过空格字符
				continue
			document = Document(page_content=seg.strip(), metadata={"source": file_path})  # 将切分好的文本加入到列表中
			chunks.append(document)
		return chunks
	
	elif ext == ".txt":
		with open(file_path, 'r', encoding='utf-8') as f:
			full_text = f.read()  # 直接读取全文
		segments = re.split(r'\n(?=\d+\. )', full_text)  # 按数字编号切分条目
		for seg in segments:
			if seg.strip() == '': continue  # 跳过空段
			if not seg.strip()[0].isdigit(): continue  # 跳过不以数字开头的标题段
			clean_seg = re.sub(r'\n+### .+$', '', seg.strip())  # 清理条目末尾附带的小标题
			document = Document(page_content=clean_seg, metadata={"source": file_path})  # 包装成Document
			chunks.append(document)
		return chunks
	else:
		raise ValueError(f"不支持的文件格式: {ext}")  # 遇到不支持的格式直接抛异常
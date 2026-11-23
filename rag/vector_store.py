from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
import os
from langchain_core.documents import Document
from model import factory
from utils.file_handler_文件处理 import prcoess_file
import hashlib

from utils.path_tools_路径工具 import get_abs_path


#存取向量
class VectorStore:
	def __init__(self):
		self.embed_model = factory.get_embed_model()
		self.vector_store = Chroma(
			collection_name="records",
			embedding_function=self.embed_model,
			persist_directory=os.getenv("VECTOR_STORE_PATH")
		)
	
	#存入文本
	def add_file_data(self):
		paths = [
			get_abs_path("data/扫地机器人100问.pdf"),
			get_abs_path("data/扫地机器人100问2.txt"),
			get_abs_path("data/扫拖一体机器人100问.txt"),
			get_abs_path("data/故障排除.txt"),
			get_abs_path("data/维护保养.txt"),
			get_abs_path("data/选购指南.txt"),
			get_abs_path("data/external/records.csv")
		]
		metadata = []
		for path in paths:
			chunks = prcoess_file(path)
			for chunk in chunks:
				hash = hashlib.md5(chunk.page_content.encode('utf-8')).hexdigest()
				metadata.append({"ids": hash, "doc": chunk.page_content})
		return metadata
	
	#存入向量
	def build_vector_store(self):
		metadata = self.add_file_data()
		documents = []
		ids = []
		for chunk in metadata:
			doc = Document(page_content=chunk['doc'])  # 包装成document对象
			ids.append(chunk["ids"])
			documents.append(doc)
		self.vector_store.add_documents(documents=documents, ids=ids)
	
	#检索向量获取内容
	def get_retriever(self, k: int):
		result = self.vector_store.as_retriever(search_kwages={"k": k})
		return result  # 返回检索器对象

#智能体工具
from langchain_core.tools import tool
from rag.rag_service import generate_answer
#1.RAG 知识库检索工具
@tool(description="获取检索得到的资料文件")
def knowledge_retriever(query:str):
	return generate_answer(query)
def get_tools():
	return [
		knowledge_retriever,
	]


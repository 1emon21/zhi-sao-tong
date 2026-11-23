#接受用户的问题接受问题，检索文档，填充提示词，调用大模型，回答问题
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from model.factory import get_chat_model
from rag.vector_store import VectorStore
from utils.prompt_loader_提示词加载工具 import load_add_prompt


#获取模型的回答
def generate_answer(question:str):
	vector_store=VectorStore()
	#向向量库检索信息
	retriever=vector_store.get_retriever(k=3)
	#定义函数，用于检索到的文档列表格式化为一个字符串
	#如果文档为空返回“为查询到相关资料”
	def format_func(docs):
		if not docs:
			return "No answer"
		format_str='['
		for doc in docs:
			format_str+=doc.page_content
		format_str+=']'
		return format_str
	prompt_template=ChatPromptTemplate.from_messages(
		load_add_prompt()
	)
	chain=(
		{"question":RunnablePassthrough(),"context":retriever | format_func}
		| prompt_template
		| get_chat_model()
		|StrOutputParser()
	)
	res = chain.invoke(question)
	return res

	
	
	



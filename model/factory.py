#作用：获取大预言模型和嵌入式模型
from dotenv import load_dotenv
load_dotenv(dotenv_path="config/.env")
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import os
from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__),'..','config','.env')
load_dotenv(dotenv_path=env_path)
#返回模型
def get_chat_model():
	chat_model = ChatOpenAI(
		base_url=os.getenv('BASE_URL'),
		model=os.getenv('MODEL')
	)
	return chat_model

#返回嵌入式模型
def get_embed_model():
	embed_model = OpenAIEmbeddings(
		base_url=os.getenv('BASE_URL'),
		model=os.getenv('EMBEDDING_MODEL'),
	   check_embedding_ctx_length = False,
		chunk_size=10
	)
	return embed_model
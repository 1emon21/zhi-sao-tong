from langchain.agents import create_agent
from agent.tools.agent_tools import get_tools
from agent.tools.middleware import get_middleware
from model.factory import get_chat_model
agent=create_agent(
	model=get_chat_model(),
	system_prompt="""'角色设定：你是“智扫通”助手，专攻扫地机器人知识。'
				  '工具使用规则：当用户问到具体的技术问题（故障、参数、选购、扫地机器人相关问题等）时，必须调用 knowledge_retriever 工具；'
				  '当用户只是打招呼、问常识或闲聊时，直接用自己的知识回答，不要调用工具'
				  '。输出格式：如果使用了工具，最终回答要引用来源。""",
	tools=get_tools(),
	middleware=get_middleware()
)
from langchain.agents import AgentState
from langchain.agents.middleware import before_agent, before_model, after_model, after_agent
from langchain_community.utilities.pebblo import Runtime
@before_agent #智能体执行前
def on_chain_start(state:AgentState, runtime:Runtime):
	#获取用户的问题
	print(f"智能体执行前[Agent 开始]用户问题：{state["messages"][-1]}")
@before_model #模型执行前
def on_llm_start(state:AgentState, runtime:Runtime):
	messages =state["messages"]
	for msg in messages:
		print(f"模型执行前[{msg.type}] {msg.content}]")
@after_model#模型执行后
def on_llm_end(state:AgentState, runtime:Runtime):
	messages =state["messages"] #获取模型获取的信息
	#获取模型刚生成的消息
	last_message=messages[-1]
	#获取文本内容
	generate_text =last_message.content
	print(f"[模型执行后] 生成文本：{generate_text}")
	return state
@after_agent#智能体结束后的回答
def on_chain_end(state:AgentState, runtime:Runtime):
	last = state["messages"][-1]
	if getattr(last, "type", None) == "ai":
		print("智能体结束后[最终回答]", last.content)
	return None
def get_middleware():
	return [
		on_chain_start,on_llm_start,on_llm_end,on_chain_end
	]
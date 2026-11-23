# app.py
import streamlit as st
from agent.react_agent import agent

# 页面配置
st.set_page_config(page_title="智扫通 - 扫地机器人问答助手", page_icon="🤖")
st.title("智扫通 🤖")
st.markdown("请输入关于扫地机器人的问题，我会尽力为你解答。")

# 初始化聊天历史（存储在 session_state 中）
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示历史消息
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 用户输入
if prompt := st.chat_input("请输入你的问题..."):
    # 显示用户消息
    with st.chat_message("user"):
        st.markdown(prompt)
    # 添加到历史
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用 agent 获取回答
    with st.chat_message("assistant"):
        with st.spinner("思考中..."):
            try:
                result = agent.invoke({
                    "messages": [{"role": "user", "content": prompt}]
                })
                answer = result["messages"][-1].content
                st.markdown(answer)
                # 添加到历史
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                error_msg = f"发生错误：{str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
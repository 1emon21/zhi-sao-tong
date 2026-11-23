好的，以下是适合你项目的 README.md 内容。你可以直接复制到项目根目录的 README.md 文件中。
# 智扫通 🧹🤖

**智扫通** 是一款基于 **RAG（检索增强生成）** 与 **ReAct Agent** 的扫地机器人智能问答助手。用户可以通过自然语言询问扫地机器人的使用、故障排查、选购建议等问题，系统会结合专业知识库给出准确、带来源的答案。

## ✨ 功能特性

- **智能问答**：支持扫地机器人相关的各类问题（使用方法、故障处理、保养技巧等）。
- **RAG 检索**：基于向量数据库检索专业知识库，确保回答准确可靠。
- **Agent 自主决策**：利用 ReAct 模式的 Agent 自动判断是否需要检索知识库，闲聊问题直接回答。
- **装饰器风格中间件**：通过 `@before_agent`、`@after_model` 等钩子记录日志、监控 Token 消耗。
- **友好的 Web 界面**：基于 Streamlit 构建的聊天界面，交互流畅。

## 📂 项目结构


智扫通/
├── app.py                      # Streamlit 页面入口
├── agent/
│   ├── react_agent.py          # Agent 构建与调用
│   ├── tools/
│   │   └── agent_tools.py      # 工具函数（知识检索等）
│   └── middleware.py           # 装饰器/中间件（日志、监控）
├── model/
│   └── factory.py              # 模型工厂（LLM 与 Embedding）
├── rag/
│   ├── rag_service.py          # RAG 核心服务（检索 + 生成）
│   └── vector_store.py         # 向量库管理（文档切分、入库、检索）
├── config/
│   ├── agent.yml               # Agent 配置
│   ├── rag.yml                 # RAG 配置
│   └── prompts.yml             # 提示词配置
├── prompts/
│   ├── main_prompt.txt         # 系统提示词
│   └── rag_prompt.txt          # RAG 提示词
├── utils/
│   ├── config_handler.py       # 配置加载
│   ├── path_tool.py            # 路径工具
│   ├── logger_handler.py       # 日志工具
│   └── prompt_loader.py        # 提示词加载
├── data/                       # 原始文档与向量数据库
├── .gitignore
├── requirements.txt
└── README.md


## 🔧 技术栈

- **语言**：Python 3.10+
- **框架**：LangGraph（Agent）、LangChain（RAG）、Streamlit（UI）
- **模型**：Qwen3.8-Flash（通过 OpenAI 兼容接口调用）
- **向量库**：ChromaDB
- **文档切分**：RecursiveCharacterTextSplitter
- **日志**：logging（标准库）
- **配置**：PyYAML

## 🚀 快速开始

### 1. 克隆项目

bash
git clone https://github.com/1emon21/zhi-sao-tong.git
cd zhi-sao-tong


### 2. 创建虚拟环境（推荐）

bash
python -m venv .venv
Windows

.venv\Scripts\activate
Linux/Mac

source .venv/bin/activate


### 3. 安装依赖

bash
pip install -r requirements.txt


### 4. 配置环境变量

在项目根目录创建 `.env` 文件（或直接在系统中设置环境变量）：

ini
OPENAI_API_KEY=你的API密钥
OPENAI_BASE_URL=https://api.example.com/v1   # 如有需要


### 5. 准备知识库（首次运行）

运行向量库入库脚本（如 `python rag/vector_store.py`），将扫地机器人文档存入 ChromaDB。

### 6. 启动应用

bash
streamlit run app.py


浏览器访问 `http://localhost:8501` 即可开始对话。

## 📖 使用示例

| 用户问题 | 回答特点 |
|---------|---------|
| “如何使用扫地机器人？” | 检索知识库，给出详细步骤并注明来源 |
| “1+1为什么等于2？” | 直接回答，不调用知识库（闲聊模式） |
| “扫地机器人价格是多少？” | 检索知识库，给出价格区间和推荐品牌 |

## 🛠️ 自定义配置

- **修改模型**：编辑 `model/factory.py` 中的 `get_chat_model()` 函数。
- **修改提示词**：编辑 `prompts/main_prompt.txt` 和 `prompts/rag_prompt.txt`。
- **修改检索参数**：编辑 `config/rag.yml` 中的 `chunk_size`、`top_k` 等。

## 🤝 贡献

欢迎提交 Issue 或 Pull Request。如果你有更好的想法，请先开 Issue 讨论。

## 📄 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 🙏 致谢

- 感谢 LangChain / LangGraph 社区提供的优秀框架。
- 感谢所有开源知识库与数据集的支持。


**🤖 GenAI Q&A Chatbot with LangChain & Streamlit**

This repository contains a production-ready LLM-powered Chatbot built using Python, LangChain, and Streamlit. It demonstrates a clean implementation of a "Chain" architecture, integrating OpenAI's latest models with real-time performance tracking.


**🚀 Key Features**

  **Dynamic Model Selection:** Switch between various OpenAI models (e.g., GPT-5 series) via a sidebar interface.
  
  **Granular LLM Control:** Real-time adjustment of Temperature and Max Tokens to control creativity and response length.
  
  **LangSmith Observability:** Integrated with LangChain Tracing V2 for debugging, monitoring latency, and analyzing token usage.
  
  **Secure API Handling:** Uses dotenv for environment variables and a secure Streamlit password input for runtime API key injection.
  
  

**🛠️ Technical Stack**

  **Frontend:** Streamlit
  
  **Orchestration:** LangChain (Expression Language - LCEL)
  
  **LLM Provider:** OpenAI
  
  **Tracking:** LangSmith
  
  **Environment Management:** Python dotenv
  


**📋 Prerequisites**

**Before running the application, ensure you have the following:**

  An **OpenAI API** Key.
  
  A **LangChain API** Key (optional, for tracing).
  
  **Python 3.9** or higher installed.

# import streamlit as st
# import requests
# import pandas as pd

# # --- CONFIGURATION ---
# FASTAPI_URL = "http://localhost:8000"

# st.set_page_config(page_title="Project Insight", page_icon="🧠", layout="wide")

# # --- SESSION STATE INITIALIZATION ---
# if "dataset" not in st.session_state:
#     st.session_state.dataset = None
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # --- SIDEBAR FOR FILE UPLOAD ---
# with st.sidebar:
#     st.header("Upload Your Data")
#     uploaded_file = st.file_uploader(
#         "Upload a PDF, Word, CSV, or Excel file",
#         type=['csv', 'xls', 'xlsx', 'pdf', 'doc', 'docx']
#     )

#     if uploaded_file:
#         with st.spinner("Processing file..."):
#             files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
#             try:
#                 response = requests.post(f"{FASTAPI_URL}/upload", files=files)
#                 if response.status_code == 200:
#                     st.session_state.dataset = response.json()
#                     st.session_state.messages = []  # Reset chat
#                     st.success("File processed successfully!")
#                 else:
#                     st.error(f"Error: {response.json().get('detail')}")
#             except requests.exceptions.ConnectionError:
#                 st.error("Connection failed. Is the FastAPI backend running?")

# # --- MAIN PANEL FOR PREVIEW AND CHAT ---
# st.title("🧠 Project Insight: Natural Language Data Analysis")

# if st.session_state.dataset:
#     st.header("Data Preview")
#     if st.session_state.dataset["type"] == "dataframe":
#         st.dataframe(pd.DataFrame(st.session_state.dataset["data"]))
#     else:
#         st.text_area("File Content", st.session_state.dataset["data"], height=300)

#     st.header("Chat with Your Data")

#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     if prompt := st.chat_input("Ask a question about your data..."):
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(prompt)

#         with st.chat_message("assistant"):
#             with st.spinner("Thinking..."):
#                 payload = {"message": prompt, "context": st.session_state.dataset["context"]}
#                 response = requests.post(f"{FASTAPI_URL}/chat", data=payload)
#                 if response.status_code == 200:
#                     bot_response = response.json()["reply"]
#                 else:
#                     bot_response = f"Error: {response.json().get('detail')}"
#                 st.markdown(bot_response)
        
#         st.session_state.messages.append({"role": "assistant", "content": bot_response})
# else:
#     st.info("Please upload a file using the sidebar to get started.")



# import streamlit as st
# import requests
# import pandas as pd
# import plotly.express as px

# FASTAPI_URL = "http://localhost:8000"
# st.set_page_config(page_title="Project Insight", page_icon="🧠", layout="wide")

# if "dataset" not in st.session_state:
#     st.session_state.dataset = None
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # --- SIDEBAR ---
# with st.sidebar:
#     st.header("Upload Your Data")
#     uploaded_file = st.file_uploader("Upload CSV, Excel, PDF, or Word", type=["csv", "xls", "xlsx", "pdf", "doc", "docx"])

#     if uploaded_file:
#         files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
#         try:
#             res = requests.post(f"{FASTAPI_URL}/upload", files=files)
#             if res.status_code == 200:
#                 st.session_state.dataset = res.json()
#                 st.session_state.messages = []
#                 st.success("File uploaded!")
#             else:
#                 st.error(res.json().get("detail"))
#         except:
#             st.error("Backend not running.")

# # --- MAIN CHAT UI ---
# st.title("🧠 Project Insight: Natural Language Data Analysis")

# if st.session_state.dataset:
#     st.header("Data Preview")
#     if st.session_state.dataset["type"] == "dataframe":
#         st.dataframe(pd.DataFrame(st.session_state.dataset["data"]))
#     else:
#         st.text_area("Document Content", st.session_state.dataset["data"], height=300)

#     st.header("Chat with Your Data")
#     for msg in st.session_state.messages:
#         with st.chat_message(msg["role"]):
#             st.markdown(msg["content"])
#             if msg.get("chart"):
#                 fig = None
#                 chart = msg["chart"]
#                 if chart["type"] == "bar":
#                     fig = px.bar(x=chart["x"], y=chart["y"])
#                 elif chart["type"] == "line":
#                     fig = px.line(x=chart["x"], y=chart["y"])
#                 elif chart["type"] == "pie":
#                     fig = px.pie(names=chart["x"], values=chart["y"])
#                 if fig:
#                     st.plotly_chart(fig, use_container_width=True)

#     if prompt := st.chat_input("Ask a question about your data..."):
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(prompt)

#         with st.chat_message("assistant"):
#             with st.spinner("Thinking..."):
#                 payload = {"message": prompt, "context": st.session_state.dataset["context"]}
#                 res = requests.post(f"{FASTAPI_URL}/chat", data=payload)
#                 if res.status_code == 200:
#                     data = res.json()
#                     st.markdown(data["answer"])
#                     chart = data.get("chart")
#                     if chart:
#                         if chart["type"] == "bar":
#                             fig = px.bar(x=chart["x"], y=chart["y"])
#                         elif chart["type"] == "line":
#                             fig = px.line(x=chart["x"], y=chart["y"])
#                         elif chart["type"] == "pie":
#                             fig = px.pie(names=chart["x"], values=chart["y"])
#                         st.plotly_chart(fig, use_container_width=True)
#                         st.session_state.messages.append({"role": "assistant", "content": data["answer"], "chart": chart})
#                     else:
#                         st.session_state.messages.append({"role": "assistant", "content": data["answer"]})
#                 else:
#                     st.error(res.json().get("detail"))
# else:
#     st.info("Please upload a data file from the sidebar to begin.")

import streamlit as st
import requests
import pandas as pd
import plotly.express as px

FASTAPI_URL = "http://localhost:8000"
st.set_page_config(page_title="Project Insight", page_icon="🧠", layout="wide")

# Custom CSS for styling to match the screenshot
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
        font-family: Arial, sans-serif;
    }
    .title {
        text-align: left;
        font-size: 24px;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 20px;
    }
    .upload-box {
        border: 2px dashed #D1D5DB;
        border-radius: 8px;
        padding: 20px;
        text-align: center;
        background-color: #F9FAFB;
        margin-bottom: 20px;
    }
    .upload-text {
        color: #6B7280;
        font-size: 14px;
    }
    .data-preview {
        margin-bottom: 20px;
    }
    .data-preview h2 {
        font-size: 18px;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 10px;
    }
    .chat-container {
        border: 1px solid #E5E7EB;
        border-radius: 8px;
        padding: 20px;
        background-color: #F9FAFB;
        height: 400px;
        overflow-y: auto;
        margin-bottom: 20px;
    }
    .chat-message-user {
        text-align: right;
        margin-bottom: 10px;
    }
    .chat-message-assistant {
        text-align: left;
        margin-bottom: 10px;
    }
    .chat-bubble-user {
        display: inline-block;
        background-color: #3B82F6;
        color: white;
        padding: 10px 15px;
        border-radius: 15px;
        font-size: 14px;
        max-width: 70%;
    }
    .chat-bubble-assistant {
        display: inline-block;
        background-color: #E5E7EB;
        color: #1F2937;
        padding: 10px 15px;
        border-radius: 15px;
        font-size: 14px;
        max-width: 70%;
    }
    .chat-bubble-error {
        display: inline-block;
        background-color: #E5E7EB;
        color: #EF4444;
        padding: 10px 15px;
        border-radius: 15px;
        font-size: 14px;
        max-width: 70%;
    }
    .chat-input-container {
        display: flex;
        align-items: center;
        border: 1px solid #E5E7EB;
        border-radius: 8px;
        padding: 5px;
        background-color: white;
    }
    .chat-input {
        border: none !important;
        outline: none !important;
        flex-grow: 1;
        font-size: 14px;
        padding: 5px;
    }
    .send-button {
        background-color: #3B82F6;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 8px 15px;
        font-size: 14px;
        cursor: pointer;
    }
    .send-button:hover {
        background-color: #2563EB;
    }
    </style>
""", unsafe_allow_html=True)

# Session state initialization
if "dataset" not in st.session_state:
    st.session_state.dataset = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- MAIN UI ---
st.markdown('<div class="title">Project Insight</div>', unsafe_allow_html=True)

# File uploader
st.markdown('<div class="upload-box"><p class="upload-text">Drag & drop a file here, or click to select<br>Supports: PDF, Word, CSV, Excel</p></div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["csv", "xls", "xlsx", "pdf", "doc", "docx"], label_visibility="collapsed")

if uploaded_file:
    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
    try:
        res = requests.post(f"{FASTAPI_URL}/upload", files=files)
        if res.status_code == 200:
            st.session_state.dataset = res.json()
            st.session_state.messages = [{"role": "assistant", "content": "Data loaded. Ask me anything!"}]
            st.success("File uploaded!")
        else:
            st.error(res.json().get("detail"))
    except:
        st.error("Backend not running.")

# Data preview and chat section
if st.session_state.dataset:
    # Data Preview
    st.markdown('<div class="data-preview"><h2>Data Preview: ' + st.session_state.dataset["filename"] + '</h2></div>', unsafe_allow_html=True)
    if st.session_state.dataset["type"] == "dataframe":
        st.dataframe(pd.DataFrame(st.session_state.dataset["data"]), use_container_width=True)
    else:
        st.text_area("Document Content", st.session_state.dataset["data"], height=300)

    # Chat section
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f'<div class="chat-message-user"><div class="chat-bubble-user">{msg["content"]}</div></div>', unsafe_allow_html=True)
        elif msg["role"] == "assistant":
            if "ERROR" in msg["content"]:
                st.markdown(f'<div class="chat-message-assistant"><div class="chat-bubble-error">{msg["content"]}</div></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-message-assistant"><div class="chat-bubble-assistant">{msg["content"]}</div></div>', unsafe_allow_html=True)
                if msg.get("chart"):
                    fig = None
                    chart = msg["chart"]
                    if chart["type"] == "bar":
                        fig = px.bar(x=chart["x"], y=chart["y"])
                    elif chart["type"] == "line":
                        fig = px.line(x=chart["x"], y=chart["y"])
                    elif chart["type"] == "pie":
                        fig = px.pie(names=chart["x"], values=chart["y"])
                    if fig:
                        st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Chat input
    with st.container():
        prompt = st.text_input("", placeholder="Ask a question about your data...", key="chat_input", label_visibility="collapsed")
        if prompt:
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.spinner("Thinking..."):
                payload = {"message": prompt, "context": st.session_state.dataset["context"]}
                res = requests.post(f"{FASTAPI_URL}/chat", data=payload)
                if res.status_code == 200:
                    data = res.json()
                    st.session_state.messages.append({"role": "assistant", "content": data["answer"], "chart": data.get("chart")})
                    st.experimental_rerun()
                else:
                    st.session_state.messages.append({"role": "assistant", "content": f"ERROR: {res.json().get('detail')}"})
                    st.experimental_rerun()
else:
    st.info("Please upload a data file to begin.")
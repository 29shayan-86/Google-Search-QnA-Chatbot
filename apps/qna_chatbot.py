from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
import streamlit as st







llm = ChatGroq(model="llama-3.3-70b-versatile",temperature=0.5)

st.title("🤖 Ask Buddy - AI QnA Botst")
st.markdown("My QnA Bot with Langchain and Groq")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask anything?")

if query:
    st.session_state.messages.append({"role":"user","content":query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.chat_message("ai").markdown(res.content)

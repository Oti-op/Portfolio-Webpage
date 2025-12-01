import streamlit as st

st.title("Chatbot")

if "messages" not in st.session_state:
    st.session_state.message = []

for message in st.session_stage.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("whats up?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.message.append({"role": "assistant", "content": response})
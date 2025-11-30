import streamlit as st
import re
import requests

WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjcwNTZkMDYzNjA0M2M1MjY1NTUzMDUxMzUi_pc" 


def is_valid_email(email: str) -> bool:
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_pattern, email) is not None



@st.dialog("Contact Me")
def show_contact_form():
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("E-mail")
        message = st.text_area("Message")

        submitted = st.form_submit_button("Submit")

    if submitted:
        # Email validation
        if not is_valid_email(email):
            st.error("❌ Please enter a valid email address.")
            return

        # Send to webhook
        data = {"email": email, "name": name, "message": message}
        try:
            response = requests.post(WEBHOOK_URL, json=data)
            response.raise_for_status()
            st.success("✅ Thank you! Your message has been sent.")
        except Exception as e:
            st.error(f"❌ Failed to send message: {e}")



st.title("About Me")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/logo.JPG")

with col2:
    st.title("Oti Oseji", anchor=False)
    st.write(
        "Computer Science + AI Student @ Uni of Plymouth,\n"
        "AI and Cyber Risk Research Intern @ E3 Consulting"
    )

if st.button("Contact Me"):
    show_contact_form()

import streamlit as st
from database import get_connection
from datetime import datetime

def client_page():
    st.set_page_config(page_title="Client Query Page", layout="wide")
    st.title("👤 Client Query Page")

    st.markdown("---")  # horizontal separator

    # --- Info / instructions ---
    st.info("Fill out the form below to submit your query. Our support team will get back to you as soon as possible.")

    # --- Form container ---
    with st.form("query_form"):
        col1, col2 = st.columns(2)

        with col1:
            email = st.text_input("Email ID", placeholder="example@example.com")
            mobile = st.text_input("Mobile Number", placeholder="Enter 10-digit number")

        with col2:
            heading = st.text_input("Query Heading", placeholder="Brief summary of your issue")
            description = st.text_area("Query Description", placeholder="Describe your issue in detail here...")

        submit = st.form_submit_button("Submit Query")

    # --- Form submission ---
    if submit:
        if not email or not mobile or not heading or not description:
            st.error("All fields are required!")
        else:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO client_queries
                (email_id, mobile_number, query_heading, query_description, status, query_created_time, query_closed_time)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                email,
                mobile,
                heading,
                description,
                "Open",
                datetime.now(),
                None
            ))

            conn.commit()
            conn.close()

            st.success(f"✅ Query Submitted Successfully on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}!")


    st.markdown("---")

    # --- Footer / Logout ---
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("Logout"):
            st.session_state.page = "login"
            st.rerun()
            # st.experimental_rerun()

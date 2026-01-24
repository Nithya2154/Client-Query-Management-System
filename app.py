import streamlit as st
import database as db
import hashlib

st.set_page_config(page_title="Login System", layout="centered")

# ------------------ USER DATABASE (DEMO) ------------------
USERS = {
    "client1": {"password": "client123", "role": "Client"},
    "support1": {"password": "12345", "role": "Support Team"}
}

# Session state init
if "page" not in st.session_state:
    st.session_state.page = "login"

# ------------------ LOGIN PAGE ------------------
if st.session_state.page == "login": 

    st.markdown("<h2 style='text-align:center;'>🔐 Login</h2>", unsafe_allow_html=True)

    with st.container():
        # st.markdown("<div class='login-box'>", unsafe_allow_html=True)

        with st.form("login_form"):
            username = st.text_input("Username",key='uname')
            username_error=st.empty()
            password = st.text_input("Password", type="password",key='pass')
            password_error=st.empty()
            role = st.selectbox("Login As", ["Client", "Support Team"],key='Role')

            col1, col2 = st.columns(2)
            with col1:
                login_btn = st.form_submit_button("Login")
            with col2:
                cancel_btn = st.form_submit_button("Cancel")
                

    if login_btn:
        valid=True
        if not username:
            username_error.error("Please enter a Username")
            valid=False
        else:
            username_error.empty()
        if not password:
            password_error.error("Please enter a Password")
            valid=False
        else:
            password_error.empty()
       
        if valid:
            try:
                conn=db.get_connection()
                cursor = conn.cursor()
                hashed_password = hashlib.sha256(password.encode()).hexdigest()

                query = """
                    SELECT * FROM users
                    WHERE username = %s AND hashed_password = %s
                    """

                cursor.execute(query, (username, hashed_password))
                user = cursor.fetchone()
                if user:
                    st.session_state.username = username
                    st.session_state.role = role
                    st.session_state.page = "client" if role == "Client" else "support"
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password")
                # if username in USERS:
                #     if USERS[username]["password"] == password and USERS[username]["role"] == role:
                #         st.session_state.username = username
                #         st.session_state.role = role
                #         st.session_state.page = "client" if role == "Client" else "support"
                #         st.rerun()
                #     else:
                #         st.error("❌ Invalid password or role")
                # else:
                #     st.error("❌ User not found")
            except Exception as e:
                st.title('Invalid Connection')
                st.caption(str(e))
    if cancel_btn:
        st.rerun()

# ------------------ CLIENT PAGE ------------------
elif st.session_state.page == "client":
    import client
    client.client_page()

# ------------------ SUPPORT TEAM PAGE ------------------
elif st.session_state.page == "support":
    import support_team
    support_team.support_page()


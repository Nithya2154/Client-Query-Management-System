import streamlit as st
import pandas as pd
from database import get_connection
from datetime import datetime

def support_page():
    st.title("🛠 Support Dashboard")

    # --- Filter by status ---
    status_filter = st.selectbox("Filter by Status", ["All", "Opened", "Closed"])
    try:
        # --- Connect to DB ---
        conn = get_connection()
        
        # --- Load data ---
        query = """
            SELECT query_id, email_id, mobile_number, query_heading, query_description, 
                   query_created_time, status, query_closed_time 
            FROM client_queries
        """
        params = ()
        if status_filter != "All":
            query += " WHERE status=%s"
            params = (status_filter,)
        query+=" ORDER BY query_id"
        df = pd.read_sql(query, conn, params=params)
    
        # --- Dashboard summary ---
        st.subheader("Summary")
        total_queries = len(df)
        open_queries = len(df[df['status'] == 'Opened'])
        closed_queries = len(df[df['status'] == 'Closed'])
    
        st.markdown(f"- **Total Queries:** {total_queries}")
        st.markdown(f"- **Open Queries:** {open_queries}")
        st.markdown(f"- **Closed Queries:** {closed_queries}")
    
        # Optional: display a bar chart
        st.bar_chart(df['status'].value_counts())
    
        # --- Display all queries ---
        st.subheader("All Queries")
        st.dataframe(df)
    
        # --- Close a query ---
        st.subheader("Close a Query")
        query_id_input = st.text_input("Enter Query ID")
    
        if st.button("Close Query") and query_id_input:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE client_queries
                SET status='Closed', query_closed_time=%s
                WHERE query_id=%s
            """, (
                datetime.now(),
                query_id_input
            ))
            conn.commit()
            st.success(f"Query {query_id_input} Closed Successfully!")
            # st.rerun()
    
            # st.experimental_rerun()
    
        # --- Logout ---
        if st.button("Logout"):
            st.session_state.page = "login"
            st.rerun()
        # st.experimental_rerun()

        conn.close()
    except Exception as e:
        st.caption(str(e))
    



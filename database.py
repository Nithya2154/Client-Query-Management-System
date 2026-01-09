import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="support",
        user="postgres",
        password="12345",
        port="5432"
    )

# def create_tables():
#     conn = get_connection()
#     cursor = conn.cursor()

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         username TEXT PRIMARY KEY,
#         hashed_password TEXT,
#         role TEXT
#     )
#     """)

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS queries (
#         id SERIAL PRIMARY KEY,
#         email TEXT,
#         mobile TEXT,
#         heading TEXT,
#         description TEXT,
#         status TEXT,
#         created_time TIMESTAMP,
#         closed_time TIMESTAMP
#     )
#     """)

    # conn.commit()
    # cursor.close()
    # conn.close()

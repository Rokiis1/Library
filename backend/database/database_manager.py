import psycopg2


def get_connection():
    conn = psycopg2.connect(
        host="db.uzfyszuaseakoacmgvpt.supabase.co",
        database="postgres",
        port="5432",
        user="postgres",
        password="GdX1ZhGsBV0h68Cu",
    )
    return conn


def close_connection(conn):
    conn.close()

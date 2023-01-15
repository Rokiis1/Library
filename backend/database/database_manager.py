import psycopg2


def get_connection():
    conn = psycopg2.connect(
        host="database-1.cimi9tl7ksk8.eu-west-2.rds.amazonaws.com",
        database="postgres",
        port="5432",
        user="postgres",
        password="GdX1ZhGsBV0h68Cu",
    )
    return conn


def close_connection(conn):
    conn.close()

def create_table(conn):
    cursor = conn.cursor()
    query = """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) NOT NULL,
            hashed_password VARCHAR(255) NOT NULL,
            is_active BOOLEAN DEFAULT true NOT NULL
        );
    """
    cursor.execute(query)
    conn.commit()
    print("Table created successfully")
    cursor.close()
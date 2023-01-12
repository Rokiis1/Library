import psycopg2
from flask import Flask

app = Flask(__name__)


def create_connection():
    connection = psycopg2.connect(
        host="db.uzfyszuaseakoacmgvpt.supabase.co",
        database="postgres",
        port="5432",
        user="postgres",
        password="6e8CAWK6Uch2!6X"
    )
    return connection


connection = create_connection()

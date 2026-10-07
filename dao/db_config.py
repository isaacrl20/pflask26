import sqlite3
import psycopg2

# path = url de conexão
DB_PATH = "postgresql://neondb_owner:npg_oWFyBZA8ShE1@ep-gentle-block-b7dsn1wf-pooler.c-13.us-east-1.aws.neon.tech/neondb?channel_binding=require&sslmode=require"

def get_connection():
    conn = psycopg2.connect (DB_PATH , sslmode='require')
    return conn

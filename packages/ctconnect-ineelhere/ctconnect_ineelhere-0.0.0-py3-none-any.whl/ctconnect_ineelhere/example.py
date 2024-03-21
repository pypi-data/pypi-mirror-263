
import psycopg2
import pandas as pd

def hello():
    return "Hello there! 😃"

def connect_to_database(aact_username, aact_password):
    # PostgreSQL connection parameters
    conn_params = {
        "host": "aact-db.ctti-clinicaltrials.org",
        "port": 5432,
        "user": aact_username,
        "password": aact_password,
        "database": "aact",
    }

    # Establish a connection to the database
    try:
        conn = psycopg2.connect(**conn_params)
        print("Connected to the database ✅ \n")
        return conn
    except Exception as e:
        print(f"Error connecting to the database ⚠️ :\n {e}")
        return None

def execute_query(conn, query):
    try:
        df = pd.read_sql_query(query, conn)
        print("Data loaded into Pandas DataFrame ✅ \n")
        print(df)
        return df
    except Exception as e:
        print(f"Error executing query: {e}")
        return None
    finally:
        # Close the database connection
        conn.close()
        print("Connection closed")
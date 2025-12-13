import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

try:
    conn = psycopg2.connect(
        host="my-postgres-db.c0tikqw806cm.us-east-1.rds.amazonaws.com",
        port="5432",
        database="my-postgres-db",
        user="sridevi",
        password="sridevi123"
    )
    cur = conn.cursor()
    
    # Create the table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            feedback TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    conn.commit()
    print("✓ Table 'feedback' created successfully!")
    
    cur.close()
    conn.close()
except Exception as e:
    print(f"✗ Error creating table: {e}")

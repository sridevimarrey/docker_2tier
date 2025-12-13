import psycopg2
from psycopg2 import sql

# First, connect to default 'postgres' database to create our database
try:
    conn = psycopg2.connect(
        host="my-postgres-db.c0tikqw806cm.us-east-1.rds.amazonaws.com",
        port=5432,
        database="postgres",  # Connect to default postgres DB first
        user="sridevi",
        password="sridevi123"
    )
    conn.autocommit = True
    cur = conn.cursor()
    
    # Create database if it doesn't exist
    cur.execute("CREATE DATABASE \"my-postgres-db\"")
    print("✓ Database 'my-postgres-db' created successfully!")
    
    cur.close()
    conn.close()
except psycopg2.errors.DuplicateDatabase:
    print("⚠ Database 'my-postgres-db' already exists")
except Exception as e:
    print(f"✗ Error creating database: {e}")

# Now connect to our database and create the table
try:
    conn = psycopg2.connect(
        host="my-postgres-db.c0tikqw806cm.us-east-1.rds.amazonaws.com",
        port=5432,
        database="my-postgres-db",
        user="sridevi",
        password="sridevi123"
    )
    cur = conn.cursor()
    
    # Create table
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
    print("✓ Database setup complete!")
    
    cur.close()
    conn.close()
except Exception as e:
    print(f"✗ Error creating table: {e}")

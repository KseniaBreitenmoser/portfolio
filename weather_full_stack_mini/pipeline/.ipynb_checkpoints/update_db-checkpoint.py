import sqlite3
from fetch_weather import fetch_weather

DB_PATH = "data/weather.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Create table if it doesn't exist
    c.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            date TEXT PRIMARY KEY,
            temp_max REAL,
            temp_min REAL
        )
    """)

    conn.commit()
    conn.close()

def insert_data(df):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    for _,row in df.iterrows():
        try:
            c.execute("""
                INSERT INTO weather (date, temp_max, temp_min)
                VALUES (?, ?, ?)
            """, (row["date"], row["temp_max"], row["temp_min"]))
        except sqlite3.IntegrityError:
            # Skip rows with duplicate date
            pass

    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("Fetching data from Open-Meteo...")
    df = fetch_weather()
    print("Initializing DB...")
    init_db()
    print("Inserting data...")
    insert_data(df)
    print("Done.")
    
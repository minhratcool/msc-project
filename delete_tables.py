import sqlite3

def drop_all_tables(db_connection):
    cursor = db_connection.cursor()

    # Get the list of table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()

    # Drop each table
    for table_name in table_names:
        cursor.execute(f"DROP TABLE {table_name[0]}")

    db_connection.commit()

def delete_minhtn286(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("delete from ")


if __name__ == "__main__":
    try:
        db_connection = sqlite3.connect('user_data.db')
        # drop_all_tables(db_connection)
        print("All tables dropped successfully.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        if db_connection:
            db_connection.close()

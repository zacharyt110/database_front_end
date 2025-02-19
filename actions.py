import mysql.connector

def get_people():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="BlackHoles!1",
            database="test_database"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM people")
        people = cursor.fetchall()
        for person in people:
            print(f"{person[0]}: {person[1]}")
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    get_people()

import mysql.connector

class Actions:
    def __init__(self, gui):
        self.gui = gui

    # def database_credentials(self):


    def send_to_status_log(self, message):
        self.gui.update_status_log(message)

    def search_button_action(self, first_name, last_name):
        self.send_to_status_log(f"Button clicked with first name: {first_name} and last name: {last_name}")

    def get_people(self):
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
    from gui import GUI
    gui = GUI()
    actions = Actions(gui)
    actions.get_people()

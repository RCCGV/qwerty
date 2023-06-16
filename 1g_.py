import sqlite3



class User:
    def __init__(self, name: str, surname: str, age: int, gender: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender


def add_new_user(cur: sqlite3.Cursor, user: User):
    command = """
    INSERT
    INTO
    users(name, surname, age, gender)
    VALUES(?, ?, ?, ?);
    """
    cur.execute(command, (user.name, user.surname, user.age, user.gender))


def get_all_users(cur: sqlite3.Cursor):
    command = """
    SELECT * FROM users;
    """
    result = cur.execute(command)
    return result.fetchall()


def get_user(cur: sqlite3.Cursor, user_id: int):
    command = """
    SELECT * FROM users WHERE id = ?;
    """
    result = cur.execute(command, (user_id,))
    return result.fetchone()


def create_user_table(cur: sqlite3.Cursor):
    command = """
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    age INTEGER,
    gender TEXT);
    """
    cur.execute(command)


def clear_user_table(cur: sqlite3.Cursor):
    command = """
    DELETE FROM users;
    """
    cur.execute(command)


def update_user_name(cur: sqlite3.Cursor, name: str, user_id: int):
    command = """
    UPDATE users SET name = ? WHERE id = ?;
    """
    cur.execute(command, (name, user_id))


def delete_user_data(cur: sqlite3.Cursor, user_id: int):
    command = """
    DELETE FROM users WHERE id = ?;
    """
    cur.execute(command, (user_id,))


if __name__ == "__main__":
    with sqlite3.connect('sqlite.db') as connection:
        cursor = connection.cursor()

        
        user = User(name='Максим', surname='Максимов', age=16, gender='М')
        add_new_user(cursor, user=user)
        users = get_all_users(cursor)
        
        delete_user_data(cursor, 1)
        
        print(users)

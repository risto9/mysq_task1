import mysql.connector

def create_connection():
    conn = mysql.connector.connect(
        host='localhost',  # или '127.0.0.1'
        user='root',
        password='Ristedoma321323A#',
        database='tasks_db'
    )
    return conn

def create_table(conn):
    sql = '''CREATE TABLE IF NOT EXISTS tasks (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                priority INT
            );'''
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

def add_task(conn, task):
    sql = '''INSERT INTO tasks (name, priority) VALUES (%s, %s)'''
    cursor = conn.cursor()
    cursor.execute(sql, task)
    conn.commit()

def get_tasks(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    return rows

def main():
    conn = create_connection()
    create_table(conn)
    
    while True:
        print("1. Додади задача")
        print("2. Прегледај задачи")
        print("3. Излез")
        choice = input("Изберете опција: ")
        
        if choice == "1":
            name = input("Внесете име на задача: ")
            priority = int(input("Внесете приоритет (1-5): "))
            add_task(conn, (name, priority))
        elif choice == "2":
            tasks = get_tasks(conn)
            for task in tasks:
                print(task)
        elif choice == "3":
            break

main()

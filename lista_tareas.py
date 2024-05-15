import sqlite3

# Conexión a la base de datos 
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# Creación de la tabla 
cursor.execute('''CREATE TABLE tasks (
                    id INTEGER PRIMARY KEY,
                    task TEXT NOT NULL,
                    completed BOOLEAN NOT NULL
                )''')

def add_task(task):
    cursor.execute('INSERT INTO tasks (task, completed) VALUES (?, ?)', (task, False))
    conn.commit()
    print("Tarea agregada correctamente.")

def delete_task(task_id):
    cursor.execute('DELETE FROM tasks WHERE id=?', (task_id,))
    conn.commit()
    print("Tarea eliminada correctamente.")

def mark_task_completed(task_id):
    cursor.execute('UPDATE tasks SET completed=? WHERE id=?', (True, task_id))
    conn.commit()
    print("Tarea marcada como completada.")

def display_tasks():
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    print("\nLista de tareas:")
    for task in tasks:
        status = "Completada" if task[2] else "Pendiente"
        print(f"{task[0]}. {task[1]} - {status}")

# Ejemplo de uso
while True:
    print("\n1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Marcar tarea como completada")
    print("4. Mostrar tareas")
    print("5. Salir")

    choice = input("Ingrese el número de la opción que desea realizar: ")

    if choice == '1':
        task = input("Ingrese la tarea que desea agregar: ")
        add_task(task)
    elif choice == '2':
        task_id = int(input("Ingrese el ID de la tarea que desea eliminar: "))
        delete_task(task_id)
    elif choice == '3':
        task_id = int(input("Ingrese el ID de la tarea que desea marcar como completada: "))
        mark_task_completed(task_id)
    elif choice == '4':
        display_tasks()
    elif choice == '5':
        break
    else:
        print("Opción no válida. Por favor, ingrese un número válido.")
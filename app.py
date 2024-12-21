from flask import Flask, render_template
import pandas as pd
import sqlite3

src_data = [
    ['Миша', 'Позвать в баню', '2024-12-31'],
    ['Маша', 'Отмыть раковину', '2026-01-31'],
    ['Мойша', 'Отдать долг', '2030-12-30'],
    ['Кеша', 'Поменять клетку', '2024-12-20'],
    ['Коша', 'Заказать корм в мешках', '2025-01-03'],
    ['Паша', 'Победить', '2024-12-28'],
    ['Тиша', 'Сказать правду', '2025-01-06'],
    ['Платиша', 'Пересмотреть фильм', '2025-01-07'],
    ['Рикша', 'Заказать, гонять, дать на чай', '2025-01-10'],
    ['Крыша', 'Чинить. Содержать в порядке!','2025-04-01']
]
df=pd.DataFrame(src_data, columns=['who', 'what', 'when'])
connection  = sqlite3.connect('todo.db')
df.to_sql('My_ToDo', connection, index = False, if_exists='replace')
connection.close()
# sql = '''
#         select *
#             from 'My_ToDo'
#     '''
# t=pd.read_sql(sql, connection)
# print(t)

app = Flask(__name__)

def get_data():
    connection = sqlite3.connect('todo.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM "My_ToDo"')
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

@app.route('/')
def index():
    todo_items = get_data()
    return render_template('index.html', todo_items=todo_items)

if __name__ == '__main__':
    app.run(debug=True)

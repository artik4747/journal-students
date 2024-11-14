import sqlite3

class SQLiteCRUD:
    def __init__(self, db_name):
        """Инициализация подключения к базе данных."""
        self.db_name = db_name
        with sqlite3.connect(db_name) as self.connection:
            self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        """Создание таблицы."""
        columns_definition = ', '.join(f"{col_name} {col_type}" for col_name, col_type in columns.items())
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_definition});"
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert(self, table_name, **kwargs):
        """Вставка новой записи в таблицу."""
        columns = ', '.join(kwargs.keys())
        placeholders = ', '.join('?' for _ in kwargs)
        values = tuple(kwargs.values())
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders});"
        self.cursor.execute(insert_query, values)
        self.connection.commit()

    def read(self, table_name, columns='*', where_clause=None):
        """Чтение записей из таблицы."""
        if where_clause:
            select_query = f"SELECT {columns} FROM {table_name} WHERE {where_clause};"
        else:
            select_query = f"SELECT {columns} FROM {table_name};"
        self.cursor.execute(select_query)
        results = self.cursor.fetchall()
        return results if results else None
    
    def update(self, table_name, set_clause, where_clause):
        """Обновление записей в таблице."""
        update_query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause};"
        self.cursor.execute(update_query)
        self.connection.commit()

    def delete(self, table_name, where_clause):
        """Удаление записей из таблицы."""
        delete_query = f"DELETE FROM {table_name} WHERE {where_clause}"
        self.cursor.execute(delete_query)
        self.connection.commit()

    def close(self):
        """Закрытие подключения к базе данных."""
        self.connection.close()

db = SQLiteCRUD('sqlite4.db')

# db.create_table('Student',{
#     'Ism':'VARCHAR(50)',
#     'Familiya':'VARCHAR(50)',
#     'Fan':'VARCHAR(50)',
#     'Ball':'VARCHAR(50)',
#     'date':'VARCHAR(50)'
#     }
# )

# db.insert('Student',ism='natalii',familiya='vladimirova',fan='math',ball='4',date='09.09.2024')
db.insert('Student',ism='alina',familiya='aliyeva',fan='math',ball='5',date='09.09.2024')
db.insert('Student',ism='dasha',familiya='alixanova',fan='math',ball='5',date='09.09.2024')
db.insert('Student',ism='danya',familiya='krasnosvetov',fan='math',ball='5',date='09.09.2024')
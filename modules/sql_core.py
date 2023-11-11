import sqlite3


def insert_several_records(database_name, multiple_records):
    my_connection=sqlite3.connect(database_name)
    my_cursor=my_connection.cursor()
    for i in multiple_records:
        my_cursor.execute(i)
    my_connection.commit()
    my_connection.close()

def read_records(database_name, table_name):
    my_connection=sqlite3.connect(database_name)
    my_cursor=my_connection.cursor()
    my_cursor.execute("SELECT * FROM {}".format(table_name))
    records=my_cursor.fetchall()
    my_connection.close()
    return records

def read_last_record(database_name, table_name):
    my_connection=sqlite3.connect(database_name)
    my_cursor=my_connection.cursor()
    my_cursor.execute("SELECT * FROM {} ORDER BY ID DESC LIMIT 1".format(table_name))
    records=my_cursor.fetchall()
    my_connection.close()
    return records[0]

def update_record(database_name, record):
    my_connection=sqlite3.connect(database_name)
    my_cursor=my_connection.cursor()
    my_cursor.execute(record)
    my_connection.commit()
    my_connection.close()

def remove_record(database_name, record):
    my_connection=sqlite3.connect(database_name)
    my_cursor=my_connection.cursor()
    my_cursor.execute(record)
    my_connection.commit()
    my_connection.close()

def run_command(database_name, command):
    my_connection=sqlite3.connect(database_name)
    my_cursor=my_connection.cursor()
    my_cursor.execute(command)
    my_connection.commit()
    my_connection.close()

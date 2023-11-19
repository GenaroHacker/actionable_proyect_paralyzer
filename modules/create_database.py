import sqlite3
from google.colab import files
import os
from actionable_builder.modules.add_example_data import add_example_data

# Constant for the database name
DATABASE_NAME = 'tasks.db'

def create_table(database_name, table_name, table_structure):
    with sqlite3.connect(database_name) as conn:
        cursor = conn.cursor()
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({table_structure});')
        conn.commit()

def insert_record(database_name, insert_sql, params=()):
    with sqlite3.connect(database_name) as conn:
        cursor = conn.cursor()
        cursor.execute(insert_sql, params)
        conn.commit()
        return cursor.lastrowid

def create_empty_database():
    tables = {
        "PLACES": "ID INTEGER PRIMARY KEY, NAME TEXT UNIQUE, IS_SELECTED BOOLEAN DEFAULT FALSE",
        "CONTEXTS": "ID INTEGER PRIMARY KEY, PLACE_ID INTEGER, NAME TEXT, RANK INTEGER, "
                    "FOREIGN KEY(PLACE_ID) REFERENCES PLACES(ID), UNIQUE(PLACE_ID, NAME)",
        "TAGS": "ID INTEGER PRIMARY KEY, CONTEXT_ID INTEGER, NAME TEXT, RANK INTEGER, "
                "FOREIGN KEY(CONTEXT_ID) REFERENCES CONTEXTS(ID), UNIQUE(CONTEXT_ID, NAME)",
        "TASKS": "ID INTEGER PRIMARY KEY, TAG_ID INTEGER, NAME TEXT, RANK INTEGER, "
                 "FOREIGN KEY(TAG_ID) REFERENCES TAGS(ID), UNIQUE(TAG_ID, NAME)",
        "STEPS": "ID INTEGER PRIMARY KEY, TASK_ID INTEGER, NAME TEXT, ORDER_SEQUENCE INTEGER, "
                 "MINUTES INTEGER, FOREIGN KEY(TASK_ID) REFERENCES TASKS(ID), UNIQUE(TASK_ID, ORDER_SEQUENCE)",
        "PLACEHOLDERS": "ID INTEGER PRIMARY KEY, TYPE TEXT, VALUE TEXT, RANK INTEGER, UNIQUE(TYPE, VALUE)",
        "HISTORY": "ID INTEGER PRIMARY KEY, STEP_ID INTEGER, ACTION TEXT, TIME TEXT, "
                   "FOREIGN KEY(STEP_ID) REFERENCES STEPS(ID)"
    }
    for table_name, table_structure in tables.items():
        create_table(DATABASE_NAME, table_name, table_structure)

def check_or_insert_with_parent(table, name, parent_id_column, parent_id):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()

        if table == "PLACES":
            cursor.execute("SELECT ID FROM PLACES WHERE NAME = ?", (name,))
            record = cursor.fetchone()
            if record is None:
                is_first_place = cursor.execute("SELECT COUNT(*) FROM PLACES").fetchone()[0] == 0
                is_selected = 1 if is_first_place else 0
                cursor.execute("INSERT INTO PLACES (NAME, IS_SELECTED) VALUES (?, ?)", (name, is_selected))
                conn.commit()
                if is_selected:
                    new_place_id = cursor.lastrowid
                    cursor.execute("UPDATE PLACES SET IS_SELECTED = 0 WHERE ID != ?", (new_place_id,))
                    conn.commit()
                return cursor.lastrowid
            return record[0]
        else:
            cursor.execute(f"SELECT ID FROM {table} WHERE NAME = ? AND {parent_id_column} = ?", (name, parent_id))
            record = cursor.fetchone()
            if record is None:
                cursor.execute(f"INSERT INTO {table} ({parent_id_column}, NAME, RANK) VALUES (?, ?, NULL)", (parent_id, name))
                conn.commit()
                return cursor.lastrowid
            return record[0]

def check_step_exists(task_id, order_sequence):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM STEPS WHERE TASK_ID = ? AND ORDER_SEQUENCE = ?", (task_id, order_sequence))
        count = cursor.fetchone()[0]
        return count > 0

def add_task(task_input):
    place_id = check_or_insert_with_parent('PLACES', task_input["place"], 'ID', None)
    context_id = check_or_insert_with_parent('CONTEXTS', task_input["context"], 'PLACE_ID', place_id)
    tag_id = check_or_insert_with_parent('TAGS', task_input["tag"], 'CONTEXT_ID', context_id)
    task_id = check_or_insert_with_parent('TASKS', task_input["task"], 'TAG_ID', tag_id)

    for index, step in enumerate(task_input["steps"], start=1):
        if not check_step_exists(task_id, index):
            step_sql = "INSERT INTO STEPS (TASK_ID, NAME, ORDER_SEQUENCE, MINUTES) VALUES (?, ?, ?, NULL)"
            insert_record(DATABASE_NAME, step_sql, (task_id, step, index))

def add_placeholders(placeholders_dict):
    insert_sql = "INSERT INTO PLACEHOLDERS (TYPE, VALUE, RANK) VALUES (?, ?, ?)"
    for placeholder_type, values in placeholders_dict.items():
        for value in values:
            rank = None
            try:
                insert_record(DATABASE_NAME, insert_sql, (placeholder_type, value, rank))
            except sqlite3.IntegrityError:
                continue

def initialize_database(user_choice):
    print("\n1. Create empty database\n2. Create database with example data\n3. Upload database\n")
    user_choice = str(user_choice)
    print(user_choice)
    print("\n")
    if user_choice == '1':
        create_empty_database()
    elif user_choice == '2':
        create_example_database()
        tasks, placeholders = add_example_data()
        for task in tasks:
            add_task(task)
        add_placeholders(placeholders)
    elif user_choice == '3':
        uploaded_files = files.upload()
        for filename in uploaded_files.keys():
            os.rename(filename, DATABASE_NAME)
            print(f"Uploaded file '{filename}' has been renamed to '{DATABASE_NAME}'")

def create_example_database():
    create_empty_database()
    # Insert example data into each table

def download_database():
    files.download(DATABASE_NAME)


from google.colab import files

from actionable.modules.sql_core import (
    create_table, 
    insert_record, 
    insert_several_records, 
    read_records,
    read_last_record,
    update_record,
    remove_record,
    run_command
)

DB_NAME = "time_management.db"

def create_tables():
    tables = {
        "CONTEXTS": """
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT,
            EXPECTED_PERCENTAGE INTEGER,
            R REAL,
            G REAL,
            B REAL
        """,
        "TAGS": """
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT,
            CONTEXT_ID INTEGER REFERENCES CONTEXTS(ID),
            RANK INTEGER
        """,
        "TASKS": """
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT,
            TAG_ID INTEGER REFERENCES TAGS(ID),
            RANK INTEGER,
            DEPENDENCY_ID INTEGER REFERENCES TASKS(ID),
            START TIME,
            END TIME,
            WEEKDAYS TEXT
        """,
        "SUBTASKS": """
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            TASK_ID INTEGER REFERENCES TASKS(ID),
            ORDER_SEQUENCE INTEGER,
            NAME TEXT,
            DETAILS TEXT,
            DURATION INTEGER
        """,
        "PLACEHOLDERS": """
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            TYPE TEXT,
            VALUE TEXT
        """,
        "HISTORY": """
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            SUBTASK_ID INTEGER REFERENCES SUBTASKS(ID),
            ACTION TEXT,
            TIME DATETIME
        """
    }

    for table_name, table_structure in tables.items():
        create_table(DB_NAME, table_name, table_structure)

def populate_contexts():
    records = [
        ("Create", 25, 0.00, 0.45, 1.00),
        ("Exercise", 25, 1.00, 0.46, 0.00),
        ("Recreate", 25, 0.13, 0.64, 0.15),
        ("Sleep", 25, 0.46, 0.00, 0.00)
    ]
    
    for record in records:
        sql_command = f"INSERT INTO CONTEXTS (NAME, EXPECTED_PERCENTAGE, R, G, B) VALUES ('{record[0]}', {record[1]}, {record[2]}, {record[3]}, {record[4]})"
        insert_record(DB_NAME, sql_command)


def populate_tags():
    records = [
        ("write", 1, 1),
        ("design", 1, 2),
        ("program", 1, 3),
        ("brainstorm", 1, 4),
        ("hit", 2, 1),
        ("strengthen", 2, 2),
        ("cardio", 2, 3),
        ("sport", 2, 4),
        ("read", 3, 1),
        ("watch", 3, 2),
        ("game", 3, 3),
        ("outdoor", 3, 4),
        ("sleep", 4, 1),
        ("meditate", 4, 2)
    ]
    
    for record in records:
        sql_command = f"INSERT INTO TAGS (NAME, CONTEXT_ID, RANK) VALUES ('{record[0]}', {record[1]}, {record[2]})"
        insert_record(DB_NAME, sql_command)


def populate_tasks():
    records = [
        ("Write a thank you list", 1, 1, "yyyyyyy", None, "08:00:00", "20:00:00"),
        ("Automate a repetitive computer task", 3, 1, "yyyyyyy", None, "08:00:00", "20:00:00"),
        ("Learn a new %programming_language% concept", 3, 2, "yyyyyyy", None, "08:00:00", "20:00:00"),
        ("Plan meals for the upcoming week", 4, 1, "yyyyyyy", None, "08:00:00", "20:00:00"),
        ("Do a quick %exercise_name% session", 5, 1, "yyyyyyy", 6, "08:00:00", "20:00:00"),
        ("Perform basic %exercise_name%", 6, 1, "yyyyyyy", 6, "08:00:00", "20:00:00"),
        ("Watch %movie_name%", 9, 1, "yyyyyyy", None, "08:00:00", "20:00:00"),
        ("Go to sleep", 13, 1, "yyyyyyy", None, "08:00:00", "20:00:00")
    ]

    for record in records:
        dependency = "NULL" if record[4] is None else record[4]
        sql_command = f"INSERT INTO TASKS (NAME, TAG_ID, RANK, WEEKDAYS, DEPENDENCY_ID, START, END) VALUES ('{record[0]}', {record[1]}, {record[2]}, '{record[3]}', {dependency}, '{record[5]}', '{record[6]}')"
        insert_record(DB_NAME, sql_command)


def populate_subtasks():
    records = [
        # Subtasks for Task 1 ('Write a thank you list')
        (1, 1, "Choose person", None, 5),
        (1, 2, "Write message", "Express gratitude sincerely", 10),

        # Subtasks for Task 2 ('Automate a repetitive computer task')
        (2, 1, "Identify task", None, 10),
        (2, 2, "Write script for %programming_language%", "Research library or framework if needed", 60),
        (2, 3, "Test script", None, 30),

        # Subtasks for Task 3 ('Learn a new programming concept')
        (3, 1, "Choose %programming_language% concept", None, 10),
        (3, 2, "Read %programming_language% documentation", None, 30),
        (3, 3, "Implement example in %programming_language%", None, 45),

        # Subtasks for Task 4 ('Plan meals for the upcoming week')
        (4, 1, "Choose recipes", None, 20),
        (4, 2, "Make a grocery list", None, 15),
        (4, 3, "Schedule cooking times", None, 10),

        # Subtasks for Task 5 ('Do a quick workout session')
        (5, 1, "Prepare for %exercise_name% session", "Gather equipment or clear space", 10),
        (5, 2, "Perform %exercise_name%", None, 30),
        (5, 3, "Workout", "Follow exercise routine", 20),

        # Subtasks for Task 6 ('Perform basic push-ups, squats, and lunges')
        (6, 1, "Warm up", None, 5),
        (6, 2, "Perform %exercise_name%", "Keep good form", 20),
        (6, 3, "Perform squats", None, 10),
        (6, 4, "Perform lunges", None, 10),

        # Subtasks for Task 7 ('Watch a recommended movie')
        (7, 1, "Choose %movie_name%", None, 5),
        (7, 2, "Set up watching space", "Comfortable seating, snacks", 10),
        (7, 3, "Watch %movie_name%", None, 120),

        # Subtasks for Task 8 ('Go to sleep')
        (8, 1, "Prepare room", "Dim lights, quiet environment", 5),
        (8, 2, "Brush teeth", None, 5),
        (8, 3, "Lay in bed", None, 1)
    ]

    for record in records:
        if record[3] is None:
            sql_command = f"INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DURATION) VALUES ({record[0]}, {record[1]}, '{record[2]}', {record[4]})"
        else:
            sql_command = f"INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES ({record[0]}, {record[1]}, '{record[2]}', '{record[3]}', {record[4]})"
        insert_record(DB_NAME, sql_command)

def populate_placeholders():
    records = [
        ("programming_language", "Python"),
        ("programming_language", "JavaScript"),
        ("programming_language", "Java"),
        ("programming_language", "C++"),

        ("movie_name", "Inception"),
        ("movie_name", "The Matrix"),
        ("movie_name", "Interstellar"),

        ("exercise_name", "push ups"),
        ("exercise_name", "sit ups"),
        ("exercise_name", "squats"),
        ("exercise_name", "jumping jacks")
    ]

    for record in records:
        sql_command = f"INSERT INTO PLACEHOLDERS (TYPE, VALUE) VALUES ('{record[0]}', '{record[1]}')"
        insert_record(DB_NAME, sql_command)

def create_example_database():
    create_tables()
    populate_contexts()
    populate_tags()
    populate_tasks()
    populate_subtasks()
    populate_placeholders()

    # Trigger download
    files.download(DB_NAME)

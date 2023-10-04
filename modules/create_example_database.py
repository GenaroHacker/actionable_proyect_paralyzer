def create_example_database():
    # @title Create Tables
    def create_tables():
        # Define the structure for each table with the specified changes
        tables = {
            "CONTEXTS": """
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME TEXT,
                EXPECTED_PERCENTAGE INTEGER,
                FUTURE_EXPECTED_PERCENTAGE INTEGER,
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
                FREQUENCY REAL,
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
    
        # Create each table with the updated structure
        for table_name, table_structure in tables.items():
            create_table("time_management.db", table_name, table_structure)
    
    # @title Populate Example Records
    def populate_tables():
        # Populate the CONTEXTS table
        contexts_records = [
            "INSERT INTO CONTEXTS (NAME, EXPECTED_PERCENTAGE, FUTURE_EXPECTED_PERCENTAGE, R, G, B) VALUES ('Create', 25, 25, 0.00, 0.45, 1.00)",
            "INSERT INTO CONTEXTS (NAME, EXPECTED_PERCENTAGE, FUTURE_EXPECTED_PERCENTAGE, R, G, B) VALUES ('Exercise', 25, 25, 1.00, 0.46, 0.00)",
            "INSERT INTO CONTEXTS (NAME, EXPECTED_PERCENTAGE, FUTURE_EXPECTED_PERCENTAGE, R, G, B) VALUES ('Recreate', 25, 25, 0.13, 0.64, 0.15)",
            "INSERT INTO CONTEXTS (NAME, EXPECTED_PERCENTAGE, FUTURE_EXPECTED_PERCENTAGE, R, G, B) VALUES ('Sleep', 25, 25, 0.46, 0.00, 0.00)"
        ]
        insert_several_records("time_management.db", contexts_records)
    
        # Populate the TAGS table
        tags_records = [
            "INSERT INTO TAGS (NAME, CONTEXT_ID, RANK) VALUES ('write', 1, 1)",
            "INSERT INTO TAGS (NAME, CONTEXT_ID, RANK) VALUES ('design', 1, 2)",
            "INSERT INTO TAGS (NAME, CONTEXT_ID, RANK) VALUES ('program', 1, 3)",
            "INSERT INTO TAGS (NAME, CONTEXT_ID, RANK) VALUES ('brainstorm', 1, 4)",
            "INSERT INTO TAGS (NAME, CONTEXT_ID, RANK) VALUES ('hit', 2, 1)",
            "INSERT INTO TAGS (NAME, CONTEXT_ID, RANK) VALUES ('strengthen', 2, 2)",
            "INSERT INTO TAGS (NAME, CONTEXT_ID, RANK) VALUES ('cardio', 2, 3)",
            "INSERT INTO TAGS (NAME, CONTEXT_ID, RANK) VALUES ('sport', 2, 4)",
            "INSERT INTO TAGS (NAME, CONTEXT_ID, RANK) VALUES ('read', 3, 1)",
            "INSERT INTO TAGS (NAME, CONTEXT_ID, RANK) VALUES ('watch', 3, 2)",
            "INSERT INTO TAGS (NAME, CONTEXT_ID, RANK) VALUES ('game', 3, 3)",
            "INSERT INTO TAGS (NAME, CONTEXT_ID, RANK) VALUES ('outdoor', 3, 4)",
            "INSERT INTO TAGS (NAME, CONTEXT_ID, RANK) VALUES ('sleep', 4, 1)",
            "INSERT INTO TAGS (NAME, CONTEXT_ID, RANK) VALUES ('meditate', 4, 2)"
        ]
        insert_several_records("time_management.db", tags_records)
    
        # Populate the TASKS table
        tasks_records = [
            "INSERT INTO TASKS (NAME, TAG_ID, RANK, WEEKDAYS, DEPENDENCY_ID, START, END, FREQUENCY) VALUES ('Write a thank you list', 1, 1, 'yyyyyyy', NULL, '08:00:00', '20:00:00', 1)",
            "INSERT INTO TASKS (NAME, TAG_ID, RANK, WEEKDAYS, DEPENDENCY_ID, START, END, FREQUENCY) VALUES ('Automate a repetitive computer task', 3, 1, 'yyyyyyy', NULL, '08:00:00', '20:00:00', 1)",
            "INSERT INTO TASKS (NAME, TAG_ID, RANK, WEEKDAYS, DEPENDENCY_ID, START, END, FREQUENCY) VALUES ('Learn a new %programming_language% concept', 3, 2, 'yyyyyyy', NULL, '08:00:00', '20:00:00', 1)",
            "INSERT INTO TASKS (NAME, TAG_ID, RANK, WEEKDAYS, DEPENDENCY_ID, START, END, FREQUENCY) VALUES ('Plan meals for the upcoming week', 4, 1, 'yyyyyyy', NULL, '08:00:00', '20:00:00', 1)",
            "INSERT INTO TASKS (NAME, TAG_ID, RANK, WEEKDAYS, DEPENDENCY_ID, START, END, FREQUENCY) VALUES ('Do a quick %exercise_name% session', 5, 1, 'yyyyyyy', NULL, '08:00:00', '20:00:00', 1.5)",
            "INSERT INTO TASKS (NAME, TAG_ID, RANK, WEEKDAYS, DEPENDENCY_ID, START, END, FREQUENCY) VALUES ('Perform basic %exercise_name%', 6, 1, 'yyyyyyy', 6, '08:00:00', '20:00:00', 1)",
            "INSERT INTO TASKS (NAME, TAG_ID, RANK, WEEKDAYS, DEPENDENCY_ID, START, END, FREQUENCY) VALUES ('Watch %movie_name%', 9, 1, 'yyyyyyy', NULL, '08:00:00', '20:00:00', 1)",
            "INSERT INTO TASKS (NAME, TAG_ID, RANK, WEEKDAYS, DEPENDENCY_ID, START, END, FREQUENCY) VALUES ('Go to sleep', 13, 1, 'yyyyyyy', NULL, '08:00:00', '20:00:00', 1)"
        ]
        insert_several_records("time_management.db", tasks_records)
    
        subtasks_records = [
            # Subtasks for Task 1 ('Write a thank you list')
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (1, 1, 'Choose person', NULL, 5)",
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (1, 2, 'Write message', 'Express gratitude sincerely', 10)",
    
            # Subtasks for Task 2 ('Automate a repetitive computer task')
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (2, 1, 'Identify task', NULL, 10)",
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (2, 2, 'Write script for %programming_language%', 'Research library or framework if needed', 60)",
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (2, 3, 'Test script', NULL, 30)",
    
            # Subtasks for Task 3 ('Learn a new programming concept')
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (3, 1, 'Choose %programming_language% concept', NULL, 10)",
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (3, 2, 'Read %programming_language% documentation', NULL, 30)",
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (3, 3, 'Implement example in %programming_language%', NULL, 45)",
    
            # Subtasks for Task 4 ('Plan meals for the upcoming week')
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (4, 1, 'Choose recipes', NULL, 20)",
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (4, 2, 'Make a grocery list', NULL, 15)",
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (4, 3, 'Schedule cooking times', NULL, 10)",
    
            # Subtasks for Task 5 ('Do a quick workout session')
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (5, 1, 'Prepare for %exercise_name% session', 'Gather equipment or clear space', 10)",
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (5, 2, 'Perform %exercise_name%', NULL, 30)",
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (5, 3, 'Workout', 'Follow exercise routine', 20)",
    
            # Subtasks for Task 6 ('Perform basic push-ups, squats, and lunges')
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (6, 1, 'Warm up', NULL, 5)",
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (6, 2, 'Perform %exercise_name%', 'Keep good form', 20)",
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (6, 3, 'Perform squats', NULL, 10)",
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (6, 4, 'Perform lunges', NULL, 10)",
    
            # Subtasks for Task 7 ('Watch a recommended movie')
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (7, 1, 'Choose %movie_name%', NULL, 5)",
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (7, 2, 'Set up watching space', 'Comfortable seating, snacks', 10)",
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (7, 3, 'Watch %movie_name%', NULL, 120)",
    
            # Subtasks for Task 8 ('Go to sleep')
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (8, 1, 'Prepare room', 'Dim lights, quiet environment', 5)",
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (8, 2, 'Brush teeth', NULL, 5)",
            "INSERT INTO SUBTASKS (TASK_ID, ORDER_SEQUENCE, NAME, DETAILS, DURATION) VALUES (8, 3, 'Lay in bed', NULL, 1)"
        ]
    
        insert_several_records("time_management.db", subtasks_records)
    
        placeholders_records = [
            "INSERT INTO PLACEHOLDERS (TYPE, VALUE) VALUES ('programming_language', 'Python')",
            "INSERT INTO PLACEHOLDERS (TYPE, VALUE) VALUES ('programming_language', 'JavaScript')",
            "INSERT INTO PLACEHOLDERS (TYPE, VALUE) VALUES ('programming_language', 'Java')",
            "INSERT INTO PLACEHOLDERS (TYPE, VALUE) VALUES ('programming_language', 'C++')",
    
            "INSERT INTO PLACEHOLDERS (TYPE, VALUE) VALUES ('movie_name', 'Inception')",
            "INSERT INTO PLACEHOLDERS (TYPE, VALUE) VALUES ('movie_name', 'The Matrix')",
            "INSERT INTO PLACEHOLDERS (TYPE, VALUE) VALUES ('movie_name', 'Interstellar')",
    
            "INSERT INTO PLACEHOLDERS (TYPE, VALUE) VALUES ('exercise_name', 'push ups')",
            "INSERT INTO PLACEHOLDERS (TYPE, VALUE) VALUES ('exercise_name', 'sit ups')",
            "INSERT INTO PLACEHOLDERS (TYPE, VALUE) VALUES ('exercise_name', 'squats')",
            "INSERT INTO PLACEHOLDERS (TYPE, VALUE) VALUES ('exercise_name', 'jumping jacks')"
        ]
        insert_several_records("time_management.db", placeholders_records)

    create_tables()
    populate_tables()
    
create_example_database()

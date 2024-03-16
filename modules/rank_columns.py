import sqlite3
import functools
import re

def ask_user_cmp(item1, item2):
    while True:
        print(f" [ 1 ] [{item1}] ?")
        print(f" [ 2 ] [{item2}] ?")
        cmp = input(" --> ? ")
        if cmp == "1":
            return -1  # Note: Returning -1 for item1 < item2 to sort in descending order initially
        if cmp == "2":
            return 1
        print("1 or 2, please!")

def fetch_records_for_ranking(database_path, table_name, parent_column=None, rank_column='RANK'):
    my_connection = sqlite3.connect(database_path)
    my_cursor = my_connection.cursor()
    if parent_column:
        query = f"""
            SELECT ID, {parent_column}, NAME FROM {table_name}
            WHERE {rank_column} IS NULL
            ORDER BY {parent_column} ASC
        """
    else:
        query = f"""
            SELECT ID, NAME FROM {table_name}
            WHERE {rank_column} IS NULL
            ORDER BY ID ASC
        """
    my_cursor.execute(query)
    records = my_cursor.fetchall()
    my_connection.close()
    return records

def sort_and_update(database_path, table_name, parent_column=None, rank_column='RANK'):
    records_to_rank = fetch_records_for_ranking(database_path, table_name, parent_column, rank_column)
    grouped_records = {}
    for record in records_to_rank:
        if parent_column:
            parent_id, name = record[1], record[2]
        else:
            parent_id, name = 'default', record[1]
        if parent_id not in grouped_records:
            grouped_records[parent_id] = []
        grouped_records[parent_id].append((record[0], name))

    ask_user_key = functools.cmp_to_key(ask_user_cmp)

    print(f"Sorting for table: {table_name}")
    for group, records in grouped_records.items():
        print(f"Sorting group: {group}")
        # Sorting based on user input comparison; ensure reverse is False to sort ascending based on ranks
        records.sort(key=functools.cmp_to_key(lambda x, y: ask_user_cmp(x[1], y[1])), reverse=False)
        for rank, (record_id, _) in enumerate(records, start=1):
            update_rank(database_path, table_name, record_id, rank, rank_column)



def check_minimum_tasks(database_path):
    my_connection = sqlite3.connect(database_path)
    my_cursor = my_connection.cursor()
    my_cursor.execute("""
        SELECT P.ID, COUNT(T.ID)
        FROM PLACES P
        JOIN CONTEXTS C ON P.ID = C.PLACE_ID
        JOIN TAGS TG ON C.ID = TG.CONTEXT_ID
        JOIN TASKS T ON TG.ID = T.TAG_ID
        GROUP BY P.ID
    """)
    task_counts = my_cursor.fetchall()
    my_connection.close()
    for place_id, count in task_counts:
        if count < 5:
            raise ValueError(f"Place ID {place_id} has only {count} tasks, which is less than the required minimum of 5.")

def extract_placeholders(text):
    # Regular expression to find placeholders in the format %placeholder%
    pattern = re.compile(r"%(\w+)%")
    return pattern.findall(text)

def check_placeholders(database_path):
    my_connection = sqlite3.connect(database_path)
    my_cursor = my_connection.cursor()

    # Retrieve all names from TASKS and STEPS
    my_cursor.execute("SELECT NAME FROM TASKS UNION SELECT NAME FROM STEPS")
    names = my_cursor.fetchall()

    # Extract and collect all placeholders
    placeholders = set()
    for (name,) in names:
        placeholders.update(extract_placeholders(name))

    # Check each placeholder in the PLACEHOLDERS table
    for placeholder in placeholders:
        my_cursor.execute("SELECT COUNT(*) FROM PLACEHOLDERS WHERE TYPE = ?", (placeholder,))
        count = my_cursor.fetchone()[0]
        if count == 0:
            raise ValueError(f"No values found for placeholder: {placeholder}")

    my_connection.close()



def update_rank(database_path, table_name, record_id, new_rank, rank_column='RANK'):
    my_connection = sqlite3.connect(database_path)
    my_cursor = my_connection.cursor()
    my_cursor.execute(f"UPDATE {table_name} SET {rank_column} = {new_rank} WHERE ID = {record_id}")
    my_connection.commit()
    my_connection.close()

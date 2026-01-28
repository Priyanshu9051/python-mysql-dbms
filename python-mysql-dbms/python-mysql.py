import mysql.connector as sql

con = sql.connect(host="localhost", user="root", password="")  # Enter your password
cursor = con.cursor()


def create_database():
    try:
        database = input("enter the database name to create database: ")
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database} ")
        print("Database created successfully ")
    except Exception as e:
        print("enter the valid name ")


def delete_database():
    database = input("enter the database name to delete database: ")
    cursor.execute(f"DROP DATABASE {database} ")


def create_table():
    database = input("enter the database to create table: ")
    cursor.execute(f"USE {database} ")
    query_table = input("enter the query to create table : ")
    cursor.execute(query_table)
    insert_values = "enter the insert query in table : "
    cursor.execute(insert_values)


def delete_table():
    database = input("enter the database to create table: ")
    cursor.execute(f"USE {database} ")
    table_name = input("enter the table name to delete table : ")
    cursor.execute(f"DROP TABLE {table_name}")


def show_tables():
    database = input("enter the database to show tables: ")
    cursor.execute(f"USE {database} ")
    # table_name=input("enter the table name to show : ")
    cursor.execute(f"SHOW TABLES")
    all_column = cursor.fetchall()
    for column in all_column:
        print(column)


def show_tables_values():
    database = input("enter the database to show tables: ")
    cursor.execute(f"USE {database} ")
    table_name = input("enter the table name to show : ")
    cursor.execute(f"SHOW COLUMNS FROM {table_name}")
    all_column = cursor.fetchall()
    for column in all_column:
        print(column[0], end="    ")
    print("\n")
    cursor.execute(f"SELECT*FROM {table_name}")
    all_values = cursor.fetchall()
    for value in all_values:
        print(value)


def update_table():
    def take_db_tb():
        database = input("enter the database  ")
        cursor.execute(f"USE {database} ")
        table_name = input("enter the table name  : ")
        return table_name

    print(
        """1 for Add new Column
2 for Change the datatype of existing column
3 for Rename a Column
4 for Delete a Column
5 for Rename a Table
6 for Add primary key"""
    )
    try:

        n = int(input("enter the choice : "))
        if n == 1:
            table_name = take_db_tb()
            new_column = input("enter the name of the new column with datatype : ")
            cursor.execute(f"ALTER TABLE {table_name} ADD ({new_column}) ")
        elif n == 2:
            table_name = take_db_tb()
            column_name = input("enter the datatype to change  : ")
            datatype = input("enter the datatype to change : ")
            cursor.execute(f"ALTER TABLE {table_name} MODIFY {column_name} {datatype} ")
        elif n == 3:
            table_name = take_db_tb()
            column_name = input("enter the datatype to change the column name  : ")
            rename_column = input("enter the column name with datatype to rename : ")
            cursor.execute(
                f"ALTER TABLE {table_name} CHANGE {column_name} {rename_column} "
            )
        elif n == 4:
            table_name = take_db_tb()
            delete_column = input("enter the name of the column to delete : ")
            cursor.execute(f"ALTER TABLE {table_name} DROP {delete_column}")
        elif n == 5:
            table_name = take_db_tb()
            rename_table = input("enter the name to rename the table : ")
            cursor.execute(f"ALTER TABLE {table_name} RENAME TO {rename_table} ")
        elif n == 6:
            table_name = take_db_tb()
            column_name = input("enter the name to rename the table : ")
            cursor.execute(f"ALTER TABLE {table_name} ADD PRIMARY KEY ({column_name})")
        else:
            print("Invalid choice select again")
    except ValueError:
        print("Invalid input! Please enter a number only")


def update_values():
    database = input("enter the database to show tables: ")
    cursor.execute(f"USE {database} ")
    table_name = input("enter the table name to insert the new row : ")
    set_value = input("enter the vale to update :  ")
    where = input("enter where do you want to change the value: ")
    cursor.execute(f"UPDATE {table_name} SET {set_value} WHERE {where}")


def aggregate_fun():
    print(
        """1 for COUNT
2 for SUM
3 for AVG
4 for MIN
5 for MAX
"""
    )

    def take_db_tb():
        database = input("enter the database to use aggregate function : ")
        cursor.execute(f"USE {database} ")
        table_name = input("enter the table name to use aggregate function : ")
        return table_name

    try:
        n = int(input("enter the choice: "))
        if n == 1:
            table_name = take_db_tb()
            col = input("enter the name of the coloumn to count  :  ")
            cursor.execute(f"SELECT COUNT{col} FROM {table_name} ")
        elif n == 2:
            table_name = take_db_tb()
            col = input("enter the name of the coloumn to sum  :  ")
            cursor.execute(f"SELECT SUM{col} FROM {table_name} ")
        elif n == 3:
            table_name = take_db_tb()
            avg = input("enter the name of the coloumn to find average :  ")
            cursor.execute(f"SELECT AVG{avg} FROM {table_name} ")
        elif n == 4:
            table_name = take_db_tb()
            Min = input("enter the name of the coloumn to find minimum   :  ")
            cursor.execute(f"SELECT MIN{Min} FROM {table_name} ")
        elif n == 5:
            table_name = take_db_tb()
            Max = input("enter the name of the coloumn to find maximum   :  ")
            cursor.execute(f"SELECT MAX{Max} FROM {table_name} ")
        else:
            print("invalid choice select again")

    except ValueError:
        print("Invalid input! Please enter a number only")


print(
    """1 for Create database 
2 for Delete database
3 for Create table
4 for Delete table
5 for Show tables
6 for Show table column + values 
7 for Update table
8 for Update values
9 for Use aggregate funtion"""
)
try:
    n = int(input("enter the choice : "))
    if n == 1:
        create_database()
    elif n == 2:
        delete_database()
    elif n == 3:
        create_table()
    elif n == 4:
        delete_table()
    elif n == 5:
        show_tables()
    elif n == 6:
        show_tables_values()
    elif n == 7:
        update_table()
    elif n == 8:
        update_values()
    elif n == 9:
        aggregate_fun()
    else:
        print("invalid choice select again")
except ValueError:
    print("Invalid input! Please enter a number only")
con.close()

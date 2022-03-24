import mysql.connector
from mysql.connector import Error

def create_db_connection(host_name, user_name, user_password,db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as err:
        print(f"Error: '{err}'")

def execute_get_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        return records
    except Error as err:
        print(f"Error: '{err}'")
   
connection = create_db_connection("localhost", "root", "residentz","tenantpayments")

queryShowTables = "SHOW TABLES"

a = execute_get_query(connection,queryShowTables)

results_list = [item[0] for item in a]

table = "payments"

if table not in results_list:
    queryCreate = "CREATE TABLE payments (flatid INT AUTO_INCREMENT PRIMARY KEY, tenantname VARCHAR(255), tenantsurname VARCHAR(255), currentpayment FLOAT(7,2), previouspayment FLOAT(7,2), discount VARCHAR(255))"
    b = execute_query(connection, queryCreate)
    queryInsert = """
        INSERT INTO payments
        (payments.tenantname,payments.tenantsurname,payments.currentpayment,payments.previouspayment,payments.discount)
        VALUES('Jason','Momoa','8000.00','8000.00','Yes')
        ;
        """
    x = execute_query(connection, queryInsert)
    queryInsert = """
        INSERT INTO payments
        (payments.tenantname,payments.tenantsurname,payments.currentpayment,payments.previouspayment,payments.discount)
        VALUES('Brent','Affleck','0.00','8000.00','No')
        ;
        """
    x = execute_query(connection, queryInsert)
    queryInsert = """
        INSERT INTO payments
        (payments.tenantname,payments.tenantsurname,payments.currentpayment,payments.previouspayment,payments.discount)
        VALUES('Jenna','Garner','8000.00','0.00','No')
        ;
        """
    x = execute_query(connection, queryInsert)
    queryInsert = """
        INSERT INTO payments
        (payments.tenantname,payments.tenantsurname,payments.currentpayment,payments.previouspayment,payments.discount)
        VALUES('Peters','Davids','0.00','0.00','No')
        ;
        """
    x = execute_query(connection, queryInsert)
    queryInsert = """
        INSERT INTO payments
        (payments.tenantname,payments.tenantsurname,payments.currentpayment,payments.previouspayment,payments.discount)
        VALUES('Nikita','Minaj','8000.00','8000.00','Yes')
        ;
        """
    x = execute_query(connection, queryInsert)
    queryInsert = """
        INSERT INTO payments
        (payments.tenantname,payments.tenantsurname,payments.currentpayment,payments.previouspayment,payments.discount)
        VALUES('Taylor-Lautner','Swift','8000.00','0.00','No')
        ;
        """
    x = execute_query(connection, queryInsert)
    queryInsert = """
        INSERT INTO payments
        (payments.tenantname,payments.tenantsurname,payments.currentpayment,payments.previouspayment,payments.discount)
        VALUES('Selena-Kyle','Gomez','0.00','0.00','No')
        ;
        """
    x = execute_query(connection, queryInsert)
    queryInsert = """
        INSERT INTO payments
        (payments.tenantname,payments.tenantsurname,payments.currentpayment,payments.previouspayment,payments.discount)
        VALUES('Thierry-Henry','Cavill','8000.00','8000.00','Yes')
        ;
        """
    x = execute_query(connection, queryInsert)
    queryInsert = """
        INSERT INTO payments
        (payments.tenantname,payments.tenantsurname,payments.currentpayment,payments.previouspayment,payments.discount)
        VALUES('Carole','Basculin','0.00','0.00','No')
        ;
        """
    x = execute_query(connection, queryInsert)
    queryInsert = """
        INSERT INTO payments
        (payments.tenantname,payments.tenantsurname,payments.currentpayment,payments.previouspayment,payments.discount)
        VALUES('Liu-Kang','Sang-Tsung','8000.00','0.00','No')
        ;
        """
    x = execute_query(connection, queryInsert)

query2 = """
        SELECT payments.tenantname, payments.tenantsurname, payments.flatid, payments.currentpayment 
        FROM payments
        WHERE payments.currentpayment = 0
        """
y = execute_get_query(connection, query2)

print(y)

query2 = """
        SELECT payments.tenantname, payments.tenantsurname, payments.flatid, payments.previouspayment 
        FROM payments
        WHERE payments.previouspayment = 0
        """
y = execute_get_query(connection, query2)

print(y)

query2 = """
        SELECT payments.tenantname, payments.tenantsurname, payments.flatid, payments.discount 
        FROM payments
        WHERE payments.discount = 'Yes'
        """
y = execute_get_query(connection, query2)

print(y)

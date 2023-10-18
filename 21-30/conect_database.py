import pyodbc

SERVER = 'localhost'
DATABASE = '***'
USERNAME = '***'
PASSWORD = '****'

connectionString = f'DRIVER={{MySQL ODBC 8.1 ANSI Driver}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString)

cursor = conn.cursor()

ClientID = int(input('ID: '))
clientName = input('Client Name: ')
Address = input('Addres: ')
Email = input('Email: ')
PhoneNumber = input('Phone Number: ')

insert_cmd = f"""
    INSERT INTO clients (ClientID, clientName, Address, Email, PhoneNumber)
   VALUES({ClientID}, '{clientName}', '{Address}', '{Email}', {PhoneNumber})
"""

select_cms = """
    SELECT * FROM Clients
"""

cursor.execute(insert_cmd)
cursor.commit()

result = cursor.execute(select_cms)

for i in result:
    print(f'{i.ClientID}: {i.ClientName}')
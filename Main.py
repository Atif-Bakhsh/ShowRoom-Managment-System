
import mysql.connector as mysql


host = "localhost"
user = "admin"
password = "admin"


def database():
  try:
    db = mysql.connect(host=host, user=user, password=password)
    print("Connected successfully to the database!")
  except Exception as e:
    print(e)
    print("Failed to connect to the database!")


def welcome():
  print(" - WELCOME TO BAKHSH SHOWROOM - ")


def accessibility():
  use = int(input("Enter your ID:"))
  passwor = int(input("Enter you password:"))
  if use == 2 and passwor == 1234 or use == 1 and passwor == 1234:
    print("Welcome to the portal!")
  else:
    print("Enter the correct password!")


 # Displaying all records from a selected table
def inventory():
  db1 = mysql.connect(host=host, user=user, password=password, database="cars")
  command_handler = db1.cursor()
  command_handler.execute("SELECT * from Inventory")
  records = command_handler.fetchall()
  print("Displaying records")
  for record in records:
    print(record)


def adding():
  # Adding cars to the inventory
  db1 = mysql.connect(host=host, user=user, password=password, database="cars")
  command_handler = db1.cursor()
  query = "INSERT INTO Inventory(name,engine_size,no_seats,price) VALUES (%s,%s,%s,%s)"
  query_vals = (
  input("Enter the name of the car:"), input("Enter the engine size:"), input("Enter the number of seats:"),
  eval(input("Enter the price of the car:")))
  command_handler.execute(query, query_vals)
  db1.commit()
  print(command_handler.rowcount, "record inserted")


def selling():
  # Deleting records
  db1 = mysql.connect(host=host, user=user, password=password, database="cars")
  command_handler = db1.cursor()
  print("Deleting records from a table")
  name = input("Enter the car's name:")
  command_handler.execute("DELETE FROM Inventory WHERE name ='" + name + "'")
  db.commit()
  print(command_handler.rowcount, "Record(s) deleted")


def clear():
  for _ in range(65):
     print()




def main():
  database()
  welcome()
  accessibility()

  while True:
    print(' B A K H S H   S H O W R O O M ')
    print('*'*120)
    print("\n1.   Display the ShowRoom inventory")
    print('\n2.   Add a car to the ShowRoom inventory')
    print('\n3.   Sell a car from the ShowRoom inventory')
    print('\n4.  Log Out')
    print('\n\n')
    choice = int(input('Enter your choice ...: '))
    if choice == 1:
      inventory()
    if choice == 2:
      adding()
    if choice == 3:
      selling()
    if choice == 4:
        break


if __name__ == "__main__":
    main()


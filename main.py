import re
import os
import time

#name, number, email, password

#CRUDS
'''
C: Create
R: Read
U: Update
D: Delete
S: Save
'''

REGEX_CHECK_EMAIL = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

user:dict = {
  "id": 0,
  "name": "",
  "number": "",
  "email": "",
  "password": ""
}

def resetUser() -> None:
  global user
  user = {
    "id": 0,
    "name": "",
    "number": "",
    "email": "",
    "password": ""
  }

def getUser():
  name = input("Enter your name: ")
  id = input("Enter your ID: ")

  if not re.fullmatch("[a-zA-Z]+", name):
    while not re.fullmatch("[a-zA-Z]+", name):
      name = input("Enter your name: ")

  yield name

  if not re.fullmatch("[0-9]+", id):
    while not re.fullmatch("[0-9]+", id):
      id = input("Enter your ID: ")

  id = int(id)
    
  yield id

def readUser(name:str, id:int) -> None:
  
  file = ''
  
  try:
    file = open(f"{name}-{id}.txt")
  except:
    print("\n\n\n~~~Wrong user ID or Name~~~\n\n\n")
    return

  print('\n')

  print(file.read(), '\n')
  
def checkInputs() -> bool:
  global user, regexCheckEmail
  
  if not re.fullmatch("[a-zA-Z]+", user['name']):
    while not re.fullmatch("[a-zA-Z]+", user['name']):
      user["name"] = input("Enter your name: ")
      
  if not re.fullmatch("[0-9]+", user["number"]):
    while not re.fullmatch("[0-9]+", user["number"]):
      user["number"] = input("Enter your phone number: ")
  else:
    user["number"] = int(user["number"])

  if not re.fullmatch(REGEX_CHECK_EMAIL, user["email"]):
    while not re.fullmatch(REGEX_CHECK_EMAIL, user["email"]):
      user["email"] = input("Enter your email: ")

  if not re.fullmatch("[a-zA-Z0-9]{8,}", user["password"]):
    while not re.fullmatch("[a-zA-Z0-9]{8,}", user["password"]):
      user["password"] = input("Enter your password: ")
    

def createUser() -> None:
  global user
  user["id"] = int(time.time())
  user["name"] = input("Enter your name: ")
  user["number"] = input("Enter your phone number: ")
  user["email"] = input("Enter your email: ")
  user["password"] = input("Enter your password: ")

  checkInputs()

  file = ''
  
  try:
    file = open(f"{user['name']}-{user['id']}.txt")

    print("user already exists")
    return
  except:
    file = open(f"{user['name']}-{user['id']}.txt", 'w')

    file.write(f"""id: {user['id']}
name: {user['name']}
number: {user['number']}
email: {user['email']}
password: {user['password']}""")
    
    file.close()
  
  readUser(user['name'], user['id'])
  resetUser()
  

def updateUser(name:str, id:int) -> None:
  global user

  file = ''

  try:
    file = open(f"{name}-{id}.txt")
  except :
    print("\n\n\n~~~Wrong user ID or Name~~~\n\n\n")
    return

  file = file.read()
  
  file = file.split(": ")

  #print(file)
  fileCopy = file
  file = []
  
  for i in fileCopy:
    file.extend(i.split("\n"))
  
  #print(file)

  print(f"""id: {file[1]}
name: {file[3]}
number: {file[5]}
email: {file[7]}
password: {file[9]}""")

  global user
  user['id'] = file[1]
  user["name"] = input("Enter your name: ")
  user["number"] = input("Enter your phone number: ")
  user["email"] = input("Enter your email: ")
  user["password"] = input("Enter your password: ")

  checkInputs()

  updateFile = ''

  try:
    updateFile = open(f"{file[3]}-{file[1]}.txt", 'w')
  except:
    pass

  updateFile.write(f"""id: {user['id']}
name: {user['name']}
number: {user['number']}
email: {user['email']}
password: {user['password']}""")
    
  updateFile.close()

  os.rename(f"./{file[3]}-{file[1]}.txt", f"./{user['name']}-{file[1]}.txt")
  
def deleteUser(name: str, id: int) -> None:
  try:
    file = f"{name}-{id}.txt"

    if os.path.exists(file):
      os.remove(f"./{file}")

      print("User Deleted")

    else:
      print("\n\n\n~~~Wrong user ID or Name~~~\n\n\n")
  except:
    print("\n\n\n~~~Wrong user ID or Name~~~\n\n\n")
    return
  
def checkChoice(choice:int) -> None:
  if choice == 1:
    createUser()
  elif choice == 2:
    getUserInfo = getUser()
    readUser(next(getUserInfo), next(getUserInfo))
  elif choice == 3:
    getUserInfo = getUser()
    updateUser(next(getUserInfo), next(getUserInfo))
  elif choice == 4:
    getUserInfo = getUser()
    deleteUser(next(getUserInfo), next(getUserInfo))

def main():
  while True:
    print("1.Create")
    print("2.Read")
    print("3.Update")
    print("4.Delete")
    choice = input("Enter a choice: ")

    if not re.fullmatch('\d', choice):
      while not re.fullmatch('\d', choice):
        choice = input("Enter a choice: ")
    
    choice = int(choice)
    checkChoice(choice)  

      
if __name__ == "__main__":
  main()
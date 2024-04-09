nameList = []
def printList():
  print()
  for i in nameList:
    print(i)
  print()

while True:
  firstName = input("First Name: ").strip().capitalize()
  lastName = input("Last Name: ").strip().capitalize()
  fullName = f"{firstName} {lastName}"
  if fullName not in nameList:
    nameList.append(fullName)
  else:
    print("ERROR: Duplicate name")
  printList()



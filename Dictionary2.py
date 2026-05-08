# how does a dictionary store our data?
# Answer: it has to store our data in KEY : VALUE pairs

# items() returns ALL key-value pairs in a dictionary


users = {}
users["A_Person"] = ["1234", 1000, ["B_Person", "C_Person"]]
users["Jaden123"] = ["admin", 5000, ["Ethan456", "Jane789"]]
users["EICC_EROS"] = ["0000", 10000000, ["AAA", "BBB"]]


def PrintDictionary(anyDict):
    for key, value in anyDict.items():
        print(f"{key} : {value}")


# how do we retrieve a user's account details (password and Robux amount)?
def AccountDetails():
    username = input("Enter the username: ")
    print("Password:", users[username][0])
    print("Robux:", users[username][1])


# how do we edit account details
def EditDetails():
    username = input("Whose account details would you like to amend: ")
    details = input("Password(1) or Robux(2): ")
    if details == "1":
        # edit password
        newPassword = input("Enter new password: ")
        users[username][0] = newPassword
        print("password has been successfully updated")

    elif details == "2":
        # edit Robux
        newAmount = int(input("Enter new amount: "))
        users[username][1] = newAmount
        print("Robux amount has been successfully updated")


def AddFriends():
    username = input("Enter username: ")
    friendName = input("Provide a new friend's name: ")
    if friendName in users[username][2]:
        print("Already a friend")
    else:
        users[username][2].append(friendName)
        print(f"updated friend's list: {users[username][2]}")




PrintDictionary(users)
AddFriends()
PrintDictionary(users)




































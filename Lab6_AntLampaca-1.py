"""
Program Name: Lab6_AntLampaca-1.py
Author: Antoni Labsz
Purpose: Simple Login page
Starter Code: None
Date: February 22, 2026
"""

users = {
    "Toni": "s3cr3t",
    "admin": "admin1234",
    "user": "user1234",
    "guest": "guest"
}

#ask for username

username = input("Enter username: ")

#Checks if username exists

if username not in users:
    print("User not found. Exiting")
else:
    attempts = 0
    max_attempts = 3

    #limits number of attempts

    while attempts < max_attempts:
        password = input("Ente password: ")

        if password == users[username]:

            #Assigned security level

            if username == "guest":
                security_level = "Guest access"
            else:
                security_level = "Security level 1"
            
            print(f"\nWelcome, {username}. You have {security_level}.")
            break
        else:
            attempts += 1
            if attempts < max_attempts:
                print("Access Denied. try again")
            else:
                print("\nToo many failed attempts. Account locked.")
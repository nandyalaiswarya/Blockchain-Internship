import hashlib

class DigitalIdentity:

    def __init__(self):
        self.users = {}

    def create_identity(self, user_id, name, password):
        if user_id in self.users:
            print("User Already Exists!")
            return

        password_hash = hashlib.sha256(
            password.encode()
        ).hexdigest()

        self.users[user_id] = {
            "name": name,
            "password": password_hash
        }

        print("Digital Identity Created Successfully!")

    def verify_identity(self, user_id, password):
        if user_id not in self.users:
            print("Identity Not Found!")
            return

        entered_hash = hashlib.sha256(
            password.encode()
        ).hexdigest()

        stored_hash = self.users[user_id]["password"]

        if entered_hash == stored_hash:
            print("Identity Verified Successfully!")
            print("Welcome:", self.users[user_id]["name"])
        else:
            print("Invalid Password!")

    def display_users(self):
        print("\nRegistered Digital Identities:")

        for user_id, details in self.users.items():
            print("User ID:", user_id)
            print("Name:", details["name"])


system = DigitalIdentity()

while True:
    print("\n--- DIGITAL IDENTITY MANAGEMENT ---")
    print("1. Create Identity")
    print("2. Verify Identity")
    print("3. Display Users")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        user_id = input("Enter User ID: ")
        name = input("Enter Name: ")
        password = input("Create Password: ")

        system.create_identity(user_id, name, password)

    elif choice == "2":
        user_id = input("Enter User ID: ")
        password = input("Enter Password: ")

        system.verify_identity(user_id, password)

    elif choice == "3":
        system.display_users()

    elif choice == "4":
        break

    else:
        print("Invalid Choice!")

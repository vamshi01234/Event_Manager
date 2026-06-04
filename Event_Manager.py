people = []

while True:

    print("\n--- Personal Memory Manager ---")
    print("1. Add Person")
    print("2. View People")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        name = input("Enter person's name: ")

        person = {
            "name": name,
            "events": [],
            "details": {}
        }

        people.append(person)

        print("Person added!")

    elif choice == "2":

        if len(people) == 0:
            print("No people found.")

        for person in people:
            print("\nName:", person["name"])

    elif choice == "3":
        break

    else:
        print("Invalid option.")
        

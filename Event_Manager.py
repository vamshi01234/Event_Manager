people = []

while True:

    print("\n--- Personal Memory Manager ---")
    print("1. Add Person")
    print("2. View People")
    print("3. Add Event")
    print("4. Exit")

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

        name = input("Enter person's name: ")

        found = False

        for person in people:

            if person["name"] == name:

                found = True

                print("Person found!")

                event_type = input("Enter event type (Birthday, Anniversary, etc): ")
                event_date = input("Enter event date (MM-DD): ")

                event = {
                    "type": event_type,
                    "date": event_date
                }

                person["events"].append(event)

                print("Event added!")
    
                break

        if not found:
            print("Person not found ❌")
    elif choice == "4":
        break

    else:
        print("Invalid option.")
        

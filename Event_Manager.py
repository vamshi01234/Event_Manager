

import json

try:
    with open("people.json", "r") as file:
        people = json.load(file)
except FileNotFoundError:
    people = []


while True:

    print("\n--- Personal Memory Manager ---")
    print("1. Add Person")
    print("2. View People")
    print("3. Add Event")
    print("4. View Events")
    print("5. Add Detail")
    print("6. View Detail")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
#Add Person
        name = input("Enter person's name: ")

        person = {
            "name": name,
            "events": [],
            "details": {
                    
                }
        }

        people.append(person)

        print("Person added!")

    elif choice == "2":
#View People
        if len(people) == 0:
            print("No people found.")

        for person in people:
            print("\nName:", person["name"])

    elif choice == "3":
#Add Event
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
#View Events
        name = input("Enter person's name: ")

        found = False

        for person in people:

            if person["name"] == name:

                found = True

                if len(person["events"]) == 0:
                    print("No events found.")

                else:
                    print("\nEvents:")

                    for event in person["events"]:

                        print(event["type"], "-", event["date"])

                break

        if not found:
            print("Person not found ❌")


    elif choice == "5":
#Add Detail
        name = input("Enter person's name: ")

        found = False

        for person in people:

            if person["name"] == name:

                found = True

                detail_name = input("Enter Detail Name (e.g., Shoe Size, Favorite Food): ")
                detail_value = input("Enter Value (e.g., 10, Biryani): ")

                person["details"][detail_name] = detail_value

                print("Detail added!")

                break

        if not found:
            print("Person not found ❌")

    elif choice == "6":
#View Detail
        name = input("Enter person's name: ")

        found = False

        for person in people:

            if person["name"] == name:

                found = True

                if len(person["details"]) == 0:
                    print("No details found.")

                else:

                    print("\nDetails:")

                    for detail_name, detail_value in person["details"].items():

                        print(detail_name, ":", detail_value)
    
                break

        if not found:
            print("Person not found ❌")    

#Exit
    elif choice == "7":

        with open("people.json", "w") as file:
            
            json.dump(people, file, indent=4)

        print("Data saved!")

        break
 

    else:
        print("Invalid option.")
        

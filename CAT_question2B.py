rooms = {
    "A": "Dirty",
    "B": "Dirty"
}
location = "A"

def vacuum_agent(location):
    global rooms

    while True:
        if rooms[location] == "Dirty":
            print("Cleaning Room", location)
            rooms[location] = "Clean"

        if location == "A":
            location = "B"

        else:
            location = "A"

        if rooms["A"] == "Clean" and rooms["B"] == "Clean":
            print("All rooms are clean")
            break

vacuum_agent(location)

print(rooms)
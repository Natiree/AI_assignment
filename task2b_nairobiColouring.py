from constraint import Problem

problem = Problem()

subcounties = [
    "Westlands",
    "Dagoretti North",
    "Dagoretti South",
    "Langata",
    "Kibra",
    "Roysambu",
    "Kasarani",
    "Ruaraka",
    "Embakasi South",
    "Embakasi North",
    "Embakasi Central",
    "Embakasi East",
    "Embakasi West",
    "Makadara",
    "Kamukunji",
    "Starehe",
    "Mathare"
]

colors = ["Red", "Green", "Blue"]

for area in subcounties:
    problem.addVariable(area, colors)


adjacent = [
    ("Westlands", "Dagoretti North"),
    ("Westlands", "Starehe"),
    ("Dagoretti North", "Dagoretti South"),
    ("Dagoretti South", "Langata"),
    ("Langata", "Kibra"),
    ("Kibra", "Starehe"),
    ("Roysambu", "Kasarani"),
    ("Kasarani", "Ruaraka"),
    ("Ruaraka", "Mathare"),
    ("Mathare", "Starehe"),
    ("Starehe", "Kamukunji"),
    ("Kamukunji", "Makadara"),
    ("Makadara", "Embakasi West"),
    ("Embakasi West", "Embakasi Central"),
    ("Embakasi Central", "Embakasi East"),
    ("Embakasi East", "Embakasi North"),
    ("Embakasi North", "Embakasi South"),
    ("Embakasi South", "Langata"),
    ("Embakasi West", "Langata"),
    ("Ruaraka", "Embakasi North")
]

for area1, area2 in adjacent:
    problem.addConstraint(
        lambda a, b: a != b,
        (area1, area2)
    )

solution = problem.getSolution()

print("Nairobi Sub-County Map Coloring")
print("--------------------------------")

for area in solution:
    print(area, ":", solution[area])

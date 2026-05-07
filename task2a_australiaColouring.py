from constraint import Problem

problem = Problem()

# Regions
regions = ["WA", "NT", "SA", "Q", "NSW"]

# Colors
colors = ["Red", "Green", "Blue"]

# Add variables
for region in regions:
    problem.addVariable(region, colors)

# Constraints
problem.addConstraint(lambda a, b: a != b, ("WA", "NT"))
problem.addConstraint(lambda a, b: a != b, ("WA", "SA"))
problem.addConstraint(lambda a, b: a != b, ("NT", "SA"))
problem.addConstraint(lambda a, b: a != b, ("NT", "Q"))
problem.addConstraint(lambda a, b: a != b, ("SA", "Q"))
problem.addConstraint(lambda a, b: a != b, ("SA", "NSW"))
problem.addConstraint(lambda a, b: a != b, ("Q", "NSW"))

# Get solution
solution = problem.getSolution()

print("Australia Map Coloring:")
print(solution)
from constraint import Problem

problem = Problem()

regions = ["WA", "NT", "SA", "Q", "NSW"]

colors = ["Red", "Green", "Blue"]

for region in regions:
    problem.addVariable(region, colors)

problem.addConstraint(lambda a, b: a != b, ("WA", "NT"))
problem.addConstraint(lambda a, b: a != b, ("WA", "SA"))
problem.addConstraint(lambda a, b: a != b, ("NT", "SA"))
problem.addConstraint(lambda a, b: a != b, ("NT", "Q"))
problem.addConstraint(lambda a, b: a != b, ("SA", "Q"))
problem.addConstraint(lambda a, b: a != b, ("SA", "NSW"))
problem.addConstraint(lambda a, b: a != b, ("Q", "NSW"))

solution = problem.getSolution()

print("Australia Map Coloring:")
print(solution)

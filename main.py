from optimizers import genetic_algorithm, gradient_descent

points = [
    (0, 20),
    (2, 16),
    (6, 14),
    (4, 10),
    (10, 10),
    (10, 4)
]

solution_range = (-100, 100)

gradient_linear_regression = gradient_descent(
    points,
    random_range=solution_range
)

print(str(gradient_linear_regression))

genetic_linear_regression = genetic_algorithm(
    points,
    population=1000,
    mutation_rate=0.15,
    generations=2000,
    random_range=solution_range
)

print(str(genetic_linear_regression))
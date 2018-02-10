from line import Line, Number, random_line
import random
from typing import List, Tuple


def decision(probability: Number) -> bool:
    """Return a random decision based on a given probability"""
    return random.random() < probability


def mse(line: Line, points: List[Tuple[Number, Number]]) -> Number:
    """
    Calculates the mean squared errors (MSE) of a Line object
    from a given list of points.
    """
    return sum([(y - line(x)) ** 2 for x, y in points]) / len(points)


def mse_gradient(line: Line, points: List[Tuple[Number, Number]]) -> Tuple[Number]:
    """
    Calculates the mean squared error (MSE) gradient from a given Line object
    and a given list of points.
    """

    '''
    a_gradient and b_gradient are the partial derivatives of the SSE function
    with respect to a and to b.
    '''
    a_gradient = round(sum([2 * x * (line(x) - y) for x, y in points]) / len(points), 3)
    b_gradient = round(sum([2 * (line(x) - y) for x, y in points]) / len(points), 3)

    return a_gradient, b_gradient


def genetic_algorithm(
        training_data: List[Tuple[Number, Number]],
        population: int = 100,
        mutation_rate: Number = 0.01,
        selection_rate: Number = 0.1,
        generations: int = 200,
        random_range=(-100, 100)
        ) -> Line:

    selected_population_size = round(population * selection_rate)

    # Initialize by generating a population of random lines.
    lines_population = [random_line(random_range) for _ in range(population)]

    for generation in range(1, generations+1):

        lines_error = [mse(line, training_data) for line in lines_population]

        # Selection : "Kill" the lines with the highest error rate.
        while len(lines_population) != selected_population_size:
            worst_line_index = lines_error.index(max(lines_error))
            lines_error.pop(worst_line_index)
            lines_population.pop(worst_line_index)

        if generation < generations:
            # Crossover : two randomly selected "survivor" lines are merged together.
            while len(lines_population) != population:
                mutate = decision(mutation_rate)

                line_a = random.choice(lines_population)

                if mutate: line_b = random_line(random_range)
                else: line_b = random.choice(lines_population)

                lines_population.append(line_a + line_b)

    return lines_population[lines_error.index(min(lines_error))]


def gradient_descent(
        training_data: List[Tuple[Number, Number]],
        step_rate: int = 0.01,
        random_range=(-100, 100)
        ) -> Line:

    line = random_line(random_range)
    line_gradient = mse_gradient(line, training_data)

    # While we have not reached a "valley" (where the error is minimized)...
    while line_gradient != (0, 0):
        a_gradient = line_gradient[0]
        b_gradient = line_gradient[1]

        line.a -= step_rate*a_gradient
        line.b -= step_rate*b_gradient

        line_gradient = mse_gradient(line, training_data)

    return line

import sys
import math
import os
from pathlib import Path
import requests
from traceback import print_exc
import time
from typing import List, Tuple
import threading
import queue
from concurrent.futures import ThreadPoolExecutor, as_completed
import random
import heapq

# Add the parent directory to the Python path
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir))

from icfp.encode import encode_message
from icfp.decode import decode_message

URL = "https://boundvariable.space/communicate"
AUTH_HEADER = {"Authorization": "Bearer f8fb3b34-7f8f-4cb0-bd74-c83be464d0a1"}

BEST_SCORES = {
    1: 5,
    2: 49,
    3: 10,
    4: 99,
    5: 116,
    6: 117,
    7: 94,
    8: 90,
    9: 206,
    10: 304,
    11: 8192,
    12: 8192,
    13: 23791,
    14: 137,
    15: 39,
    16: 1373,
    17: 408,
    18: 1765,
    19: 11279,
    20: 2342,
    21: 2376,
    22: 1136,
    23: 152792,
    24: 498329,
    25: 513862,
}


class SpaceshipPathfinder:
    def __init__(self):
        self.directions = {
            1: (-1, -1),
            2: (0, -1),
            3: (1, -1),
            4: (-1, 0),
            5: (0, 0),
            6: (1, 0),
            7: (-1, 1),
            8: (0, 1),
            9: (1, 1),
        }

    def find_path(self, targets: List[Tuple[int, int]]) -> str:
        first_move = self.find_nearest_point(targets)
        ordered_targets = self.nearest_neighbor_tsp(first_move, targets)
        path = self.generate_path(ordered_targets)
        return path

    def find_nearest_point(self, targets: List[Tuple[int, int]]) -> Tuple[int, int]:
        return min(targets, key=lambda x: max(abs(x[0]), abs(x[1])))

    def nearest_neighbor_tsp(
        self, start: Tuple[int, int], targets: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        unvisited = set(targets)
        path = [start]
        unvisited.remove(start)

        while unvisited:
            current = path[-1]
            next_target = min(
                unvisited, key=lambda x: self.manhattan_distance(current, x)
            )
            path.append(next_target)
            unvisited.remove(next_target)

        return path

    def manhattan_distance(self, p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def generate_path(self, ordered_targets: List[Tuple[int, int]]) -> str:
        path = []
        current_pos = (0, 0)
        vx, vy = 0, 0

        for target in ordered_targets:
            while current_pos != target:
                dx = target[0] - current_pos[0]
                dy = target[1] - current_pos[1]

                move_x = max(min(dx - vx, 1), -1)
                move_y = max(min(dy - vy, 1), -1)

                move = next(
                    key
                    for key, value in self.directions.items()
                    if value == (move_x, move_y)
                )
                path.append(str(move))

                vx += move_x
                vy += move_y
                current_pos = (current_pos[0] + vx, current_pos[1] + vy)

        return "".join(path)


class GeneticAlgorithmPathfinder:
    def __init__(self, population_size=100, generations=1000):
        self.population_size = population_size
        self.generations = generations
        self.directions = {
            1: (-1, -1),
            2: (0, -1),
            3: (1, -1),
            4: (-1, 0),
            5: (0, 0),
            6: (1, 0),
            7: (-1, 1),
            8: (0, 1),
            9: (1, 1),
        }

    def find_path(self, targets: List[Tuple[int, int]]) -> str:
        population = self.initialize_population(targets)

        for _ in range(self.generations):
            fitness_scores = [
                self.calculate_fitness(individual, targets) for individual in population
            ]
            parents = self.selection(population, fitness_scores)
            offspring = self.crossover(parents)
            population = self.mutation(offspring)

        best_individual = min(
            population, key=lambda x: self.calculate_fitness(x, targets)
        )
        return self.generate_path(best_individual)

    def initialize_population(self, targets):
        return [
            random.sample(targets, len(targets)) for _ in range(self.population_size)
        ]

    def calculate_fitness(self, individual, targets):
        total_distance = 0
        current_pos = (0, 0)
        for target in individual:
            total_distance += max(
                abs(target[0] - current_pos[0]), abs(target[1] - current_pos[1])
            )
            current_pos = target
        return total_distance

    def selection(self, population, fitness_scores):
        return random.choices(
            population,
            weights=[1 / score for score in fitness_scores],
            k=len(population),
        )

    def crossover(self, parents):
        offspring = []
        for i in range(0, len(parents), 2):
            parent1, parent2 = parents[i], parents[i + 1]
            crossover_point = random.randint(1, len(parent1) - 1)
            child1 = parent1[:crossover_point] + [
                x for x in parent2 if x not in parent1[:crossover_point]
            ]
            child2 = parent2[:crossover_point] + [
                x for x in parent1 if x not in parent2[:crossover_point]
            ]
            offspring.extend([child1, child2])
        return offspring

    def mutation(self, population):
        for individual in population:
            if random.random() < 0.1:  # 10% chance of mutation
                i, j = random.sample(range(len(individual)), 2)
                individual[i], individual[j] = individual[j], individual[i]
        return population

    def generate_path(self, ordered_targets):
        path = []
        current_pos = (0, 0)
        vx, vy = 0, 0

        for target in ordered_targets:
            while current_pos != target:
                dx = target[0] - current_pos[0]
                dy = target[1] - current_pos[1]

                move_x = max(min(dx - vx, 1), -1)
                move_y = max(min(dy - vy, 1), -1)

                move = next(
                    key
                    for key, value in self.directions.items()
                    if value == (move_x, move_y)
                )
                path.append(str(move))

                vx += move_x
                vy += move_y
                current_pos = (current_pos[0] + vx, current_pos[1] + vy)

        return "".join(path)


class AStarPathfinder:
    def __init__(self):
        self.directions = {
            1: (-1, -1),
            2: (0, -1),
            3: (1, -1),
            4: (-1, 0),
            5: (0, 0),
            6: (1, 0),
            7: (-1, 1),
            8: (0, 1),
            9: (1, 1),
        }

    def find_path(self, targets: List[Tuple[int, int]]) -> str:
        ordered_targets = self.order_targets(targets)
        path = self.generate_path(ordered_targets)
        return path

    def order_targets(self, targets):
        ordered = []
        current = (0, 0)
        remaining = set(targets)

        while remaining:
            next_target = min(
                remaining, key=lambda x: self.manhattan_distance(current, x)
            )
            ordered.append(next_target)
            current = next_target
            remaining.remove(next_target)

        return ordered

    def manhattan_distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def generate_path(self, ordered_targets):
        path = []
        current_pos = (0, 0)

        for target in ordered_targets:
            while current_pos != target:
                next_move = self.a_star(current_pos, target)
                path.append(str(next_move))
                dx, dy = self.directions[next_move]
                current_pos = (current_pos[0] + dx, current_pos[1] + dy)

        return "".join(path)

    def a_star(self, start, goal):
        def heuristic(node):
            return max(abs(node[0] - goal[0]), abs(node[1] - goal[1]))

        open_set = {start}
        came_from = {}
        g_score = {start: 0}
        f_score = {start: heuristic(start)}

        while open_set:
            current = min(open_set, key=lambda x: f_score[x])

            if current == goal:
                path = []
                while current in came_from:
                    prev = came_from[current]
                    for direction, (dx, dy) in self.directions.items():
                        if (prev[0] + dx, prev[1] + dy) == current:
                            path.append(direction)
                            break
                    current = prev
                return path[-1]  # Return only the first move

            open_set.remove(current)

            for direction, (dx, dy) in self.directions.items():
                neighbor = (current[0] + dx, current[1] + dy)
                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor)
                    if neighbor not in open_set:
                        open_set.add(neighbor)

        return None  # No path found


class SimulatedAnnealingPathfinder:
    def __init__(self, initial_temp=1000, cooling_rate=0.995, iterations=10000):
        self.initial_temp = initial_temp
        self.cooling_rate = cooling_rate
        self.iterations = iterations
        self.directions = {
            1: (-1, -1),
            2: (0, -1),
            3: (1, -1),
            4: (-1, 0),
            5: (0, 0),
            6: (1, 0),
            7: (-1, 1),
            8: (0, 1),
            9: (1, 1),
        }

    def find_path(self, targets: List[Tuple[int, int]]) -> str:
        current_solution = targets.copy()
        current_energy = self.calculate_energy(current_solution)
        best_solution = current_solution.copy()
        best_energy = current_energy
        temperature = self.initial_temp

        for _ in range(self.iterations):
            neighbor = self.get_neighbor(current_solution)
            neighbor_energy = self.calculate_energy(neighbor)

            if (
                neighbor_energy < current_energy
                or random.random()
                < self.acceptance_probability(
                    current_energy, neighbor_energy, temperature
                )
            ):
                current_solution = neighbor
                current_energy = neighbor_energy

                if current_energy < best_energy:
                    best_solution = current_solution.copy()
                    best_energy = current_energy

            temperature *= self.cooling_rate

        return self.generate_path(best_solution)

    def calculate_energy(self, solution):
        total_distance = 0
        current_pos = (0, 0)
        for target in solution:
            total_distance += max(
                abs(target[0] - current_pos[0]), abs(target[1] - current_pos[1])
            )
            current_pos = target
        return total_distance

    def get_neighbor(self, solution):
        neighbor = solution.copy()
        i, j = random.sample(range(len(neighbor)), 2)
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        return neighbor

    def acceptance_probability(self, energy, new_energy, temperature):
        if new_energy < energy:
            return 1.0
        return math.exp((energy - new_energy) / temperature)

    def generate_path(self, ordered_targets):
        path = []
        current_pos = (0, 0)
        vx, vy = 0, 0

        for target in ordered_targets:
            while current_pos != target:
                dx = target[0] - current_pos[0]
                dy = target[1] - current_pos[1]

                move_x = max(min(dx - vx, 1), -1)
                move_y = max(min(dy - vy, 1), -1)

                move = next(
                    key
                    for key, value in self.directions.items()
                    if value == (move_x, move_y)
                )
                path.append(str(move))

                vx += move_x
                vy += move_y
                current_pos = (current_pos[0] + vx, current_pos[1] + vy)

        return "".join(path)


class AntColonyOptimizationPathfinder:
    def __init__(
        self,
        num_ants=50,
        num_iterations=100,
        alpha=1.0,
        beta=2.0,
        evaporation_rate=0.5,
        q=100,
    ):
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.q = q
        self.directions = {
            1: (-1, -1),
            2: (0, -1),
            3: (1, -1),
            4: (-1, 0),
            5: (0, 0),
            6: (1, 0),
            7: (-1, 1),
            8: (0, 1),
            9: (1, 1),
        }

    def find_path(self, targets: List[Tuple[int, int]]) -> str:
        num_targets = len(targets)
        target_index_map = {target: idx for idx, target in enumerate(targets)}

        distance_matrix = [
            [
                self.calculate_distance(targets[i], targets[j])
                for j in range(num_targets)
            ]
            for i in range(num_targets)
        ]
        pheromone_matrix = [
            [1 / (num_targets * num_targets) for _ in range(num_targets)]
            for _ in range(num_targets)
        ]

        best_path = None
        best_distance = float("inf")

        for _ in range(self.num_iterations):
            paths = self.construct_solutions(
                targets, distance_matrix, pheromone_matrix, target_index_map
            )
            self.update_pheromones(paths, pheromone_matrix, target_index_map)

            for path, distance in paths:
                if distance < best_distance:
                    best_path = path
                    best_distance = distance

        return self.generate_path([targets[i] for i in best_path])

    def construct_solutions(
        self, targets, distance_matrix, pheromone_matrix, target_index_map
    ):
        paths = []
        for _ in range(self.num_ants):
            path = self.construct_path(
                targets, distance_matrix, pheromone_matrix, target_index_map
            )
            distance = sum(
                distance_matrix[target_index_map[path[i]]][
                    target_index_map[path[i + 1]]
                ]
                for i in range(len(path) - 1)
            )
            paths.append((path, distance))
        return paths

    def construct_path(
        self, targets, distance_matrix, pheromone_matrix, target_index_map
    ):
        unvisited = set(targets)
        path = [random.choice(list(unvisited))]
        unvisited.remove(path[0])

        while unvisited:
            current = path[-1]
            probabilities = [
                self.calculate_probability(
                    current,
                    next_target,
                    distance_matrix,
                    pheromone_matrix,
                    target_index_map,
                )
                for next_target in unvisited
            ]
            next_target = random.choices(list(unvisited), weights=probabilities)[0]
            path.append(next_target)
            unvisited.remove(next_target)

        return path

    def calculate_probability(
        self, current, next_target, distance_matrix, pheromone_matrix, target_index_map
    ):
        current_idx = target_index_map[current]
        next_target_idx = target_index_map[next_target]

        pheromone = pheromone_matrix[current_idx][next_target_idx] ** self.alpha
        distance = (1 / distance_matrix[current_idx][next_target_idx]) ** self.beta
        return pheromone * distance

    def update_pheromones(self, paths, pheromone_matrix, target_index_map):
        for i in range(len(pheromone_matrix)):
            for j in range(len(pheromone_matrix)):
                pheromone_matrix[i][j] *= 1 - self.evaporation_rate

        for path, distance in paths:
            for i in range(len(path) - 1):
                pheromone_matrix[target_index_map[path[i]]][
                    target_index_map[path[i + 1]]
                ] += (self.q / distance)

    def calculate_distance(self, p1, p2):
        return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

    def generate_path(self, ordered_targets):
        path = []
        current_pos = (0, 0)
        vx, vy = 0, 0

        for target in ordered_targets:
            while current_pos != target:
                dx = target[0] - current_pos[0]
                dy = target[1] - current_pos[1]

                move_x = max(min(dx - vx, 1), -1)
                move_y = max(min(dy - vy, 1), -1)

                move = next(
                    key
                    for key, value in self.directions.items()
                    if value == (move_x, move_y)
                )
                path.append(str(move))

                vx += move_x
                vy += move_y
                current_pos = (current_pos[0] + vx, current_pos[1] + vy)

        return "".join(path)


class BeamSearchPathfinder:
    def __init__(self, beam_width=10):
        self.beam_width = beam_width
        self.directions = {
            1: (-1, -1),
            2: (0, -1),
            3: (1, -1),
            4: (-1, 0),
            5: (0, 0),
            6: (1, 0),
            7: (-1, 1),
            8: (0, 1),
            9: (1, 1),
        }

    def find_path(self, targets: List[Tuple[int, int]]) -> str:
        start = (0, 0)
        beam = [(0, start, [])]
        visited = set()

        while beam:
            new_beam = []
            for cost, current, path in beam:
                if current in visited:
                    continue
                visited.add(current)

                if set(targets).issubset(visited):
                    return self.generate_path(path)

                for direction, (dx, dy) in self.directions.items():
                    next_pos = (current[0] + dx, current[1] + dy)
                    new_cost = cost + 1
                    if next_pos in targets:
                        new_cost -= 10  # Prioritize hitting targets

                    new_beam.append((new_cost, next_pos, path + [direction]))

            beam = sorted(new_beam, key=lambda x: x[0])[: self.beam_width]

        return ""  # No path found

    def generate_path(self, path):
        return "".join(map(str, path))


def send_command(command: str) -> str:
    payload = encode_message(command)
    response = requests.post(URL, data=payload, headers=AUTH_HEADER)
    return decode_message(response.text)


def get_spaceship_coordinates(ship_number: int) -> str:
    return send_command(f"get spaceship{ship_number}")


def solve_spaceship(ship_number: int, path: str) -> str:
    return send_command(f"solve spaceship{ship_number} {path}")


def parse_coordinates(coordinate_list: str) -> List[Tuple[int, int]]:
    return [
        tuple(map(int, line.strip().split()))
        for line in coordinate_list.strip().split("\n")
    ]


def solve_with_algorithm(algorithm, ship_number, coordinates, result_queue):
    path = algorithm.find_path(coordinates)
    result = solve_spaceship(ship_number, path)
    result_queue.put((len(path), result, path, algorithm.__class__.__name__))


def main():
    for ship_number in range(1, 26):  # 1 to 25
        try:
            print(f"Processing Spaceship {ship_number}:")

            # Get coordinates for the current spaceship
            coordinates_str = get_spaceship_coordinates(ship_number)
            coordinates = parse_coordinates(coordinates_str)

            # Create instances of different pathfinding algorithms
            algorithms = [
                SpaceshipPathfinder(),
                GeneticAlgorithmPathfinder(),
                AStarPathfinder(),
                SimulatedAnnealingPathfinder(),
                BeamSearchPathfinder(),
            ]

            result_queue = queue.Queue()
            threads = []

            # Start a thread for each algorithm
            for alg in algorithms:
                thread = threading.Thread(
                    target=solve_with_algorithm,
                    args=(alg, ship_number, coordinates, result_queue),
                )
                thread.start()
                threads.append(thread)

            # Wait for all threads to complete or timeout after 10 minutes
            timeout = time.time() + 600  # 10 minutes
            best_result = None
            optimal_found = False

            while (
                time.time() < timeout
                and not optimal_found
                and any(t.is_alive() for t in threads)
            ):
                try:
                    path_length, result, path, alg_name = result_queue.get(timeout=1)
                    print(
                        f"Algorithm {alg_name} found a solution with length {path_length}"
                    )

                    if result.startswith("Correct"):
                        if best_result is None or path_length < best_result[0]:
                            best_result = (path_length, result, path, alg_name)

                            if path_length <= BEST_SCORES[ship_number]:
                                optimal_found = True
                                print(f"Optimal solution found by {alg_name}!")
                                break
                except queue.Empty:
                    continue

            # Stop all threads
            for t in threads:
                t.join(0.1)

            if best_result:
                path_length, result, path, alg_name = best_result
                print(f"Best solution found by {alg_name}")
                print(f"Path length: {path_length}")
                print(f"Result: {result}")

                if path_length <= BEST_SCORES[ship_number]:
                    print(
                        f"Found optimal or better solution! (Best known: {BEST_SCORES[ship_number]})"
                    )
                else:
                    print(
                        f"Solution found, but not optimal. (Best known: {BEST_SCORES[ship_number]})"
                    )
            else:
                print(
                    f"No solution found for Spaceship {ship_number} within the time limit."
                )

            print()

            # Add a small delay to avoid overwhelming the server
            time.sleep(1)

        except Exception as e:
            print(f"Error processing spaceship{ship_number}: {str(e)}")
            print_exc()
            print()


if __name__ == "__main__":
    main()

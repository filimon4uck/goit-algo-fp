import random
import matplotlib.pyplot as plt


def dice_simulation(num_rolls=100000):
    results = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        results[roll_sum] += 1

    probabilities = {key: (value / num_rolls) for key, value in results.items()}
    return probabilities


def plot_probabilities(simulation_probabilities, analytical_probabilities):
    sums = list(simulation_probabilities.keys())
    sim_probs = list(simulation_probabilities.values())
    ana_probs = [analytical_probabilities[s] for s in sums]

    plt.figure(figsize=(10, 5))
    plt.bar(sums, sim_probs, width=0.4, label="Симуляційні ймовірності", alpha=0.7)
    plt.bar(
        [s + 0.4 for s in sums],
        ana_probs,
        width=0.4,
        label="Аналітичні ймовірності",
        alpha=0.7,
    )
    plt.xlabel("Сума чисел на кубиках")
    plt.ylabel("Ймовірність")
    plt.title("Порівняння симуляційних та аналітичних ймовірностей")
    plt.xticks(sums)
    plt.legend()
    plt.show()


def main():
    analytical_probabilities = {
        2: 1 / 36,
        3: 2 / 36,
        4: 3 / 36,
        5: 4 / 36,
        6: 5 / 36,
        7: 6 / 36,
        8: 5 / 36,
        9: 4 / 36,
        10: 3 / 36,
        11: 2 / 36,
        12: 1 / 36,
    }
    simulation_probabilities = dice_simulation()
    print("Симуляційні ймовірності:")
    for s in range(2, 13):
        print(f"Сума {s}: {simulation_probabilities[s] * 100:.2f}%")

    print("\nАналітичні ймовірності:")
    for s in range(2, 13):
        print(f"Сума {s}: {analytical_probabilities[s] * 100:.2f}%")
    plot_probabilities(simulation_probabilities, analytical_probabilities)


if __name__ == "__main__":
    main()

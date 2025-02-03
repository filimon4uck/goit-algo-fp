items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )
    total_calories = 0
    selected_items = []

    for name, data in sorted_items:
        if budget >= data["cost"]:
            budget -= data["cost"]
            total_calories += data["calories"]
            selected_items.append(name)
    return selected_items, total_calories


def dynamic_programming(items, budget):
    names = list(items.keys())
    costs = [items[name]["cost"] for name in names]
    calories = [items[name]["calories"] for name in names]
    n = len(items)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(budget + 1):
            if costs[i - 1] <= j:
                dp[i][j] = max(
                    dp[i - 1][j], dp[i - 1][j - costs[i - 1]]  + calories[i - 1]
                )
            else:
                dp[i][j] = dp[i - 1][j]
    total_calories = dp[n][budget]
    selected_items = []
    j = budget

    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(names[i - 1])
            j -= costs[i - 1]
    return selected_items, total_calories


budget = 40

print("Greedy Algorithm:", greedy_algorithm(items, budget))
print("Dynamic programming:", dynamic_programming(items, budget))

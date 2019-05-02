def get_factor(thresholds, value):
    for threshold, factor in sorted(thresholds.items()):
        if value <= threshold:
            return factor


def ground_shipping_cost(weight):
    thresholds = {2: 1.5, 6: 3.0, 10: 4.0, float("inf"): 4.75}
    flat_cost = 20
    return flat_cost + (get_factor(thresholds, weight) * weight)


def drone_shipping_cost(weight):
    thresholds = {2: 4.5, 6: 9.0, 10: 12.0, float("inf"): 14.75}
    return weight * get_factor(thresholds, weight)


def cheapest_shipping(weight):
    methods = {
        "drone": drone_shipping_cost,
        "standard ground": ground_shipping_cost,
        "premium ground": lambda weight: 125,
    }
    results = {method: calculation(weight)
               for method, calculation in methods.items()}
    cheapest_method = min(results, key=lambda method: results[method])
    return cheapest_method, results[cheapest_method]


method, cost = cheapest_shipping(10)
print(f"You should use {method} shipping as it will only cost {cost}")

method, cost = cheapest_shipping(1)
print(f"You should use {method} shipping as it will only cost {cost}")

method, cost = cheapest_shipping(8.4)
print(f"You should use {method} shipping as it will only cost {cost}")

method, cost = cheapest_shipping(100)
print(f"You should use {method} shipping as it will only cost {cost}")

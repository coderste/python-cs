def ground_shipping_cost(weight):
    flat_cost = 20
    premium_cost = 125
    if weight <= 2:
        flat_cost += weight * 1.50
    elif weight > 2 and weight <= 6:
        flat_cost += weight * 3.00
    elif weight > 6 and weight <= 10:
        flat_cost += weight * 4.00
    elif weight > 10:
        flat_cost += weight * 4.75
    return flat_cost, premium_cost


def drone_shipping_cost(weight):
    cost = 0
    if weight <= 2:
        cost = weight * 4.50
    elif weight > 2 and weight <= 6:
        cost = weight * 9.00
    elif weight > 6 and weight <= 10:
        cost = weight * 12.00
    elif weight > 10:
        cost = weight * 14.25
    return cost


def cheapest_shipping(weight):
    ground_cost, premium_cost = ground_shipping_cost(weight)
    drone_cost = drone_shipping_cost(weight)
    if drone_cost < ground_cost and drone_cost < premium_cost:
        return "You should use drone shipping as it will only cost " + str(drone_cost)
    if ground_cost < drone_cost and ground_cost < premium_cost:
        return "You should use standard ground shipping as it will only cost " + str(ground_cost)
    if premium_cost < ground_cost and premium_cost < drone_cost:
        return "You should use premium shipping as it will only cost " + str(premium_cost)


print(cheapest_shipping(4.8))
print(cheapest_shipping(41.5))
print(cheapest_shipping(1.5))
print(cheapest_shipping(4.0))

def get_factor(thresholds, value):
    for threshold, factor in sorted(thresholds.items()):
        if value <= threshold:
            return factor


def ground_shipping_cost(weight):
    ''' Compute cost of ground shipping for a package. '''
    flat_cost = 20
    if weight <= 2:
        weight_charge = weight * 1.50
    elif weight <= 6:
        weight_charge = weight * 3.00
    elif weight <= 10:
        weight_charge = weight * 4.00
    else:
        weight_charge = weight * 4.75
    return flat_cost + weight_charge


def premium_shipping_cost(weight):
    ''' Compute cost of premium shipping for a package. '''
    return 125


def drone_shipping_cost(weight):
    cost = 0
    if weight <= 2:
        cost = weight * 4.50
    elif weight <= 6:
        cost = weight * 9.00
    elif weight <= 10:
        cost = weight * 12.00
    else:
        cost = weight * 14.25
    return cost


def cheapest_shipping(weight):
    ''' Determine the cheapest shipping method for a package. '''
    drone_cost = drone_shipping_cost(weight)
    ground_cost = ground_shipping_cost(weight)
    premium_cost = premium_shipping_cost(weight)

    cheapest_tuple = min((drone_cost, 'drone shipping'),
                         (ground_cost, 'ground shipping'),
                         (premium_cost, 'premium shipping'))
    return cheapest_tuple


cost, name = cheapest_shipping(10)
print(f"You should use {name} shipping as it will only cost {cost}")

cost, name = cheapest_shipping(1)
print(f"You should use {name} shipping as it will only cost {cost}")

cost, name = cheapest_shipping(8.4)
print(f"You should use {name} shipping as it will only cost {cost}")

cost, name = cheapest_shipping(100)
print(f"You should use {name} shipping as it will only cost {cost}")

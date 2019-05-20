toppings = ['pepperoni', 'pineapple', 'cheese',
            'sausage', 'olives', 'anchovies', 'mushrooms']

prices = [2, 6, 1, 3, 2, 7, 2]

pizzas = list(zip(prices, toppings))
cheapest_pizzas = sorted(pizzas)
priciest_pizza = cheapest_pizzas[-1]
three_cheapest = cheapest_pizzas[:3]
num_two_dollar_slices = prices.count(2)

num_pizzas = len(toppings)

print(f"We sell {num_pizzas} different kinds of pizza!")

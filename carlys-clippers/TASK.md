# Tasks for this mini-project

-   Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.
    First, let’s sum up all the prices of haircuts. Create a variable `total_price`, and set it to `0`.
-   Iterate through the prices list and add each price to the variable `total_price`.
-   After your loop, create a variable called `average_price` that is the `total_price` divided by the number of prices.
    You can get the number of prices by using the `len()` function.
-   Print the value of `average_price` so the output looks like:
    ```python
    Average Haircut Price: <average_price>
    ```
-   That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.
    Use a list comprehension to make a list called `new_prices`, which has each element in `prices` minus `5`.
-   Print `new_prices`.

## Revenue:

-   Carly really wants to make sure that Carly’s Clippers is a profitable endeavor. She first wants to know how much revenue was brought in last week.
    Create a variable called `total_revenue` and set it to `0`.
-   Use a `for` loop to create a variable `i` that goes from `0` to `len(hairstyles)`
-   Add the product of `prices[i]` (the price of the haircut at position `i`) and `last_week[i]` (the number of people who got the haircut at position `i`) to `total_revenue` at each step.
-   After your loop, print the value of total_revenue, so the output looks like:
    ```python
    Total Revenue: <total_revenue>
    ```
-   Find the average daily revenue by dividing `total_revenue` by 7. Call this number `average_daily_revenue` and print it out.
-   Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under `30` dollars.
    Use a list comprehension to create a list called `cuts_under_30` that has the entry `hairstyles[i]` for each `i` for which `new_prices[i]` is less than 30.
    You can use `range()` in your list comprehension to make `i` go from `0` to `len(new_prices) - 1`.
-   Print `cuts_under_30`.

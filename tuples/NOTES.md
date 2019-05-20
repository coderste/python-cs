# Learn Python: Tuples

So tuples are like lists in python expect the main difference is tuples are immutable which basically means once they are created they can't be changed.

One of the cool things with tuples is you can unpack them really nicely. Take this example

```python
my_info = ('Stephen', 20, 'Software Engineer')

# I can print out the values like so
print(my_info[0], my_info[1], my_info[2])
```

But if we know say age will always be `index` number `1` we can unpack the values into variables like so:

```python
my_info = ('Stephen', 20, 'Software Engineer')

name, age, occupation = my_info

print(name) # Prints 'Stephen'
print(age) # Prints 20
print(occupation) # Prints 'Software Engineer'
```

This is quite a sweet features to be honest.

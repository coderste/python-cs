# Introduction to strings

## They're all Lists!

A string can be thought of as a **list** of characters.

For example

```python
favorite_fruit = "blueberry"
print(favorite_fruit[1])

# The above will print 'l' as the index no. 1 of the string is the `l` character
# Important: indexes start at 0 in python
```

We can also select a slice of strings in python also

```python
foo_name[first_index:last_index]
```

When we slice a string we are creating a **new** string that ares at (and includes) the `first_index` and end at (but excludes) the `last_index`

Diagram below to visualize what's going on

![favorite_fruit string indexes](images/string-index.svg?raw=true 'Favorite Fruit String Indexes')

### Strings are Immutable

If we tried updating the value of say the first character in a string then our first thought would be to do something like

```python
first_name = "Bob"

first_name[0] = "R"
```

But when we run this program we will get the following error message

> TypeError: 'str' object does not support item assignment

That's because in python strings are immutable which means they cannot be updated once defined (think tuples). So in order to update the name we would have to create a new variable and update the value

```python
first_name = "Bob"

fix_first_name = "R" + first_name[1:]
```

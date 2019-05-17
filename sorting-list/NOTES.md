# Sortings List I

So sometimes we may want to sort lists in either numerical or alphabetical order.

We can sort a list _in place_ using `.sort()`. Suppose that we have a list of names for example:

```python
names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
print(names)
```

This would print

```python
['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
```

Now we can apply `.sort()`

```python
names.sort()
print(names)
```

Results are

```python
['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
```

See how `sort` goes after our list, `names`. If we try `sort(names)`, we will get `NameError`

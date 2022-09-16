# Daily challenges

The exercises in this document drill your understanding of the fundamental data structures in Python: lists and dictionaries. A solid understanding of lists and dictionaries makes working with Python much easier, as many modules deal with list- or dictionary-like objects (meaning they have similar methods and attributes; this is called [duck typing](https://en.wikipedia.org/wiki/Duck_typing)). Furthermore, you will become comfortable with iterations over lists and dictionaries. Understanding and applying iterations are a fundamental skill for any programmer.

None of these problems are trivial. If you master these, you are well on your way to master Python. Once you solve a problem, see if you can simplify your code to make it cleaner and more beautiful. Clean and beautiful code is readable and understandable to many, and you will find joy and learning in the journey of making your code more elegant.

## Day 1

### 1

```Python
list1 = [1, 2, 2, 300, 4, 5, 'foo', 6, 7, 'bar', 'foo']
```

Write a function that returns a list of all items in the input list above that are numbers.

### 2

```Python
lol = [[1,2,'foo'],[6,3,{'a':1}],[],['bar']]
```

Write a function that returns a list like the one below for the input list above.

```Python
[[1,2],[6,3],[],[]]
```

### 3

Create a new version of the function from exercise 2 to instead produce the below input (that is, it should squash the list-of-lists into a single list).

```Python
[1,2,6,3]
```

### 4

Write a function that returns a list of all items in the list below that are numbers.

```Python
l2 = [1, 3.14, 'foo', {'bar': '5'}, 1337.42]
```

### 5

Write a function that returns the **index** of all items in list below that are not numbers.

```Python
l2 = [1, 3.14, 'foo', {'bar': '5'}, 1337.42]
```

## Day 2

### 1

Write a function that returns a dictionary, where the key is the list index and the value is the list value at that index

The input:

```Python
dict_list = [1,2,3,4,'banana']
```

Should produce this output:

```Python
{ '0': 1,
'1': 2,
'2': 3,
'3': 4,
'4': 'banana'}
```

### 2

Opposite; but the keys are the values and the values are the indexes!

We have:

```Python
dict_list = [1,2,3,4,'banana']
```

We want:

```Python
{ 1: 0,
2: 1,
3: 2,
4: 3,
'banana': 4}
```

### 3

We have:

```Python
dict_list = [1,1,2, 'foo', 3, 'foo']
```

We want:

```Python
{
1: [0,1],
2: [2],
'foo': [3,5],
3: [4]
}
```

## Day 3

### 1

We have:

```Python
lol = [[1,2], [], [5,1,2,6]]
```

We want:

```Python
[1,2,5,1,2,6]
```

### 2

We have:

```Python
lod = [{'id': '2', 'name': 'Anton'}, {'id': 3}, {'id': 4, 'name': 'Balloo'}]
```

We want:

```Python
{
'id': ['2', 3, 4],
'name': ['Anton', 'Balloo']
}
```

### 3

We have:

```Python
lod = [{'id': '2', 'name': 'Anton'}, {'id': 3}, {'id': 4, 'name': 'Balloo'}]
```

We want:

```Python
{
'id': ['2', 3, 4],
'name': ['Anton', None, 'Balloo']
}
```

## Day 4

### 1

We have:

```Python
l = [{'a': 1}, {'b':2}, {'a': 2, 'c': 5}]
```

We want:

```Python
{'a': [1, None, 2], 'b': [None, 2, None], 'c': [None, None, 5]}
```

### 2

```Python
l = [{'a': 1}, {'b':2}, {'a': 2, 'c': 5}]
```

Write a function that creates a CSV like the one below for the input above.

```Python
"""a, b, c
1, None, None
None, 2, None
2, None, 5
"""
```

### 2

We have:

```Python
l = [{'a': 1}, {'b':2}, {'a': 2, 'c': 5}]
```

We want:

```Python
{'a': [1, None, 2], 'b': [None, 2, None], 'c': [None, None, 5]}
```

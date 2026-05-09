# HackerRank Sets: Average of Distinct Heights

## Question

Ms. Gabriel Williams is a botany professor at District College.

One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

You are given a list of plant heights.

Your task is to:

1. Remove duplicate heights
2. Calculate the average of the remaining unique heights

---

## Example Input

```python
161 182 161 154 176 170 167 171 170 174
```

---

## Distinct Values Only

```python
{161, 182, 154, 176, 170, 167, 171, 174}
```

Notice:

* `161` appeared twice → keep once
* `170` appeared twice → keep once

---

## Average Formula

```python
average = sum(unique_values) / len(unique_values)
```

---

## Starter Code Explained

```python
if __name__ == '__main__':
```

This means:

> "Start running the program here"

You can mostly ignore this line for beginner HackerRank questions.

---

```python
n = int(input())
```

User types:

```python
10
```

Now:

```python
n = 10
```

This is just the number of items.

---

```python
arr = list(map(int, input().split()))
```

User types:

```python
161 182 161 154
```

This becomes:

```python
arr = [161, 182, 161, 154]
```

---

```python
result = average(arr)
```

This sends the list into the function.

Inside the function:

```python
array = arr
```

basically happens.

---

## Working Solution

```python
def average(array):
    unique = set(array)
    average = sum(unique) / len(unique)
    return average


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
```

---

## Main Lesson

The important programming concepts here are:

* functions
* parameters
* sets
* removing duplicates
* calculating averages
* returning values
* passing data

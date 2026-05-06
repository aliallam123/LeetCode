# Python String Validation Methods

Python has built-in string validation methods for basic data checks. These methods can determine whether a string contains alphabetical characters, alphanumeric characters, digits, lowercase characters, or uppercase characters.

---

## `str.isalnum()`

Checks whether all characters in the string are alphanumeric (`a-z`, `A-Z`, `0-9`).

### Examples

```python
print('ab123'.isalnum())
# True

print('ab123#'.isalnum())
# False
```

---

## `str.isalpha()`

Checks whether all characters in the string are alphabetical (`a-z`, `A-Z`).

### Examples

```python
print('abcD'.isalpha())
# True

print('abcd1'.isalpha())
# False
```

---

## `str.isdigit()`

Checks whether all characters in the string are digits (`0-9`).

### Examples

```python
print('1234'.isdigit())
# True

print('123edsd'.isdigit())
# False
```

---

## `str.islower()`

Checks whether all characters in the string are lowercase letters (`a-z`).

### Examples

```python
print('abcd123#'.islower())
# True

print('Abcd123#'.islower())
# False
```

---

## `str.isupper()`

Checks whether all characters in the string are uppercase letters (`A-Z`).

### Examples

```python
print('ABCD123#'.isupper())
# True

print('Abcd123#'.isupper())
# False
```

---

# Task

You are given a string.

Your task is to determine whether the string contains:

- Alphanumeric characters
- Alphabetical characters
- Digits
- Lowercase characters
- Uppercase characters

---

# Input Format

A single line containing a string.

---

# Output Format

Print the following values on separate lines:

1. `True` if the string contains any alphanumeric characters, otherwise `False`
2. `True` if the string contains any alphabetical characters, otherwise `False`
3. `True` if the string contains any digits, otherwise `False`
4. `True` if the string contains any lowercase characters, otherwise `False`
5. `True` if the string contains any uppercase characters, otherwise `False`

---

# Sample Input

```text
qA2
```

---

# Sample Output

```text
True
True
True
True
True
```

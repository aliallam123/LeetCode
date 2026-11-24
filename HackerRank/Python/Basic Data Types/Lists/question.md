
## HackerRank Python Challenge: Lists

**Difficulty:** Easy  
**Topic:** Python Lists, Loops, Conditional Statements

### Problem Description

Initialize an empty list and process `N` commands. Each command performs a specific operation on the list.

### Available Commands

| Command | Description |
|---|---|
| `insert i e` | Insert integer `e` at index `i`. |
| `print` | Print the current list. |
| `remove e` | Remove the first occurrence of integer `e`. |
| `append e` | Add integer `e` to the end of the list. |
| `sort` | Sort the list in ascending order. |
| `pop` | Remove the last element. |
| `reverse` | Reverse the order of the list. |

### Input Format

- The first line contains an integer `N`, representing the number of commands.
- The following `N` lines contain one command each.
- Commands must be executed in the order received.

### Sample Input

```text
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
```

### Expected Output

```text
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
```

### Task

Write a Python program that:

1. Reads the number of commands.
2. Initializes an empty list.
3. Processes each command using the appropriate list operation.
4. Prints the list only when the `print` command is encountered.

### Concepts Practised

- `input()` and `.split()`
- `for` loops and `range()`
- `if` / `elif` conditional statements
- List indexing
- Integer conversion using `int()`
- Python list methods

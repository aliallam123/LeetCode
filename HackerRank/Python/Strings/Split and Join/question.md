# Split and Join a String in Python

In Python, a string can be split using a delimiter.

## Example

    a = "this is a string"
    a = a.split(" ")  # a is converted to a list of strings
    print(a)

Output:

    ['this', 'is', 'a', 'string']

Joining a string is simple:

    a = "-".join(a)
    print(a)

Output:

    this-is-a-string

## Task

You are given a string. Split the string on a " " (space) delimiter and join the words using a - hyphen.

## Function Description

Complete the split_and_join function in the editor below.

### Parameters

- string line: a string of space-separated words

### Returns

- string: the resulting string

## Input Format

The one line contains a string consisting of space-separated words.

## Sample Input

    this is a string

## Sample Output

    this-is-a-string

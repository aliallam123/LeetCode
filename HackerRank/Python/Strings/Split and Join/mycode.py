

def split_and_join(line):
    # write your code here
    x = line.split()
    result = "-".join(x)
    return result
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

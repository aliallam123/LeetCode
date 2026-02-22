def count_substring(string, sub_string):
    counter = 0
    start_point = 0
    end_point = len(sub_string)
    
    while end_point <= len(string):
        if sub_string == string[start_point:end_point]:
            counter += 1
        start_point += 1
        end_point += 1
            
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

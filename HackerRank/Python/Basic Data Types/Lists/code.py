if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        x = input()
        parts = x.split()
        command = parts[0]
        
    
        if command == "insert":
            first_number = int(parts[1])
            second_number = int(parts[2])
            list.insert(first_number,second_number)
            
        elif command == "print":
            print(list)
            
        elif command == "remove":
            first_number = int(parts[1])
            list.remove(first_number)
            
        elif command == "append":
            first_number = int(parts[1])
            list.append(first_number)
            
        elif command == "sort":
            list.sort()
        
        elif command == "pop":
            list.pop()
            
        elif command == "reverse":
            list.reverse()

        else:
            print("nothing to see here buddy")


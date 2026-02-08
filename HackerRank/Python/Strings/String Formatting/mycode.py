def print_formatted(number):
    # your code goes here
    
    width = len(bin(number)) - 2
    
    for i in range(1, number + 1):
        
        # decimal
        decimal = int(i)
        
        #octal
        octal = oct(i)
        cleaned_octal = octal[2:]
        
        #hexadecimal
        hexadecimal = hex(i)
        cleaned_hexadecimal = hexadecimal[2:].upper()
        
        #binary
        binary_format = bin(i)
        cleaned_binary = binary_format[2:]

        dec_str = str(decimal).rjust(width)
        oct_str = cleaned_octal.rjust(width)
        hex_str = cleaned_hexadecimal.rjust(width)
        bin_str = cleaned_binary.rjust(width)

        print(dec_str, oct_str, hex_str, bin_str)

    
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

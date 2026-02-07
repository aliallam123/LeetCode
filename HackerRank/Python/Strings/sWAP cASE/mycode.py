def swap_case(s):
    

    new_sentence = []

    for letter in s:
        if letter.isupper() == True:
            opposite_letter = letter.lower()
            new_sentence.append(opposite_letter)
        else:
            opposite_letter = letter.upper()
            new_sentence.append(opposite_letter)
            
    result = "".join(new_sentence)
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

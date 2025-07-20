def Merge(arrayx,arrayy):

    x = list(set(arrayx))
    y = list(set(arrayy))

    result = x + y 

    result.sort() 
    remove_duplicates = list(set(result))

    return remove_duplicates

Merge([1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12])

first = input('Введите первую строку: ')
second = input('Введите вторую строку: ')



def strip_length(first, second):
    
    if type(first) is not str or type(second) is not str:
        return(0)
    elif len(first) == len(second):
        return(1)
    elif len(first) > len(second):
        return(2)
    elif len(first) != len(second) and second == ("learn"):
        return(3)

a = strip_length(first, second)
print(a)
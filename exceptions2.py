def get_summ(num_one, num_two):
    try:
      
        return int(num_one) + int(num_two)
    except(ValueError):
        return "Как так то?!"

result = get_summ(num_one = input("Что первым?"), num_two = input("Что вторым?"))
print(result)
age = input("Введите ваш возраст:")

def where_to_go(age):
      age = abs(int(age))
      if age <= 7:
            return("go to kindergarten")
            print("go to kindergarten")
      elif age <= 17:
            return("go to school")
            print("go to school")
      elif age <= 22:
            return("go to university")
            print("go to university")
      elif age >= 22:
            return("go to work")
            print("go to work")


a = where_to_go(age)
print(a)
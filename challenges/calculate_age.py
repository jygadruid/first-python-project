def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age

#Calls the function and gets my age

my_age = calculate_age(2049 , 2003)

#Calls the function and gets dad's age

dads_age = calculate_age(2049, 1953)

#Prints both variables into a sentence

print("I am " + str(my_age) + " years, and my dad is " + str(dads_age) + " years old.")


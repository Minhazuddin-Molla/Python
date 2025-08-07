#Understanding f strings in Python
#String formatting in earlier versions
letter ="Hey My name is {} and I am from {}"
country="India"
name= "Minhaz"
print(letter.format(name,country))
#The above code can also be written as letter="Hey My name us {0} and I am from {1}" the no.s 0 and 1 can be considered as index of the format function
#Here the disadvantage is if we have written letter.format(country,name) then the statement would have been wrong
#Now by using f strings the work would be much easier by assigning directly the variables within the curly braces
print(f"Hey My name is {name} and I am from {country}")
print(f'{name} is ')
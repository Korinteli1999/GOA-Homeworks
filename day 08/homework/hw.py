# 1)a = 5
#   b = "10"
#   result = a + b
#   print("Result:", result)

#   კოდი გამოიტანს ერორს დაწერეთ რატომ და ასევე ცალკე დაწერეთ სწორი ფორმა

# problem is in 3rd line because variables a and b cant be added,pyton doesnt define( int + str )


a = 7
b = "12"
result = a + int(b)
print("Result:", result)




#2)
# value = "10"
# result = value * 5
# print("Result:", result)

# გაიხსენეთ მონაცემთა ტიპები და შეასწორეთ ეს

#problem is that value has str value and it cant be mutiplied,
#for that you need to change its value,  either into int or float

value = "7"
result = int(value) * 5
print("Result:" + str(result))



#რა 3 ნაწილისგან შედგება კოდის წერის პროცესი (პასუხი დაასაბუთეთ)

#WRITING(wera)-->RUNNINNG(gashveba)-->DEBUGGING(chasworeba)
#repeat

#we wtite code we run and if it has some errors/bugs we debugg it and run it again




#რა არის debugging ახსენით დეტალურად ეს პროცესი

#debugging is finding and fixing errors/bugs to let the code work properly


# num1 = 1
# num2 = 7
# num3 = 9
# average = num1 + num2 + num3 / 3
# print("Average:", average)

# შეასწორეთ კოდი ისე რომ საშუალო არითმეტიკული სწორად გამოითვალოს

#problem is that it needs parenthes (num1+num2+num3)


num1 = 1
num2 = 7
num3 = 9
average = (num1 + num2 + num3) / 3
print("Average:"+ str(average))




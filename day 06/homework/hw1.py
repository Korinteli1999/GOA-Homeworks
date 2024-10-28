#1)დაწერე პროგრამა, რომელიც string ტიპს integer ტიპად გადააქცევს.

a= "11"
b= int (a)
print(b)


#2)დაწერე პროგრამა, რომელიც შეამოწმებს, არის თუ არა მოცემული ცვლადი float ტიპის

a=988.88

if type(a) == float:
    print(type(a))
else:
    print("it is not float")

    #3)დაწერე პროგრამა, რომელიც integer ტიპს float ტიპად გადააქცევს

a=33
b=float(a)
print(b)

#4)დაწერეთ პროგრამა სადაც მომხმარებელს შემოატანინებთ ინფორმაციას
#  თავის თავზე (name,surname,age,address,gmail) 
# და შემდეგ დაუპრინტეთ ეს ინფორმაცია ერთ დიდ წინადადებად

name = input("name: ")
surname = input("surname:")
age = input("age: ")
address = input("address: ")
gmail=  input("gmail: ")

print("so, with the information you gave me, your name is " + name
       +"; your surname is "+ surname +
      "; you are "+age+"years old, you live in "
        + address +" and you mail is "+ gmail)


#5)ჩამოწერეთ რომელი data type'ბი იცით და ახსენით რა რას ემსახურება

#at the moment we know only three kind of data types whick are 
# 
# int, str and float.
# 
# 
# int stands for integer and it includes all whole numbers,
# for example: a=8; a has integer value because 8 is whole number. 
#
# 
# str stands for string and it includes all the sentences, 
# it can also have numeralic value but 
# it will read it as sentence and not as number. 
# 
# 
# float standds for float and 
# it imcludes numbers that are not whole for example 7.41

#6)დაადეკლარირეთ 3 სტრინგ ტიპის ცვლადი რომელშიც 
# შეინახავთ თქვენი დაბადების წელს,თვეს,დღეს
# შემდეგ გარდაქმენით ინტეჯერებად და დაბეჭდეთ


year = "2007"

month="07"

date = "07"
a= int(year)
b= int(month)
c= int(date)
print(a)
print(b)
print(c)


#7) გარდაქმენით Boolean ტიპის ცვლადი str ტიპის ცვლადად 

a = input ("choose an random number:")

b = input ("choose an 2nd random number:")

real = int(a) > int(b)



print("a is greater than b: " +  str(real))
a = input("enter your birth year ")

b= int(a)

if (2024 -b ) >= 18:
    print("you are full grown adult, born in " + a)
else:
    print("you are still teenage, born in " + a)

month = input("your birth month ")

ex_age = ((2025*12-2)-(int(b)*12+int(month)))

ex_agem = ex_age / 12

print("you should be "+ str(ex_agem)+" years old")




a="10"
b=23.234

c=98

# print(int(a)+int(b)+c)


print("your random(int) number is:"+ str(int(a)+int(b)+c))

print("your random(float) number is:"+ str(float(a)+float(c)+b))

print("difference between your float and int is"+ str((float(a)+float(c)+b)-(int(a)+int(b)+c)))




#მომხმარებლის სახელი
# დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს მის სახელს და შემდეგ მას მიესალმება.
import random

name = input("what's your name ")
gpt = input("name me as your personal bot ")

a = "hi " + name + ", you named me " + gpt +", and i will be your assistant"

b= "so, yo're " + name +", it's nice to get to know you, my name is " + gpt

c= "hi " + name + ", I'm" + gpt

d="hi boss, how you doing?, my name is " + gpt
ran= random.choice[a,b,c,d]


print(ran)


# მოცემული რიცხვის გამრავლება 10-ზე
#  დაწერე პროგრამა, რომელიც მომხმარებელს შემოატანინებს რიცხვს, დაპრინტავს ჯერ ამ რიცხვს და შემდეგ ამ რიცხვის ნამრავლი 10-ზე.

a= int(input("enter your number"))

b= a *10

print(str(a) + " tome 10 is equal to" + str(b))


#ორი რიცხვის გამოკლება
# დაწერე პროგრამა, რომელიც შემოატანინებს მომხმარებელს ორი რიცხვს და დაბეჭდავს მათ სხვაობას.

a = int(input(" enter first number"))

b= int(input("enter second number"))

print ( str(a)+ " first number that you inputted minus " +str(b)+" second number that you inputed is equal to" + str(a-b))



#სახელი და ასაკი
# დაწერე პროგრამა, რომელიც მომხმარებელს შემოატანინებს სახელს და გვარს და 
# დაპრონტავს ამ ორ მონაცემს ასეთი ფორმატით: "თქვენი სახელია X ხოლო თქვენ ხართ Y წლის"

name =  input("name:")

surname= input("surname: ")

age= int(input("age"))

# print(age)
print("so your name is "+ name+", your surname is "+ surname+"and your age is "+ str(age))



#მეგობრის სახელის შემოტანა
#  დაწერე პროგრამა, რომელიც შემოატანინებს მომხმარებელს მისი საუკეთესო 
#   მეგობრის სახელს და გვარს და დაპრინტავს ასეთი ფორმატით: "თქვენი მეგობრის სახელია X ხოლო გვარია Y".

a = input("ur best friend name ")

b = input("ur best friend surname ")


print("ur best friend goes by the name of "+ a+", and his surname is "+b)



# ციფრის გამრავლება 2-ზე
# დაწერე პროგრამა, რომელიც მომხმარებელს შემოატანინებს რიცხვს, 
# დაპრინტავს ჯერ ამ რიცხვს და შემდეგ ამ რიცხვის ნამრავლი 2-ზე.


a = int(input("num: "))

print("you entered number "+str(a)+ ". it multiplied by two is equal to"+ str(2*a))



#  დაწერე პროგრამა, რომელშიც მომხმარებელი შემოიტანს 
#  მის საყვარელ ფერს და დაბეჭდავს ასეთი ფორმატით: "შენი საყვარელი ფერი არის X".

a= input("favourite color: ")

print("your favourite color is " + a)


# ქალაქის შემოტანა
#  დაწერე პროგრამა, რომელშიც მომხმარებელი შემოიტანს ქალაქს სადაც ცხოვრობს, შემდეგ კი გამოიტანს ასეთი ფორმატით: "შენ ცხოვრობ ქალაქში სახელად x"

a = input("city you live in: ")

print("you live in"+a)


#print('hello world')
# name = 'yaakov'
# lastname = 'magar'
# age = 40
# print (name)
# print (age)
# print (name + lastname)
# print (name, lastname)
#
# print (age + 5)
#
# print (str(age) + name)
# print (age, name)
#
#
#
# num1=10
# num2=20
# print (num1*num2)
# print (num1 + num2)
# print (num1/num2)
# print (num1 - num2)
# print ("my apt number is:" + str(7))

a=6
b=4

# if a>b:
#     print("a is biger")
#     if a >5:
#         print("abc")
# if a > b and a < 10:
#     print("a is bigger..")
# if (a > b) or (a > 10):
#     print ("ddd")

# if a>100:
#     print(1)
# elif a>3:
#     print(2)
# else:
#     print(3)



#age= input("please enter your age\n")
# if int(age) > 18:
#     print ("adult")
#


# password= "12345"
# get_password=input ("please enter your password")
# if get_password == password:
#     print("logged in")
# else:
#     print("access denied")

# age=int(input("please enter your age\n"))
# hight=int(input("please enter your hight\n"))
# if age>12 and hight >160:
#     print("ok")
# else:
#     print ("forbidden")


#Loops
# for x in range(3):
#     print (x)
# for x in range(3,5): #x will start with value 3
#     print(x)


# for x in range(3,8,1): #start from 3 till 8, jump in 2
#     print(x)

# count=0
# while count<5:
#     print(count)
#     count+=1

# count=0 #will run forever till count >=5
# while 1>0:
#     print(count)
#     count+=1
#     if count >=5:
#         break


# for x in range (100):
#     if x==7:
#         break
#     print (x)

# for x in range (10):
#     if x==7:
#          continue #will contirunue to next iteration (1...6,8....9) 7 will be missing.
#     print(x)
#


#functions

# def main():
#     print ("hello")
#
# if __name__=="__main__":
#     main()
#
# def do_someting():
#     x=2
#     y=4
#     print (x+y)
#
# do_someting()
#
# def run():
#      return "hello"
# x= run()
# print (x)
#
# def run(name):
#     print (name)
#
# run ("yaakov")
#
# def run(name):
#     return "hello"+name
#
# print (run("yaakov")) #hellowyaakov


# def print_num (num1):
#     print (num1)
# print_num(3)

#using pass as placeholder, incase we want to decalre
#
# def non_complete_function()
#     pass #I decalre the function but will complete the conetent later
# non_complete_function()

# import datetime #for import built-in python module
# print(datetime.datetime.now()) #module, class, function

# from datetime import datetime #instead of import built-in python module, I mention that from datetime file I want to import the datetime class
# print(datetime.now()) #class, function


#data strcuture
# a=[5, "yaakov", True] #a[0]=5
# a[0]=6
# print (a[0])
# a.pop(1) #remove index with its value "yaakov" and shift all left
# print (a) # [6, True]
#
# a.append(111) #append to last place[6,"yaakov",True,111]
# a.insert(1,7) #insert after index 1 the value 7-> shift right all


# my_list =[1,4,"a",True]
# print (my_list[0])
# my_list[1]=2
# print (my_list)
# my_list.pop(2)
# print (my_list)
# my_list.append("last")
# print (my_list)
# my_list.insert(2,False)
# print (my_list)
#
# print(len(my_list)) #print the number of size our list
# for x in my_list: #without index
#     print(x)
#
# for x in range (len(my_list)): #with Index
#     print(my_list[x])
#
# #tuple , once I set, can't be change. such list of session. faster than list
# tup = "summer","winter","sprint","fall"
# print (tup[0]) #summer
#
# #dictionary, key:value
# my_dictionary ={'A':1,'B':2,'C':3}
# my_dictionary['A']=5
# print(my_dictionary) #A:5,B:2,C:3
#
# print (my_dictionary.keys()) #dict_keys(A,B,C)
# print (my_dictionary.values()) #dict_values(5,2,3)
# del (my_dictionary['A'])
# print (my_dictionary) # B:2,C:3
#
#



#Files
# my_file=open("d:/temp/readme.txt",'r+') #will open/create file for read and write
# content=my_file.read()
# print(content)
#
# content=my_file.write("Yuli Magar") #will add this string to end of the file

my_file=open("d:/temp/readme.txt",'a+') #will append to end of file
content=my_file.read()
# print(content)
# my_file.seek(0) #will set the cursor back to start of the file
# content=my_file.write("\nLital Magar") #\n will start new line and add this string to end of the file
# print (content)
#
# my_file=open("d:/temp/readme.txt",'a+',encoding='utf-8') #recomended to add enconding, default utf-8

my_file.close()


# try:
#     my_file=open("d:/temp/readme.txt",'r') #will append to end of file
#     content=my_file.write("Yaakov")
#
# # except:
# #
# #     print("my except")
#
# # except IOError as e: #will insert the original error message into object e. ONLY for EXCEPTION OF IOError
# #     print(e)
# finally:
#     print("123") #now the program will print becouse the expecpt: we didn;thorogh out from the program

# try:
#     x=1/0
# except:
#     #print("catched in exception")
#     y=0
# finally:
#     print("print anyway")
#     print(y)



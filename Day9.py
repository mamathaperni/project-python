# strings 
# 1. creating strings :there are 3 ways to write strings
single_quote_strings='hello'
double_quote_strings="hello"
triple_quote_strings='''hello'''


print('hello')
print("hello")
print('''hello''')
print("""hello""")

#triple code is also called multiline string it is used mostly when in the form of sentance

multiline_string='''
this is first line in my story
this is line 2 in my story
'''
#this multiple line sting will not we consider by the compiler.
#accessing characters in a string
print(single_quote_strings[0])
print(single_quote_strings[-1])
#here strings can access by using index

#slicing the string
print(single_quote_strings[:3])

#negetive indexing
print(double_quote_strings[-1])

#to add 2 strings or concatenation of two strings
string1="perni"
string2="Mamatha"
print(string1+string2)
print(string1+" "+string2)#for getting space
#string repitation(if we want to repeat a string multiple times)

s="hai"
print(s*5)

s2="ha "
s3="!"
print(s+s2*3+s3)

#string length
s="hai"
print(len(s))
string2="Mamatha " # here we print it as 8 characters because we give space
print(len(string2))
#checking sub string
# sub string is a part of main string
string16="perni Mamatha"
print("perni" in string16)#True
print("Perni" in string16)#False (so here we can say that python is casesenstive language)

#sting Functions /methods
name="manasa"
print(name.upper())
name="MANASA"
print(name.lower())
# JOIN STRIP,SPLIT,REPLACE these are some important topics in string methods

#string formatting-f string
name='MANASA'
print(f"my name is{name}")

# for AI asking questions
# iheard that strings are one of the most asked process during iring process i am learing in python is this actually true if it is true can you suggest me some of the questions on strings in python


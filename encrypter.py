# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 00:23:22 2018

@author: Akshay Tyagi
"""
from random import shuffle
def code_generator():
    global code
    code=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",0,1,2,3,4,5,6,7,8,9,"@","!","#","$","%","&","*","(",")","-","+","/"]
    shuffle(code)
    return code

def user_input():
    user_inp=list(input("Enter The Message to be Encrypted:\n"))
    return user_inp

def encrypter(c):
    global b,key
    key_list=[]
    for i in range(1,26):
        key_list.append(i)
    shuffle (key_list)
    key = key_list[0]
    code_generator()
    for i in range(len(c)):
        if c[i] in code:
            j= code.index(c[i])+key
            if j>(len(code)-1):
                j=j-len(code)
            c[i] =code[j]
    return c

def decrypter():
    for i in range(len(a)):
        if a[i] in b:
            j= b.index(a[i])-key
            if j<0:
                j=len(b)+j
            a[i] = b[j]
    return a
    
a=user_input()
z=encrypter(a)
print("\nEncrypted Message:")
for i in z:
    print(i,end="")
ans=input("\nWould you to decrypt the code: (y/n): ")
if (ans=="y"):
    x= decrypter()
    for i in x:
        print(i,end="")
else:
    print("Code has not been decrypted");
    
    

    




# Task 1
# a = input()
# try:
#    if type(eval(a)) == int:
#       print('eded')
#    elif type(eval(a)) == bool:
#       print('boolean')
# except:
#    print('string')
   
# Task 2
# adeyisen=input('deyisen elave edin:')

# try:
#    val = int(adeyisen)
#    print(adeyisen + ": Reqemdi")
# except ValueError:
#    print(adeyisen+": Reqem deyil")


# deyisen=input("Elave et: ")
# a=list(deyisen) 
# a.reverse()
# # print(a[::-1])        
# print(a)    

# a = input('Soz daxil edin: ')
# say = 0
# for i in a :
#    if i.isupper():
#       say+=1
# print(say)
arr=['Samir','Mehemmed','Qurbani','Vesile','Qurbaneli','Memmedaga','Nurlan','Leman','Emil','Gulshen']
print(len(arr))

say=0
for i in arr:
    for a in i:
        say=say+1
        print(say)

for i in arr:
    for a in i:
        if a == "m":
            print(i)

newArr=list(arr)
arr.extend(newArr)
print(arr)
cem = 0
# for x in range(100):
#     if x%10>=0 :
#         cem=cem+x
        
print(cem)
for x in range(501):
    if x%100>=0 :
        cem=cem+x
        
print(cem)      
        
        
# c = 0
# for i in range(100):
#     c = c + i

# print(c)

    
    

    
   
   
   
   
   
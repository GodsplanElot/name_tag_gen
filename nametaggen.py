name = input("enter name?: ")
arrayofnames = name.split()    

j = 1
initials = []
for x in arrayofnames:
    if j==len(arrayofnames):
        initials.append(x.upper())
    else:
        initials.append(x[0].upper())
    j+=1

print()
        
shortname = ""
for i in range(0,len(initials)):
    shortname += initials[i] + " "

print (f"Welcome Officer : {shortname}")    
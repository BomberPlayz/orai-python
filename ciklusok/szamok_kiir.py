for i in range(1,11):
    print(i)

print()

for i in range(11):
    if i <= 0:
        continue
    
    print(i)

print()

for i in range(1,21):
    print(i,end=", ")
    if i >=20:
        print("\b\b ")
        

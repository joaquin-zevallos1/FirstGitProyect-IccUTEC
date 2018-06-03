e=int(input())
listan=[]
i=0
while i<e:
    listan.append(input("Ingresa su edad: "))
    i=i+1
mayor=int(max(listan))
menor=int(min(listan))
suma = str(mayor)+ str(menor)
print(listan)
print(mayor)
print(menor)
print(mayor+menor)

number = 2**1000
soma=0

rest = int(0)
int(number)
while number >0: 
    rest = number % 10 # take the number after the comma and insert a variable
    soma = soma+rest #whenever you get the rest sum
    number = int(number/10) #remove number after comma, until number become 0

print(soma)  

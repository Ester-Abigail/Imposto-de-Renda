salario = float (input("Digite um salario: "))
base = salario
imposto = 0 

if base <= 1903.98:
     print ("sua aliquota é 0%")

if ((base >= 1903.99)  <= 2826.65):
      imposto = imposto + ((base - salario ) * 7.5)
      base = salario
   

if  ((base >= 2826.66)  <= 3751.05):
      imposto = imposto + ((base - salario ) * 15)
      base = salario
    

if  ((base >= 3751.06)  <= 4664.68):
      imposto = imposto + ((base - salario ) * 22.5)
      base = salario
      

      
if  base > 4664.68 :
      imposto = imposto + ((base - salario ) * 27.5)
      base = salario
      
print ("Sua aliquota é")
print(salario, imposto)
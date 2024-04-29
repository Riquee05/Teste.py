#teste

# Ola Mundo com Variavel
msg = ("Hello World")
print(msg)

#Concatenação
first_name = 'Henrique'
last_name = 'Oliveira'
full_name = first_name + ' ' + last_name
print(full_name)

# Definir função
def Minha_Função (p1,p2):
 resultado = p1 + p2
 return resultado

# Função Soma
def sum (a, b):
 return (a + b)

a = int(input('Coloque o 1° Numero:  '))
b = int(input('Coloque o 2° Numero:  '))

print(f'Soma de {a} e {b} é igual a {sum(a, b)}')

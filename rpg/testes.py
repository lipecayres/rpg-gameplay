nota_1 = float(input('Qual valor da primeira nota? '))
nota_2 = float(input('Qual valor da segunda nota? '))
media = (nota_1 + nota_2) / 2

print(f"Resultado: {media} ", end = "")

if media >= 7 and media < 10:
    print('Aprovado')
elif media == 10:
    print('Aprovado com Distinção')
else:
    print("Reprovado") 

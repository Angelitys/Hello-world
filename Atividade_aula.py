nota1= float(input("Adicione a primeira nota= ")) #float para números quebrados
nota2= float(input("Adicione a segunda nota= "))
media= 7.0
resultado= (nota1 + nota2) /2

if resultado >= 7.0:
    print("Aprovado") #Espaçamento se  chama identação
else:
    print("Reprovado")
    print("Sua média é=" , resultado)
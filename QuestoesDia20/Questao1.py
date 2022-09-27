Nota1: float; nota2: float; nota3: float; media: float; somaP: float; somaN: float
Nota1= float(input("Digite sua nota do trabalho do laboratório: "))
Nota2= float(input("Digite sua nota da avaliação semestral: "))
Nota3= float(input("Digite sua nota do exame final: "))
SomaN= nota1*2 + nota2*3 + nota3*5
SomaP= 2 + 3 + 5
Media= somaN / somaP
round(media, digits=1)

if media >= 8:
    print(f"Sua nota é: {media}, conceito é A")
elif media >= 7 and media<8:
    print(f"Sua nota é: {media}, conceito é B")
elif media >= 6 and media<7:
    print(f"Sua nota é: {media}, conceito é C")
elif media >= 5 and media<6:
    print(f"Sua nota é: {media}, conceito é D")
else:
    print(f"Sua nota é: {media}, conceito é E")
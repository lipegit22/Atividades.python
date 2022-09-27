
from string import octdigits

ano=int(input("Informe em que ano estamos (XXXX): "))
mes=int(input("Informe o mês em que estamos (XX): "))
dia=int(input("Informe em que dia estamos (XX): "))
hora=int(input("Infome que horas são (sem minutos): "))
minutos=int(input("informe em que minuto estamos: "))

print(dia,'/',mes,'/',ano)

if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")

print(hora,':',minutos)

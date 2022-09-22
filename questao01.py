pes:float; jarda:float; mi:float;pol:float
medida= float(input("Informe sua medida em pes: "))
jardas=medida/3
pol= medida*12
mi= medida/1.760
print(f"seu resultado em polegadas é de {round(pol,2)}")
print(f"seu resultado em jardas é de {round(jardas,2)}")
print(f"seu resultado em milhas é de {round(mi,2)}")
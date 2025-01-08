#Copiar lista
sudeste = ["Rj","Sp","Mg","Es"]
estados = sudeste
print(sudeste)
print(estados)

sudeste[0] = "Rio de Janeiro"
print(sudeste)
print(estados)

sudeste.remove("Mg")
print(sudeste)
print(estados)

sul = ['Rj', 'Sc', 'Pr']
sul2 = sul.copy()
print("--------")
print(sul)
print(sul2)
print("--------")
sul.remove("Rj")
print(sul)
print(sul2)
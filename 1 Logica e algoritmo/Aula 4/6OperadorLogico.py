tenho_sede = False
tenho_fome = True

if tenho_fome and tenho_sede:
    print("Comprar sanduíche e Coca-cola!")
elif tenho_sede and not tenho_fome:
    print("Comprar coca-cola.")
elif not (tenho_sede) and tenho_fome:
print("Comprar sanduíche.")
else:
print("Não gastar dinheiro.")
def Fazer_big_mac(nome):
    print(f'Sanduíche Big Mac {nome}')

def fazer_batata(tamanho):
    print(f'Batata {tamanho}')

def preparar_refrigerante(tipo,tamanho):
    print(f'{tipo} {tamanho}')

def combo_bigmac(nome,tamanho_batata,tipo_refrigerante,tamanho_refri):
    Fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refrigerante,tamanho_refri)

combo_bigmac("Vanessa","Média","Coca-cola","Grande")
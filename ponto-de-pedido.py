c =  float(input("Unidades consumidas - por dia:\n"))
tr = int(input("Tempo de reposição - em dias:\n"))
es = int(input("Estoque de segurança - em unidades\n"))
pp = c * tr + es



print("Ponto de pedido:" (pp))
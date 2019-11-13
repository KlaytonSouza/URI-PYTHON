nomeVencedor = str.upper(input())
salarioFixo = float(input())
totalVendas = float(input())
porcentagem = totalVendas/100
comissao = porcentagem*15
total = salarioFixo+comissao
print("TOTAL = R$ %.2f" % total)

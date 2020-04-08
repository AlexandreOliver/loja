from cores import cor
def fpag(fpg, preço):
    taxa_base = 10 / 100
    print(cor('roxo'))
    if fpg == 1:
        taxa = preço * taxa_base
        preço = preço - taxa
        print('Á vista, desconto de 10%')
        return "Preço á pagar: R${:.2f}".format(preço)
    elif fpg == 2:
        taxa = taxa_base / 1 / 2
        desconto = preço * taxa
        preço = preço - desconto
        print('Á vista no Cartão, desconto de 5%')
        return 'Preço á pagar: R${:.2f}'.format(preço)
    elif fpg == 3:
        print('Em 2x no Cartão')
        print('Preço á pagar: R${:.2f}'.format(preço))
        return 'Parcelas de R${:.2f}'.format(preço / 2)
    elif fpg == 4:
        taxa = taxa_base + taxa_base
        juros = preço * taxa
        parcelas = (preço + juros) / 3
        print('3 parcelas ou mais, 20% de juros')
        print('Preço á pagar: R${:.2f}'.format(preço + juros))
        return 'Parcelas de R${:.2f}'.format(parcelas)



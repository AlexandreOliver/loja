from project.Component.cores import cor


def fpag(fpg, preco):
    taxa_base = 10 / 100
    print(cor('roxo'))
    if fpg == 1:
        taxa = preco * taxa_base
        preco = preco - taxa
        print('Á vista, desconto de 10%')
        return "Preço á pagar: R${:.2f}".format(preco)
    elif fpg == 2:
        taxa = taxa_base / 1 / 2
        desconto = preco * taxa
        preco = preco - desconto
        print('Á vista no Cartão, desconto de 5%')
        return 'Preço á pagar: R${:.2f}'.format(preco)
    elif fpg == 3:
        print('Em 2x no Cartão')
        print('Preço á pagar: R${:.2f}'.format(preco))
        return 'Parcelas de R${:.2f}'.format(preco / 2)
    elif fpg == 4:
        taxa = taxa_base + taxa_base
        juros = preco * taxa
        parcelas = (preco + juros) / 3
        print('3 parcelas ou mais, 20% de juros')
        print('Preço á pagar: R${:.2f}'.format(preco + juros))
        return 'Parcelas de R${:.2f}'.format(parcelas)


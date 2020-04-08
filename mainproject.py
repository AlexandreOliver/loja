from time import sleep
from vars import produtos, idproduto, carrinho
from fopag import fpag
from cores import cor


print(cor('amarelo'), "—"* 10,cor('azul'), "InfoTech",cor('amarelo'), "—" * 10, cor('pausa'))
sleep(0.2)
print(cor('azul'), "Deseja comprar algo? ", end=" ")
cliente = input().upper()
sleep(0.2)
if cliente[0] == "S":
    sleep(0.5)
    print("Produtos Disponíveis:\n")
    sleep(0.5)
    num = 0
    print(cor('verde'))
    print("N°| Preço(R$)", " " * 2, " " * 4, "Produtos\n")
    sleep(0.5)
    for p, v in produtos.items():
        num += 1
        print(num, "|", " " * 2, "{:.2f}".format(v), "-" * 11, p)
        sleep(0.5)
    sleep(1)
    print(cor('azul'))
    escolha = int(input("\nNumero do produto que deseja comprar: "))
    sleep(0.5)
    print(cor('verde'), idproduto[escolha], "R$ {:.2f}".format(produtos[idproduto[escolha]]), cor('pausa'))
    carrinho.append(idproduto[escolha])
    sleep(0.5)
    count = 0
    while True:
        sleep(1)
        if count == 0:
            print(cor('azul'))
            cliente = input("Gostria de comprar mais algo? ").upper()
        else:
            print(cor('azul'))
            cliente = input("\nmais algo? ").upper()
        count += 1
        if cliente[0] == "S":
            outroproduto = int(input("Digite o numero do produto: "))
            carrinho.append(idproduto[outroproduto])
            sleep(1)
            print(cor('verde'), "+", idproduto[outroproduto], "R$ {:.2f}".format(produtos[idproduto[outroproduto]]),"Reais", cor('pausa'))

        else:
            break
    sleep(0.5)
    print(cor('azul'), "Processando...")
    sleep(2)
    print(cor('azul claro'), "\nSeus Produtos:")
    sleep(1.5)
    total = 0
    for p in carrinho:
        print(p, "-"*9, "R${:.2f}".format(produtos[p]))
        total += produtos[p]
        sleep(1)
    print("Calculando...")
    sleep(1.5)
    print("Total: R${:.2f}".format(total))
    sleep(0.5)
    print(cor('azul'))
    z = input("\nAperte 'ENTER': ")
    sleep(0.5)
    print("...")
    sleep(0.5)
    print("\nAgora partiremos para a forma de pagamento")
    sleep(1.5)
    print(cor('verde'), '—' * 12, 'Digite:', '—' * 12)
    print('|1 para Á VISTA(dinheiro/cheque)|\n'
          '|2 para Á VISTA no Cartão       |\n'
          '|3 para Parcelar em 2x no Cartão|\n'
          '|4 para Parcelar em 3x ou mais. |')
    print('—' * 33)
    print(cor('azul'))
    f = int(input('Digite:'))
    print("\n", fpag(f, total))



else:
    print("Tchauu!!")

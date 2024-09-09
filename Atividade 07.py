# Enunciado: Uma loja aplica um imposto de 12% sobre o valor dos produtos. Crie um programa que receba o preço de um produto e calcule o preço final com o imposto incluído.

valordoproduto = float(input("Digite o valor do produto"))

valorimposto = valordoproduto * 12/100

valorfinal = valordoproduto + valorimposto

print(f"""O valor do produto é: {valordoproduto}
O valor do imposto é: {valorimposto}
O valor final com imposto é: {valorfinal}""")
# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:

itens = []
EQUIPAMENTOS = 3
# TODO: Crie um loop para solicita os itens ao usuário:
while len(itens) < EQUIPAMENTOS: 
# TODO: Solicite o item e armazena na variável "item":
  item = input("")
# TODO: Adicione o item à lista "itens":
  itens.append(item)

# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")
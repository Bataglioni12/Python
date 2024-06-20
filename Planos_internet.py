# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:

    
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
def recomendar_plano(consumo): 
  if consumo <= 10:
    print("Plano Essencial Fibra - 50Mbps")
    
  elif consumo >10 and consumo <20:
    print("Plano Prata Fibra - 100Mbps")
    
  else:
    print("Plano Premium Fibra - 300Mbps")
    
    return consumo
    
# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
(recomendar_plano(consumo))

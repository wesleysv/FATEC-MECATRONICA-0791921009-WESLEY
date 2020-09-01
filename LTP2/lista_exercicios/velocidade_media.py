'''2.Agora, dado um espaço inicial e um espaço final, um tempo inicial e um tempo final, determine o valor da velocidade média destes dados.'''

espaco1 = int(input('digite o a posição inicial do veiculo:'))
espaco2 = int(input('digite o a posição final do veiculo:'))
tempo1 = int(input('digite o tempo inicial do veiculo:'))
tempo2 = int(input('digite o tempo final do veiculo:'))
media = (espaco2 - espaco1) / (tempo2 - tempo1) 
print('a velocidade média final é de:',media)

'''Escreva um programa que possibilite o usuário informar um valor 
da velocidade, uma posição inicial e um instante de tempo para 
determinar o valor final da posição'''

velocidade = int(input('digite a velocida inicial do veiculo:'))
posição = int(input('digite a posição inicial do veiculo:'))
percurso =  int(input('em quanto tempo?'))
valor_final = (velocidade / posição) * percurso
print('o valor final da posição é:',valor_final)  

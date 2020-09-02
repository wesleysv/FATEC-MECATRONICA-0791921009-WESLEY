'''3. Escreva um programa que possibilite o usuário determinar qual a faixa do imposto
de renda que ele deve pagar, dado o valor de entrada que ele informar.'''

renda = float(input('digite o valor base a ser calculado:'))

if renda <= 1903.98:
   print('voce possue isencao de inposto de renda')

if (renda > 1903.98) and (renda <= 2826.06):
  aliquota = float (renda * 0.075)
  print('sua aliquota e de 7.5% ou seja {} e a parcela a ser deduzida do IRPF e de 142,80'.format(aliquota))

if (renda > 2826.06) and (renda <= 3751.05 ):
  aliquota = float (renda * 1.5)
  print('sua aliquota e de 15% ou seja {} e a parcela a ser deduzida do IRPF e de 354.80'.format(aliquota))

if (renda > 3751.05) and (renda <= 4664.68 ):
  aliquota = float (renda * 22.5)
  print('sua aliquota e de 22.5% ou seja {} e a parcela a ser deduzida do IRPF e de 636.13'.format(aliquota))

if (renda > 4664.68):
  aliquota = float (renda * 27.5)
  print('sua aliquota e de 27.5% ou seja {} e a parcela a ser deduzida do IRPF e de 869.36'.format(aliquota))

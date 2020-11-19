opcao = int(input("deseja converter estrela para triagulo?(digite 1) ou triangulo para estrela?(digite 2)"))

if opcao == 1:
 (print ("estrela para triagulo"))
 rab = int (input("digite o resistor correspondente a Rab:"))
 rac = int (input("digite o resistor correspondente a Rac:"))
 rbc = int (input("digite o resistor correspondente a Rbc:"))
ra = int ((rab*rac)/(rab+rac+rbc))
rb = int ((rab*rbc)/(rab+rac+rbc))
rc = int ((rac*rbc)/(rab+rac+rbc))

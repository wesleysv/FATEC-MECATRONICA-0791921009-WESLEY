opcao = int(input("deseja converter estrela para triagulo?(digite 1) ou triangulo para estrela?(digite 2)"))



if opcao == 1:(
   (print ("estrela para triagulo"))
rab = float (input("digite o resistor correspondente a Rab:"))
rac = float (input("digite o resistor correspondente a Rac:"))
rbc = float (input("digite o resistor correspondente a Rbc:"))
ra = float ((rab*rac)/(rab+rac+rbc))
rb = float ((rab*rbc)/(rab+rac+rbc))
rc = float ((rac*rbc)/(rab+rac+rbc))

print("RA=\t RB=\n RC=\n",ra,rb,rc))

elif opcao == 2:
  print ("triagulo para estrela")
  ra = float (input("digite o resistor correspondente a Ra:"))
  rb = float (input("digite o resistor correspondente a Rb:"))
  rc = float (input("digite o resistor correspondente a Rc:"))
 rab = float (((ra*rc) + (rc*rb) + (rb*ra))/(rc))
 rac = float (((ra*rc) + (rc*rb) + (rb*ra))/(rb))
 rbc = float (((ra*rc) + (rc*rb) + (rb*ra))/(ra))

print("Rab=\t RAC=\n RBC=\n",ra,rb,rc)

else:
  print("não exiete essa opcao.")

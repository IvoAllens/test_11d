import math
mala1=float(input("Ievadi malas garumu, kas lielāks par 5cm.\n"))
if mala1>=5:
  laukums1=math.pow(mala1,2)
  mala2=mala1+5
  laukums2=math.pow(mala2,2)
  starpiba=100*(laukums2/laukums1)
  print("Procenti:",round(starpiba) ,"%")
else:
  print("Ievadītais skaitlis neder")
  

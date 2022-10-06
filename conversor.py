def converter (valor):
  x = valor * 0.39 
  file = open('arquivo.txt',"w+")
  file.write("O valor {} em centímetros corresponde a {:.2f} valor em polegadas".format(valor, x))
  file.seek(0,0)
  print(file.read())
  file.seek(0,0)
  file.close()
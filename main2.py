import figuras

figura1 = figuras.Figura("")
figura1.setTipo("Figuras Geometricas")
print("Tipo de Figura ==== : " +figura1.getTipo())

print("\n")
print("######## Para los triangulos ##############\n",end="")
print("\n")

figura2 = figuras.Triangulo("","",2,2,2,90)
figura2.setTipo("Triangulos")
figura2.setNombreTri("Triángulos")
figura2.setLados(3)
figura2.setAngulosTri(3)
figura2.setTamano_angTri(90)

print("Tipo de Figura =======> : " + figura2.getTipo())
print("Nombre ===============> : " + figura2.getNombreTri())
print("Lados de Figura ======> : " + str(figura2.getLadosTri()))
print("Angulos de la Figura => : " + str(figura2.getAngulostri()))
print("Tamaño del Angulo ====> : " + str(figura2.getTamano_angTri()))

print("\n")
print("######### Para los cuadrados ##############\n",end="")
print("\n")

figura3 = figuras.Cuadrilatero("","",4,4,4,90)
figura3.setTipo("Cuadrilatero")
figura3.setNombreCua("Cuadrado")
figura3.setladoCua(4)
figura3.setverticeCua(4)
figura3.setTamanoAngCua(90)

print("Tipo de Figura =======> : " + figura3.getTipo())
print("Nombre de Figura =====> : " + figura3.getNombreCua())
print("Lados de la Figura ===> : " + str(figura3.getladoCua()))
print("Angulo de la Figura ==> : " + str(figura3.getverticeCua()))
print("Tamaño del Angulo ====> : " + str(figura3.getTamanoAngCua()))



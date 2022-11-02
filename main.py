#?x w ?y w ?z = R
#?x w ?y w ?z = R
#?x w ?y w ?z = R

print("a¹¹.x ± a¹².y ± a¹³.z = b¹¹\na²¹.x ± a²².y ± a²³.z = b²¹\na³¹.x ± a³².y ± a³³.z = b³¹")
print("Complete de acordo com a sua equação!")

a11 = float(input("Digite o a11: "))
a12 = float(input("Digite o a12: "))
a13 = float(input("Digite o a13: "))
b11 = float(input("Digite o b11: "))
a21 = float(input("Digite o a21: "))
a22 = float(input("Digite o a22: "))
a23 = float(input("Digite o a23: "))
b21 = float(input("Digite o b21: "))
a31 = float(input("Digite o a31: "))
a32 = float(input("Digite o a32: "))
a33 = float(input("Digite o a33: "))
b31 = float(input("Digite o b31: "))

#Matriz D
print("Matriz D;\n⌈",a11,",",a12,",",a13,"⌉\n|",a21,",",a22,",",a23,"|\n⌊",a31,",",a32,",",a33,"⌋")
d = ((a11*a22*a33)+(a31*a12*a23)+(a21*a32*a13))-((a13*a22*a31)+(a33*a12*a21)+(a23*a32*a11))
print("O valor de D é:",d)

#Matriz Dx
print("Matriz Dx;\n⌈",b11,",",a12,",",a13,"⌉\n|",b21,",",a22,",",a23,"|\n⌊",b31,",",a32,",",a33,"⌋")
dx = ((b11*a22*a33)+(b31*a12*a23)+(b21*a32*a13))-((a13*a22*b31)+(a33*a12*b21)+(a23*a32*b11))
x = dx/d
print("O valor de Dx é:",dx," e o valor de X é:",x)

#Matriz Dy
print("Matriz Dy;\n⌈",a11,",",b11,",",a13,"⌉\n|",a21,",",b21,",",a23,"|\n⌊",a31,",",b31,",",a33,"⌋")
dy = ((a11*b21*a33)+(a31*b11*a23)+(a21*b31*a13))-((a13*b21*a31)+(a33*b11*a21)+(a23*b31*a11))
y = dy/d
print("O valor de Dy é:",dy," e o valor de X é:",y)

#Matriz Dz
print("Matriz Dz;\n⌈",a11,",",a12,",",b11,"⌉\n|",a21,",",a22,",",b21,"|\n⌊",a31,",",a32,",",b31,"⌋")
dy = ((a11*a22*b31)+(a31*a12*b21)+(a21*a32*b11))-((b11*a22*a31)+(b31*a12*a21)+(b21*a32*a11))
y = dy/d
print("O valor de Dy é:",dy," e o valor de X é:",y)
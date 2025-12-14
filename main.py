# main.py
from drawer_logic import adelante, reiniciar
import turtle

# Configuración inicial
turtle.speed(4)           # Velocidad media para ver el dibujo
turtle.shape('turtle')
turtle.color('green')
turtle.pensize(5)         # Líneas gruesas para que se vean bien

print("Dibujando una escalera bonita de 7 peldaños...")

# Mover la tortuga al lado izquierdo para que quepa todo
turtle.penup()
turtle.goto(-300, 200)    # Posición inicial alta e izquierda
turtle.pendown()

# Dibujar escalera: horizontal + bajar vertical + repetir
for _ in range(7):
    adelante(80)          # Peldaño horizontal
    turtle.right(90)      # Girar para bajar
    adelante(40)          # Bajada vertical
    turtle.left(90)       # Volver a dirección horizontal

# Reiniciar para el cuadrado
reiniciar()
turtle.color('blue')
turtle.pensize(6)

print("Posición reiniciada. Dibujando un cuadrado grande...")

# Cuadrado grande en el centro
for _ in range(4):
    adelante(200)
    turtle.right(90)

turtle.done()
# mini_turtle/drawer_logic.py

import turtle

# Variable global para rastrear la posición horizontal
posicion_x = 0

def adelante(distancia: int = 50) -> None:
    """Avanza la tortuga y actualiza la posición horizontal."""
    global posicion_x
    turtle.forward(distancia)
    posicion_x += distancia

def abajo(distancia_y: int = 10) -> None:
    """Baja la tortuga un nivel (simulando una escalera)."""
    global posicion_x
    turtle.penup()
    turtle.backward(posicion_x)      # Volver al inicio de la línea actual
    turtle.left(90)
    turtle.forward(distancia_y)      # Bajar
    turtle.right(90)
    turtle.pendown()
    # No actualizamos posicion_x porque empezamos una nueva línea desde x=0

def reiniciar() -> None:
    """Resetea la posición horizontal a 0 y lleva la tortuga al origen."""
    global posicion_x
    posicion_x = 0
    turtle.penup()
    turtle.home()  # Vuelve a (0,0) y dirección inicial
    turtle.pendown()
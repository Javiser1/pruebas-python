# Ejemplo simple usando Turtle (basado en la documentación común de Turtle)
import turtle
import time
import random

# Configuración de pantalla
wn = turtle.Screen()
wn.title("Juego de la Viborita")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

# ... (se añadiría código para movimiento, comida y colisiones)

# Bucle principal
while True:
    wn.update()
    # ... (lógica del juego)
    time.sleep(0.1)

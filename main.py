import turtle

ventana = turtle.Screen()
ventana.title("Pong - Proyecto 2")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)

# Puntuaciones de los jugadores
puntos_izquierda = 0
puntos_derecha = 0


# Crear marcador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)

marcador.write(
    "Jugador 1: 0    Jugador 2: 0",
    align="center",
    font=("Arial", 18, "normal")
)

# Crear la paleta izquierda
paleta_izquierda = turtle.Turtle()
paleta_izquierda.speed(0)
paleta_izquierda.shape("square")
paleta_izquierda.color("white")
paleta_izquierda.shapesize(stretch_wid=5, stretch_len=1)
paleta_izquierda.penup()
paleta_izquierda.goto(-350, 0)

# Crear la paleta derecha
paleta_derecha = turtle.Turtle()
paleta_derecha.speed(0)
paleta_derecha.shape("square")
paleta_derecha.color("white")
paleta_derecha.shapesize(stretch_wid=5, stretch_len=1)
paleta_derecha.penup()
paleta_derecha.goto(350, 0)


# Movimiento de la paleta izquierda
def paleta_izquierda_arriba():
    y = paleta_izquierda.ycor()
    if y < 250:
        y += 20
        paleta_izquierda.sety(y)

def paleta_izquierda_abajo():
    y = paleta_izquierda.ycor()
    if y > -250:
        y -= 20
        paleta_izquierda.sety(y)

# Movimiento de la paleta derecha
def paleta_derecha_arriba():
    y = paleta_derecha.ycor()
    if y < 250:
        y += 20
        paleta_derecha.sety(y)

def paleta_derecha_abajo():
    y = paleta_derecha.ycor()
    if y > -250:
        y -= 20
        paleta_derecha.sety(y)


# Crear la pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)

# Velocidad de la pelota
pelota.dx = 3
pelota.dy = 3

# Actualizar el marcador
def actualizar_marcador():
    marcador.clear()
    marcador.write(
        f"Jugador 1: {puntos_izquierda}    Jugador 2: {puntos_derecha}",
        align="center",
        font=("Arial", 18, "normal")
    )


# Controles del teclado
ventana.listen()
ventana.onkeypress(paleta_izquierda_arriba, "w")
ventana.onkeypress(paleta_izquierda_abajo, "s")

ventana.onkeypress(paleta_derecha_arriba, "Up")
ventana.onkeypress(paleta_derecha_abajo, "Down")


# Bucle principal del juego
def actualizar_juego():
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)
    
    # Rebote en el borde superior
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1

    # Rebote en el borde inferior
    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1

    # Colisión con la paleta derecha
    if (pelota.dx > 0 and
        330 < pelota.xcor() < 350 and
        abs(pelota.ycor() - paleta_derecha.ycor()) < 60):
        pelota.setx(330)
        pelota.dx *= -1

    # Colisión con la paleta izquierda
    if (pelota.dx < 0 and
        -350 < pelota.xcor() < -330 and
        abs(pelota.ycor() - paleta_izquierda.ycor()) < 60):
        pelota.setx(-330)
        pelota.dx *= -1


    # Permitir modificar las puntuaciones globales
    global puntos_izquierda, puntos_derecha

    # La pelota sale por la derecha
    if pelota.xcor() > 390:
        puntos_izquierda += 1
        pelota.goto(0, 0)
        pelota.dx = -3
        pelota.dy = 3
        actualizar_marcador()

    # La pelota sale por la izquierda
    if pelota.xcor() < -390:
        puntos_derecha += 1
        pelota.goto(0, 0)
        pelota.dx = 3
        pelota.dy = 3
        actualizar_marcador()


    ventana.ontimer(actualizar_juego, 10)

actualizar_juego()

ventana.mainloop()

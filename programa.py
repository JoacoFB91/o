import os

class Pregunta:
    def __init__(self, texto, opciones):
        self.texto = texto
        self.opciones = opciones

class Cuestionario:
    def __init__(self):
        self.preguntas = []
        self.respuestas = {'a': 0, 'b': 0, 'c': 0}
        self.definir_preguntas()
        self.mostrar_intro()

    def mostrar_intro(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
        print(r"""
         /\     /\
        {  `---'  }
        {  O   O  }
        ~~>  V  <~~
         \ \|/ /
          `-----'____
          /     \    \_
         {       }\  )_ \
         |  \_/  ) / / /
          \__/  /(_/ /
            (__/
        """)
        print("¡Bienvenido al cuestionario! Descubre qué tipo de gato eres.\n")

    def definir_preguntas(self):
        self.preguntas = [
            Pregunta("¿Cómo prefieres pasar tu tiempo libre?", ["a) Jugando con otros.", "b) Durmiendo.", "c) Explorando."]),
            Pregunta("¿Cuál es tu comida favorita?", ["a) Pescado.", "b) Pollo.", "c) Verduras."]),
            Pregunta("¿Cómo reaccionas ante los cambios?", ["a) Con entusiasmo.", "b) Con calma.", "c) Con curiosidad."]),
            Pregunta("¿Qué tipo de compañía prefieres?", ["a) Muchos amigos.", "b) Solo unos pocos.", "c) Me gusta estar solo."]),
            Pregunta("¿Cómo describirías tu energía?", ["a) Muy alta.", "b) Moderada.", "c) Baja."]),
            Pregunta("¿Cuál es tu lugar favorito para descansar?", ["a) Un lugar soleado.", "b) En una caja.", "c) En una ventana."]),
            Pregunta("¿Cómo manejas el estrés?", ["a) Haciendo ejercicio.", "b) Durmiendo.", "c) Reflexionando."]),
            Pregunta("¿Te gustan las sorpresas?", ["a) Sí, me encantan.", "b) Prefiero la rutina.", "c) A veces."]),
            Pregunta("¿Cómo te sientes en multitudes?", ["a) Energizado.", "b) Cansado.", "c) Indiferente."]),
            Pregunta("¿Qué actividad disfrutas más?", ["a) Jugar al aire libre.", "b) Ver una película.", "c) Leer un libro."]),
            Pregunta("¿Cuál es tu estado de ánimo más común?", ["a) Alegre.", "b) Tranquilo.", "c) Pensativo."]),
            Pregunta("¿Qué tan sociable eres?", ["a) Muy sociable.", "b) Algo sociable.", "c) No muy sociable."]),
        ]

    def hacer_preguntas(self):
        for pregunta in self.preguntas:
            print(pregunta.texto)
            for opcion in pregunta.opciones:
                print(opcion)
            respuesta = input("Tu respuesta (a/b/c): ").strip().lower()
            if respuesta in self.respuestas:
                self.respuestas[respuesta] += 1

    def determinar_tipo_gato(self):
        tipo_gato = max(self.respuestas, key=self.respuestas.get)

        # Tipos de gatos
        if tipo_gato == 'a':
            return "Gato aventurero"
        elif tipo_gato == 'b':
            return "Gato relajado"
        elif tipo_gato == 'c':
            return "Gato curioso"
        elif self.respuestas['a'] > self.respuestas['b'] and self.respuestas['a'] > self.respuestas['c']:
            return "Gato juguetón"
        elif self.respuestas['b'] > self.respuestas['a'] and self.respuestas['b'] > self.respuestas['c']:
            return "Gato perezoso"
        elif self.respuestas['c'] > self.respuestas['a'] and self.respuestas['c'] > self.respuestas['b']:
            return "Gato filósofo"
        elif self.respuestas['a'] > self.respuestas['b'] and self.respuestas['b'] > self.respuestas['c']:
            return "Gato extrovertido"
        elif self.respuestas['c'] > self.respuestas['a'] and self.respuestas['a'] > self.respuestas['b']:
            return "Gato pensador"
        elif self.respuestas['a'] > self.respuestas['c'] and self.respuestas['b'] > self.respuestas['c']:
            return "Gato activo"
        elif self.respuestas['b'] > self.respuestas['c'] and self.respuestas['c'] > self.respuestas['a']:
            return "Gato de sofá"
        elif self.respuestas['a'] == self.respuestas['b']:
            return "Gato equilibrado"
        else:
            return "Gato misterioso"

    def mostrar_resultado(self, gato):
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
        print(r"""
         /\     /\
        {  `---'  }
        {  O   O  }
        ~~>  V  <~~
         \ \|/ /
          `-----'____
          /     \    \_
         {       }\  )_ \
         |  \_/  ) / / /
          \__/  /(_/ /
            (__/
        """)
        print(f"\n¡Eres un {gato}!\n")

    def ejecutar(self):
        self.hacer_preguntas()
        gato = self.determinar_tipo_gato()
        self.mostrar_resultado(gato)

# Ejecutar el cuestionario
cuestionario = Cuestionario()
cuestionario.ejecutar()

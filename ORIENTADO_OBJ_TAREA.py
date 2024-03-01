class Equipo:
    def __init__(self, nombre, integrante1, integrante2, integrante3, eslogan=""):
    #Se inicializan los atributos de cada equipo
        self.nombre = nombre
        self.integrantes = [integrante1, integrante2]
        if integrante3:
            self.integrantes.append(integrante3)
        self.eslogan = eslogan

    def __str__(self):
        integrantes_str = "\n".join(self.integrantes)
        if len(self.integrantes) < 3:
            integrantes_str += "\n--------------------"
        return f"{self.nombre}\nEslogan: {self.eslogan}\n{integrantes_str}\n"

class FS3:
    def __init__(self):
        #Inicializa la lista de equipos.
        self.equipos = []

    def agregar_equipo(self, equipo):
        #Método para agregar un equipo a la lista de equipos de FS3.

        self.equipos.append(equipo) 

    def __str__(self):
        # Método para convertir objeto a string de FS3.
        return '\n'.join(str(equipo) for equipo in self.equipos)

# Creación de los equipos
fs3 = FS3()

# Declaración de los nombres de equipo, integrantes y eslogans
equipos_info = [
    ("Los =^UwU^=", ["Leonardo Alberto Gonzáles Carmona", "Norma Graciela Mendoza Ruiz", "Jonathan Durán Mendoza"], 
     "Respiración de Programación, Pose de HTML, Codificar"),
    ("Toyota Legacy", ["Israel Chacon Rojo", "Dilan Mauricio Garcia Hernandez", "Jesus Elias Sierra Ruiz"],
     "Transformamos líneas de código en experiencias excepcionales."),
    ("Pingüinos Galácticos", ["Yahir Antonio Monje Ochoa", "Yesica Cristina Rodriguez Renteria"], "SIC•PARVIS•MAGNA"),
    ("Los 3 Mosqueteros", ["Dania Denisse Benavides Figueroa", "Erick Lozano Duarte", "Ana Cristina Valenzuela Ruiz"],
     "Todos para uno, uno para todos"),
    ("WebHeros", ["Jesus Manuel Arellano Merendon", "Axel Felipe Reyes Valadez", "Luis Daniel Delgado Enriquez"],
     "La verdad solo se puede encontrar en un lugar: el codigo"),
    ("Los Polystation", ["Erick Fernando Siqueiros Zúñiga", "Paulina Ixchel Arreguin Ruiz"], 
     "Conectando el futuro, hoy")
]

# Creamos y agregamos a los equipos a FS3
for nombre, integrantes, eslogan in equipos_info:
    equipo = Equipo(nombre, *integrantes, eslogan)
    fs3.agregar_equipo(equipo)

# Imprimir FS3
print(fs3)

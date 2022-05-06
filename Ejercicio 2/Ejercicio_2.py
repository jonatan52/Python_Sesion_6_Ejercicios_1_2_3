# Ejercicio 2
# Enunciado del ejercicio:
# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. 
# Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.




class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return f"Nombre: {self.nombre}, Nota: {self.nota}"

    def aprobado(self):
        if self.nota >= 5:
            return f"{self.nombre} ha aprobado"
        else:
            return f"{self.nombre} ha reprobado"


alumno = Alumno("Juan", 6)
print(alumno)
print(alumno.aprobado())
print()

alumno_2 = Alumno("Pedro", 4)
print(alumno_2)
print(alumno_2.aprobado())

      

    


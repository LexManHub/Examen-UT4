from abc import ABC, abstractmethod

# Clase abstracta para representar una receta
class Recetas(ABC):
    def __init__(self, n, i, p):
        self.n = n  # nombre
        self.i = i  # ingredientes
        self.p = p  # pasos


class Mostrar_Receta(Recetas):
    def lista_recetas():
        nombre = input("Nombre de la receta: ")
        ingredientes = []
        print("Introduce los ingredientes (escribe 'fin' para terminar): ")
        while True:
            ing = input("- ")
            if ing.lower() == "fin":
                break
            ingredientes.append(ing)
        pasos = []
        print("Introduce los pasos(escribe fin para terminar): ")
        while True:
            dato = input ("- ")
            if dato.lower() == "fin":
                break
            pasos.append(dato)

        Recetas(nombre,ingredientes,pasos)



# Clase para recetas vegetarianas
class Recetas_Vegetarianas(Recetas):
    def __init__(self, n, i, p, vegetariana):
        super().__init__(n, i, p)
        self.vegetariana = vegetariana


# Clase para recetas no vegetarianas
class Receta_no_vegetarianas(Recetas):
    def __init__(self, n, i, p , carnivora):
        super().__init__(n, i, p)
        self.carnivora = carnivora


        


# Función principal
def principal():
    Mostrar_Receta.lista_recetas()

    tipo = input("¿Que tipo de receta quieres crear?").lower()
    if tipo == "vegetariana":
        print("== Crear receta 1 vegetariana ==")
        apta_para_vegana = input("Indica si es apta para veganos: ")
        r1 = Recetas_Vegetarianas(Recetas.n,Recetas.i,Recetas.p,apta_para_vegana)
    elif tipo == "carnivora":
        print("== Crear receta 1 vegetariana ==")
        apta_para_carnivora = input("Introduce el tipo de carne")
        r2 = Receta_no_vegetarianas(Recetas.n,Recetas.i,Recetas.p,apta_para_carnivora)
    else:
        print("El tipo de receta inficado no es el correcto")

    
    #mostrar recetas
    print(r1,r2)

# Ejecutar el programa
if __name__ == "__main__":
    principal()

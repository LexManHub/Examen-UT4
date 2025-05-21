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

        return nombre,ingredientes,pasos



# Clase para recetas vegetarianas
class Recetas_Vegetarianas(Recetas):
    print(f"Receta vegetariana: {Recetas.n}")
    print(f"Ingredientes: {Mostrar_Receta.lista_recetas()}")


# Clase para recetas no vegetarianas
class Receta_no_vegetarianas(Recetas):
    print(f"Receta NO vegetariana: {Recetas.n}")
    print(f"Ingredientes: {Mostrar_Receta.lista_recetas()}")

  
        




# Clase con utilidades del restaurante
class Utilidades_Restaurante:
    @staticmethod
    def imprimir_receta(r):
        print("====================================")
        r.mostrar()
        print("====================================")

    @staticmethod
    def mostrar_lista_ingredientes(lista):
        for l in lista:
            print(f"* {l}")

# Función principal
def principal():


    # Código duplicado para mostrar ingredientes
    print("Ingredientes de Ensalada César:")
    for ing in r1.i:
        print(f"* {ing}")
    
    print("Ingredientes de Pollo al horno:")
    for ing in r2.i:
        print(f"* {ing}")


# Ejecutar el programa
if __name__ == "__main__":
    principal()

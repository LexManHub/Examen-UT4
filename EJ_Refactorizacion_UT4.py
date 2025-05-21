from abc import ABC, abstractmethod

# Clase abstracta para representar una receta
class Recetas(ABC):
    def __init__(self, n, i, p):
        self.n = n  # nombre
        self.i = i  # ingredientes
        self.p = p  # pasos


class Mostrar_Receta(Recetas):
    def lista_recetas():
        for ing in Recetas.i:
            print(f"- {ing}")
        print("Pasos:")
        for paso in Recetas.p:
            print(f"{paso}")



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
    r1 = Recetas_Vegetarianas("Ensalada César", ["lechuga", "queso", "pan tostado", "salsa"], ["Lavar", "Mezclar", "Servir"])
    r2 = Receta_no_vegetarianas("Pollo al horno", ["pollo", "patatas", "ajo", "aceite"], ["Preparar", "Hornear", "Servir"])
    
    # Duplicación de código al imprimir
    print("== Mostrar recetas ==")
    Utilidades_Restaurante.imprimir_receta(r1)
    Utilidades_Restaurante.imprimir_receta(r2)

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

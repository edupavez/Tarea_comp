from os.path import join


class RegresionCuad:

    def __init__(self, ruta):
        self.ruta = ruta
        self.puntos = list()
        self.cargar_datos()

    def cargar_datos(self):
        with open(self.ruta, "r") as archivo:
            contenido = archivo.readlines()[1:]
            for linea in contenido:
                linea = linea.rstrip("\n")
                linea = linea.split(",")
                x = float(linea[0])
                y = float(linea[1])
                self.puntos.append((x,y))
        print(self.puntos)
    
    def calcular_coeficientes(self):
        pass

    
    def modulo(self, vector):
        #calculo de modulo en base a la norma 2
        suma_coeficientes = 0
        for coeficiente in vector:
            suma_coeficientes += coeficiente ** 2
        modulo = suma_coeficientes ** 0.5
        return modulo
        
        
ruta_1 = join("P1grupo_8.csv")

if __name__ == "__main__":
    calc_reg = RegresionCuad(ruta_1)
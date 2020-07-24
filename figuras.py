# Herencia: es la posibilidad de compartir atributos y métodos
# entre clases. Y que en diferenctes clases heredan

class Figura:

    # Atributos o propiedades de la clase figura
    tipo_figura = "Triangulos"

    # constructor
    def __init__(self, tipo_figura):
        self.tipo_figura = tipo_figura

    # metodos
    def setTipo(self, tipo_figura):
        self.tipo_figura = tipo_figura

    def getTipo(self):
        return self.tipo_figura

class Triangulo(Figura):

    # Atributos o propiedades de la clase Triangulo
    nombre_tri = "Triangulo"
    vertices = 3
    lados_1 = 3
    angulos_1 = 3
    tamano_ang_1 = 90

    # Constructor
    def __init__(self, tipo_figura, nombre_tri, vertices_1, lados_1, angulos_1, tamano_ang_1):
        super().__init__(tipo_figura)
        self.tipo_figura = tipo_figura
        self.nombre_tri = nombre_tri
        self.lados_1 = lados_1
        self.angulos_1 = angulos_1
        self.tamano_ang_1 = tamano_ang_1

    # Metodos
    def setNombreTri(self, nombre_tri):
        self.nombre_tri = nombre_tri

    def getNombreTri(self):
        return self.nombre_tri
    
    def setLados(self, lados_1):
        self.lados_1 = lados_1

    def getLadosTri(self):
        return self.lados_1

    def setAngulosTri(self, angulos_1):
        self.angulos_1 = angulos_1

    def getAngulostri(self):
        return self.angulos_1

    def setTamano_angTri(self, tamano_ang_1):
        self.tamano_ang_1 = tamano_ang_1                    
    
    def getTamano_angTri(self):
        return self.tamano_ang_1

class Cuadrilatero(Figura):

    # Atributos
    nombre_cua = "Cuadrado"
    vertices_2 = 4
    lados_2 = 4
    angulos_2 = 4
    tamano_ang_2 = 90

    # constructor
    def __init__(self, tipo_figura, nombre_cua, vertices_2, lados_2, angulos_2, tamano_ang_2):
        super().__init__(tipo_figura)
        self.nombre_cua = nombre_cua
        self.vertices_2 = vertices_2
        self.lados_2 = lados_2
        self.angulos_2 = angulos_2
        self.tamano_ang_2 = tamano_ang_2

    # metodos
    def setNombreCua(self, nombre_cua):
        self.nombre_cua = nombre_cua

    def getNombreCua(self):
        return self.nombre_cua

    def setverticeCua(self, vertices_2):
        self.vertices_2 = vertices_2

    def getverticeCua(self):
        return self.vertices_2

    def setladoCua(self, lados_2):
        self.lados_2 = lados_2

    def getladoCua(self):
        return self.lados_2

    def setTamanoAngCua(self, tamano_ang_2):
        self.tamano_ang_2 = tamano_ang_2

    def getTamanoAngCua(self):
        return self.tamano_ang_2

        
                    
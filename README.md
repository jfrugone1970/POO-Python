# POO-Python
Programación Orientada a Objetos en Python

Mediante esta instroducción vamos a definir primero lo que es la programación Orientada a Objetos en Python: 
Clases.- Las clases proporcionan un medio de agrupar datos y funcionalidad juntos. La creación de una nueva clase crea un nuevo tipo de objeto, lo que permite crear nuevas instancias de ese tipo. Cada instancia de clase puede tener atributos adjuntos para mantener su estado. Las instancias de clase también pueden tener métodos (definidos por su clase) para modificar su estado.

En comparación con otros lenguajes de programación, el mecanismo de clase de Python agrega clases con un mínimo de sintaxis y semántica nuevas. Es una mezcla de los mecanismos de clase que se encuentran en C ++ y Modula-3. Las clases de Python proporcionan todas las características estándar de la programación orientada a objetos: el mecanismo de herencia de clases permite múltiples clases base, una clase derivada puede anular cualquier método de su clase o clases base, y un método puede llamar al método de una clase base con el mismo nombre . Los objetos pueden contener cantidades arbitrarias y tipos de datos. Como sucede con los módulos, las clases participan de la naturaleza dinámica de Python: se crean en tiempo de ejecución y se pueden modificar aún más después de la creación.

Definición de una clase:
La forma más simple de definir una clase es así:

class ClasName:
    <statement-1>
      .
      .
      .
    <statement-2>
Las definiciones de clase, como las definiciones de función ( defdeclaraciones) deben ejecutarse antes de que tengan algún efecto. (Posiblemente podría colocar una definición de clase en una rama de una ifdeclaración o dentro de una función).
      
Cuando se ingresa una definición de clase, se crea un nuevo espacio de nombres y se usa como el ámbito local; por lo tanto, todas las asignaciones a variables locales entran en este nuevo espacio de nombres. En particular, las definiciones de función enlazan el nombre de la nueva función aquí.

Cuando una definición de clase se deja normalmente (hasta el final), se crea un objeto de clase .

La instanciación de clase utiliza la notación de función. Simplemente imagine que el objeto de clase es una función sin parámetros que devuelve una nueva instancia de la clase. Por ejemplo (suponiendo la clase anterior):

x = MyClass()
crea una nueva instancia de la clase y asigna este objeto a la variable local x.


La operación de creación de instancias ("llamar" a un objeto de clase) crea un objeto vacío. A muchas clases les gusta crear objetos con instancias personalizadas para un estado inicial específico. Por lo tanto, una clase puede definir un método especial llamado __init__(), como este:

def __init__(self):
    self.data = []
Cuando una clase define un __init__()método, la instanciación de clase se invoca automáticamente __init__()para la instancia de clase recién creada. Entonces, en este ejemplo, se puede obtener una nueva instancia inicializada:

x = MyClass()
Por supuesto, el __init__()método puede tener argumentos para una mayor flexibilidad. En ese caso, los argumentos dados al operador de instanciación de clase se pasan a __init__(). Por ejemplo,

>>>
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)

Para este presente ejercicio vamos hablar de herencia que definimos primero lo que es una herencia:
Herencia.- Es la posibilidad de compartir atributos o propiedades y métodos entre clases, que también podemos decir que la sintáxis para definir una herencia es la siguiente:

class DerivedClassName(BaseClassName):
     <statement-1>
       .
       .
       .
     <statement-2>
       
Ejemplo:
class Triangulo(Figura):
     # Atributos o propiedades
     lado = 3
     vertice = 3
     angulo = 90
     
     # metodos
     
     def setLado(self, lado):
         self.lado = lado
         
     def getLado(self):
         return self.lado
         
     def setVertice(self, vertice):
         self.vertice = vertice
         
     def getVertice(self):
         return self.vertice
         
     def setAngulo(self, angulo):
         self.angulo = angulo
         
     def getAngulo(self):
         return self.angulo
         
Para este ejercicio vamos a definir una clase padre que se llama Figura, y dos Clases que heredan de la clase Figura que es Cuadrilatero y Triangulo, que toman los atributos, propiedades y/o métodos de la clase Figura y para cada uno de ellos sus propias atributos y métodos adicionales.







      

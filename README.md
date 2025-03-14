# poo_python

- El paradigma de POO está basado en una abstracción del mundo que nos va a permitir desarrollar programas de forma más cercana a como vemos el mundo,pensando en objetos que tenemos delante y en acciones que podemos hecer con ellos.

## Clase

- Una clase es un tipo de datos cuyas variables se llaman objetos o instancias.
- La clase es la definición del concepto del mundo real y los objetos o instancias son el propio objeto del mundo real.
- Las clases estan compuestas por dos elementos: atributos y métodos

### atributos

- Información que almecena la clase

### Métodos

- Operaciones que pueden ralizar las clases

## definición de una clase en Python
```Python
class NombreClase:

    def __init__(self, variable1, valiable2):
        self.Atributo1 = valor1
        self.Atributo2 = valor2

    def nombreMetodo(self):
        bloqueCodigo
```

### Componentes

```class```: palabra reservada en Python para definir una clase.

```NombreClase```: nombre de la clase que quieres crear.

```def```: palabra reservada en Python que se utiliza para definir tanto el constructor de la clase (metodo que se ejecuta la primera vez que usas una clase) como los diferentes metodos que tiene

```__init__```: palabre reservada en Python para definir el método constructor de la clase. Es lo primero que se ejecuta cuando creas el objeto de una clase.

```(self, variable x)```: parametro del constructor de la clase. El parametro self es obligatorio y despues puedes tener tantos parametros como quieras. La forma de añadir parametros es la misma que en las funciones.

```self.AtributoX```: forma de utilizacion y acceso a los atributos de la clase.

```nombreMetodo```: nombre del metodo de la clase.

```(self)```: parámetro del método. El parámetro self es obligatorio y despues puedes tener varios parametros coo quieras.

```bloqueCodigo```: instrucciones que ejecutara el método.

- Cuando defines una clase debes tener en cuenta los siguientes puntos:
    - Puedes definir tantos atribitos como necesites
    - Puedes ddefinir tantos métodos como necesites
    - Puedes definir tantos parametros en el constructor y en los metodos como necesites.

## Composición

- Consiste en la creación de nuevas clases a partir de otras clases ya existentes que actuan como elementos compositores de la nueva

- Las clasess existentes seran atributo de a nueva clase

- En POO la composición significa que entre las dos clases existe una relación de tipo "tiene un"

- Ejemplo:
    - Una coordenada en dos dimenciones esta compuesta por dos valores, el valor en el eje de las x y el valor en el eje de la y, esto podria ser una clase. Un cuadrado esta compuesto por cuatro coordenadas que son los cuatro vertices, esto podria ser una clase que esta compuesta por cuatro clases del objeto coordenada.

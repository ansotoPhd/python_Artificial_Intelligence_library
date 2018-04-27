El primer paso para solucionar un problema es la formulación del objetivo, 
    - basado en la situación actual y 
    - la medida de rendimiento del agente.

Consideraremos un objetivo como un conjunto de estados del mundo (exactamente
aquellos estados que satisfacen el objetivo). 

La tarea del agente es encontrar qué secuencia de acciones permite obtener un estado objetivo. 

Para esto, necesitamos decidir qué 
    - acciones
    - y estados considerar.

Este proceso de hallar esta secuencia se llama búsqueda. Un algoritmo de búsqueda
toma como entrada un problema y devuelve una solución de la forma secuencia de
acciones. Una vez que encontramos una solución, se procede a ejecutar las acciones que
ésta recomienda. Esta es la llamada fase de ejecución

supone que el entorno es estático
  formulación y búsqueda se hace sin prestar atención a cualquier cambio que en el entorno. 
el entorno es observable --> agente supone que se conoce el estado inicial;
el entorno puede verse como discreto. Finalmente,
y más importante, el agente diseñado supone que el entorno es determinista.
Las soluciones a los problemas son simples secuencias de acciones, así que no pueden
manejar ningún acontecimiento inesperado;


Un problema puede definirse, formalmente, por cuatro componentes:

• El estado inicial en el que comienza el agente. 

• Una descripción de las posibles acciones disponibles por el agente. La formulación
más común utiliza una función sucesor. Dado un estado particular x, SUCESOR-
FN(x) devuelve un conjunto de pares ordenados <acción, sucesor>, donde cada
acción es una de las acciones legales en el estado x y cada sucesor es un estado
que puede alcanzarse desde x, aplicando la acción. 

Implícitamente el estado inicial y la función sucesor definen el espacio de estados
del problema (el conjunto de todos los estados alcanzables desde el estado inicial).
El espacio de estados forma un grafo en el cual los nodos son estados y los
arcos entre los nodos son acciones. 

 Un camino en el espacio de estados es una secuencia de estados conectados por una secuencia
de acciones.

• El test objetivo, el cual determina si un estado es un estado objetivo. Algunas veces
existe un conjunto explícito de posibles estados objetivo, y el test simplemente
comprueba si el estado es uno de ellos.

• Una función costo del camino que asigna un costo numérico a cada camino. El
agente resolvente de problemas elige una función costo que refleje nuestra medida
de rendimiento. 
 suponemos que el costo del camino puede describirse como la suma
de los costos de las acciones individuales a lo largo del camino. El costo individual
de una acción a que va desde un estado x al estado y se denota por c(x,a,y).

Los elementos anteriores definen un problema y pueden unirse en una estructura de datos
simple que se dará como entrada al algoritmo resolvente del problema. Una solución
de un problema es un camino desde el estado inicial a un estado objetivo. La calidad de
la solución se mide por la función costo del camino, y una solución óptima tiene el costo
más pequeño del camino entre todas las soluciones.

técnicas de búsqueda que utilizan un árbol de búsqueda explícito generado por el estado inicial y la
función sucesor, definiendo así el espacio de estados. 

En general, podemos tener un grafo de búsqueda más que un árbol, cuando el mismo estado puede alcanzarse desde varios
caminos.

La raíz del árbol de búsqueda es el nodo de búsqueda que corresponde al estado inicial.
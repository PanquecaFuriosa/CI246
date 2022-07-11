class nodo:
    """ Clase que implementa los nodos de un árbol.
    """
    def __init__(self, valor, a, b, c):
        """Inicialización de un nodo.

        Args:
            valor (str): Contiene el valor del nodo, 
            ya sea una constante booleana o un operador.
            a (nodo): Hijo izquierdo del nodo.
            b (nodo): Hijo derecho del nodo.
            c (nodo): Padre del nodo.
        """
        self.valor = valor
        self.hijoI = a
        self.hijoD = b
        self.padre = c

def con(c1, c2) -> str:
    """Función que implementa la conjunción lógica

    Args:
        c1 (str): Una de las constantes a evaluar.
        c2 (str): Otra de las constantes a evaluar.

    Returns:
        str: Constante booleana resultante.
    """
    if c1 == "false" or c2 == "false":
        return "false"
    return "true"

def dis(c1, c2) -> str:
    """Función que implementa la disyunción lógica

    Args:
        c1 (str): Una de las constantes a evaluar.
        c2 (str): Otra de las constantes a evaluar.

    Returns:
        str: Constante booleana resultante.
    """
    if c1 == "true" or c2 == "true":
        return "true"
    return "false"

def imp(c1, c2) -> str:
    """Función que implementa la implicación lógica

    Args:
        c1 (str): Constante a evaluar (implica).
        c2 (str): Otra de las constantes a evaluar (implicado).

    Returns:
        str: Constante booleana resultante.
    """
    if c1 == "false":
        return "true"
    if c2 == "true":
        return "true"
    return "false"

def neg(c1) -> str:
    """Función que implementa la negación lógica

    Args:
        c1 (str): Constante a evaluar.

    Returns:
        str: Constante booleana resultante.
    """
    if c1 == "true":
        return "false"
    return "true"

def crea_arbol(expresion, ord) -> nodo:
    """Función que creal el árbol de operaciones.

    Args:
        expresion (list): Lista de la expresión booleana completa.
        ord (str): Orden a evaluar la expresión (PRE o POST).

    Returns:
        nodo: Es el nodo raíz del árbol resultante.
    """
    if ord == "PRE":
        expresion = list(reversed(expresion)) #Se lee la expresión al revés, para post sirve la lectura normal pero es necesario invertir la expresión para pre
    elem = [] # Pila de elementos
    i = 0
    a = 0
    b = 0
    while i != len(expresion):
        if expresion[i].lower() != "false" and expresion[i].lower() != "true": #Si el valor actual es un operador, debe agarrar dos elementos de la pila como hijos
            if expresion[i] != "^":
                a = elem.pop()
                b = elem.pop()  
                if (ord == "POST"):
                    elem.append(nodo(expresion[i], b, a, None))
                else:
                    elem.append(nodo(expresion[i], a, b, None))
                b.padre = elem[len(elem)-1]
            else:
                a = elem.pop()
                elem.append(nodo(expresion[i], a, None, None))
            a.padre = elem[len(elem)-1]
        else:
            elem.append(nodo(expresion[i].lower(), None, None, None)) #Si el valor es una constante, es empilado
        i += 1
    return elem[0]

def eval(actual) -> nodo:
    """Función recursiva que evalua la expresión de un árbol binario.
    Se evalua con las dos constantes hijas y el operador del nodo actual,
    si los hijos son operadores, se evaluan los operadores hijos primero.

    Args:
        actual (nodo): Es el nodo raíz del árbol, es el operador padre.

    Returns:
        nodo: Contiene el valor resultante de la evaluación.
    """
    a = actual.hijoI
    b = actual.hijoD
    if a == None and b == None:
        return actual
    if a != None and b == None:
        return nodo(neg(eval(a).valor), None, None, actual)
    if actual.valor == "&":
        return nodo(con(eval(a).valor, eval(b).valor), None, None, actual)
    if actual.valor == "|":
        return nodo(dis(eval(a).valor, eval(b).valor), None, None, actual)
    return nodo(imp(eval(a).valor, eval(b).valor), None, None, actual)

def mostrar(actual) -> str:
    """Función recursiva que muestra la expresión booleana infinja dado
    un orden pre o postfijo.Se muestran primero los elementos del último
    nivel del árbol hasta llegar al más alto nivel.

    Args:
        actual (nodo): Es el nodo raíz del árbol, es el operador padre.

    Returns:
        nodo: Contiene la expresión infija a partir de la dada en otro orden.
    """
    a = actual.hijoI
    b = actual.hijoD
    if a == None and b == None:
        return actual.valor
    if a != None and b == None:
        return actual.valor+" "+mostrar(a)
    if actual.padre != None and ((actual.padre.valor == "&" and actual.valor !="&") or (actual.padre.valor == "|" and actual.valor !="|")):
        if actual.valor == "=>" or actual.padre.hijoD == actual:
            return "("+mostrar(a)+" "+actual.valor+" "+mostrar(b)+")"
    return mostrar(a)+" "+actual.valor+" "+mostrar(b)
    

def main():
    while True:
        opcion = input("Por favor, elija una opción: 'EVAL' 'MOSTRAR' 'SALIR':\n")
        opcion = opcion.split()
        if opcion[0] == "EVAL":
            print(eval(crea_arbol(opcion[2:], opcion[1])).valor)
        elif opcion[0] == "MOSTRAR":
            print(mostrar(crea_arbol(opcion[2:], opcion[1])))
        elif opcion[0] == "SALIR":
            break
        else: 
            print("La opción indicada no es válida.")

if __name__ == '__main__':
    main()
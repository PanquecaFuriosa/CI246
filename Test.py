from ManejadorDeExpresiones import crea_arbol, mostrar, eval, nodo

def test():
    """Test para probras el manejador de expresiones.
    """
    # Se hacen las evaluaciones del ejemplo del enunciado
    assert eval(crea_arbol(["|", "&", "=>", "true", "true", "false", "true"], "PRE")).valor == "true"
    assert eval(crea_arbol(["true", "false", "=>", "false", "|", "true", "false", "^", "|", "&"], "POST")).valor == "false"

    assert mostrar(crea_arbol(["|", "&", "=>", "true", "true", "false", "true"], "PRE")) == "(true => true) & false | true"
    assert mostrar(crea_arbol(["true", "false", "=>", "false", "|", "true", "false", "^", "|", "&"], "POST")) == "(true => false) | false & (true | ^ false)"
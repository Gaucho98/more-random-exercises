def recetasPosibles(ingredientes, recetas):
    lista = []
    
    for receta, ingrediente in recetas.items():
        if ingrediente <= ingredientes:
            lista.append(receta)
            
    return lista

def ingredientesFaltantes(ingredientes, recetas):
    ingredientes_faltantes = {}
    
    for receta, ingrediente in recetas.items():
        ingredientes_faltantes[receta] = list(ingrediente - ingredientes)
    
    return ingredientes_faltantes

def main():
    ingredientes = {"huevo", "aceite", "papas"}
    recetas = {
        "Papas fritas" : { "aceite", "papas" },
        "Huevo frito" : { "huevo", "aceite" },
        "Pure de papas" : { "papas", "manteca" }
        }
    comidas = recetasPosibles(ingredientes, recetas)
    print(comidas)
    ingredientes_faltantes = ingredientesFaltantes(ingredientes, recetas)
    print(ingredientes_faltantes)
    
main()
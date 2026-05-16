from afinn import Afinn
import pandas as pd

# Inicializamos el analizador de léxico en inglés
afn = Afinn(language='en')

def clasificar_por_lexico(texto):
    """
    Evalúa el sentimiento de un texto usando el léxico AFINN.
    Retorna Positivo, Negativo o Neutral basado en el score.
    """
    if not isinstance(texto, str) or texto.strip() == "":
        return 'Neutral'
        
    # El método score() internamente tokeniza y suma los valores del texto
    score = afn.score(texto)
    
    if score > 0:
        return 'Positivo'
    elif score < 0:
        return 'Negativo'
    else:
        return 'Neutral'

def aplicar_analisis_sentimiento(df, columna_texto):
    """
    Aplica el motor de léxico al DataFrame completo.
    """
    df_resultados = df.copy()
    
    # Aplicamos la clasificación
    df_resultados['sentimiento_predicho'] = df_resultados[columna_texto].apply(clasificar_por_lexico)
    
    # guardamos resultados para análisis posterior
    df_resultados.to_csv('./data/facebook_reviews_resultados_analisis_sentimiento.csv', index=False)

    return df_resultados
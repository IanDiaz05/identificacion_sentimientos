import re
import string
import pandas as pd
from langdetect import detect, DetectorFactory

# Semilla para que la detección de idioma sea consistente en cada ejecución
DetectorFactory.seed = 0

def es_ingles(texto):
    """
    Intenta detectar el idioma del texto. Falla silenciosamente en textos vacíos o puros números.
    """
    try:
        return detect(texto) == 'en'
    except:
        return False

def limpiar_texto_robusto(texto):
    """
    Aplica limpieza estricta y fuerza la codificación ASCII para eliminar ruido visual.
    """
    if not isinstance(texto, str):
        return ""
    
    # Forzar ASCII: ignora cualquier caracter que no sea estándar (elimina emojis y símbolos raros)
    texto = texto.encode('ascii', 'ignore').decode('ascii')
    
    texto = texto.lower()
    
    # Eliminar URLs, menciones y números
    texto = re.sub(r'http\S+|www\S+|https\S+', '', texto, flags=re.MULTILINE)
    texto = re.sub(r'\@\w+|\#', '', texto)
    texto = re.sub(r'\d+', '', texto)
    
    # Tratamiento de exageraciones (convierte "baaaad" en "bad")
    texto = re.sub(r'(.)\1{2,}', r'\1', texto)
    
    # Eliminar signos de puntuación
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    
    # Eliminar espacios extra
    texto = re.sub(r'\s+', ' ', texto).strip()
    
    return texto

def procesar_corpus(df, columna_texto):
    """
    Pipeline completo: Filtrado de idioma, limpieza estricta y eliminación de textos cortos.
    """
    df_procesado = df.copy()
    
    # 1. Conservar solo registros en inglés
    df_procesado['is_en'] = df_procesado[columna_texto].apply(es_ingles)
    df_procesado = df_procesado[df_procesado['is_en']].drop(columns=['is_en'])
    
    # 2. Aplicar limpieza
    df_procesado['texto_limpio'] = df_procesado[columna_texto].apply(limpiar_texto_robusto)
    
    # 3. Eliminar reseñas vacías o muy cortas (ej. un solo nombre propio o una letra)
    # Conservamos textos de al menos 3 palabras para garantizar contexto semántico
    df_procesado = df_procesado[df_procesado['texto_limpio'].str.split().str.len() >= 3]
    
    return df_procesado
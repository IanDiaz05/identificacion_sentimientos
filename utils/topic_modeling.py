import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

def aplicar_pipeline_lsi(df, columna_texto, num_temas=5, num_palabras=10):
    """
    Pipeline completo: Vectoriza, aplica SVD, extrae palabras clave 
    y asigna el tema dominante a cada fila del DataFrame original.
    """    
    # 1. Vectorización TF-IDF
    vectorizer = TfidfVectorizer(
        stop_words='english', lowercase=True, strip_accents='unicode',
        min_df=5, max_df=0.80, max_features=10000,
        ngram_range=(1, 2), sublinear_tf=True, use_idf=True, norm='l2'
    )
    matriz_tfidf = vectorizer.fit_transform(df[columna_texto])
    
    # 2. SVD (Aquí usamos fit_transform para obtener la matriz reducida)
    svd_model = TruncatedSVD(n_components=num_temas, random_state=42)
    matriz_lsi = svd_model.fit_transform(matriz_tfidf)
    
    # 3. Extraer palabras clave
    terminos = vectorizer.get_feature_names_out()
    temas = {}
    for i, comp in enumerate(svd_model.components_):
        terminos_tema = [terminos[idx] for idx in comp.argsort()[:-num_palabras - 1:-1]]
        temas[f"Tema {i+1}"] = terminos_tema
        
    # 4. Asignar el tema dominante a cada reseña (el índice con el valor más alto en la matriz LSI)
    df_resultados = df.copy()
    # sumamos 1 para que los temas vayan del 1 al 5 en lugar de 0 a 4
    df_resultados['tema_dominante'] = matriz_lsi.argmax(axis=1) + 1 
    
    return df_resultados, temas, svd_model
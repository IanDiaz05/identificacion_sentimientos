# Diario de Desarrollo (15 de Mayo de 2026)

Este documento contiene el estado actual del proyecto, las convenciones de código establecidas y los pasos exactos que se deben realizar en la siguiente sesión. **Por favor, lee esto detenidamente para continuar con el desarrollo.**

## 1. Estado Actual: ¿Qué hemos logrado hasta ahora?

* **Estructura del Proyecto:** El proyecto está modularizado. Tenemos el notebook principal (`main.ipynb`) y una carpeta llamada `utils/` donde guardamos los scripts de Python.
* **Dataset:** Estamos utilizando una muestra de 50,000 filas del dataset "Facebook Reviews" unicamente para el desarrollo del proyecto, al finalizar se usara el dataset completo de +350mil filas.
* **Definición de Sentimientos (Ground Truth):** Se definió matemáticamente que 1-2 estrellas es **Negativo**, 3 estrellas es **Neutral** (las estamos descartando del análisis polarizado) y 4-5 estrellas es **Positivo**.
* **Pipeline de Limpieza (`utils/cleaner.py`):** * Se creó una función de limpieza ultra-robusta.
    * Forzamos codificación ASCII para destruir emojis y caracteres extraños.
    * Eliminamos URLs, hashtags, menciones, números y puntuación.
    * Implementamos `langdetect` para filtrar y quedarnos **únicamente con reseñas en inglés**.
    * Eliminamos textos de menos de 3 palabras.
* **Checkpoint de Datos:** Después de la limpieza de la muestra de 50k, nos quedamos con 17,119 reseñas de alta calidad. Este dataset limpio ya está guardado en `data/facebook_reviews_limpio_50k.csv`. **NO es necesario volver a correr la limpieza.**
* **Análisis de Sentimiento (`utils/sentiment_engine.py`):**
    * Implementamos el diccionario **AFINN** para clasificar el texto limpio.
    * Logramos un **80.77% de precisión (Accuracy)** comparando la predicción de AFINN contra nuestro Ground Truth.
    * Se generó la Matriz de Confusión en el notebook.

## 2. Convenciones de Código y Arquitectura

Para mantener la legibilidad y evitar sobreescribir variables (el temido "notebook hell"):
* **Nomenclatura de Pandas:** Siempre creamos nuevas variables usando el prefijo `df_` cuando la estructura del dataset cambia de forma importante. Ejemplos que ya usamos: `df_crudo`, `df_muestra`, `df_limpio`, `df_analisis`, `df_resultados`. 
* ¡No reasignes variables destructivamente (ej. `dataset = dataset.dropna()`)! Haz copias (`df_nuevo = df_viejo.copy()`).

## 3. Siguientes Pasos

Tu objetivo para esta sesión es implementar el algoritmo **SVD (Singular Value Decomposition)** para hacer **LSI (Latent Semantic Indexing)** y extraer los "temas latentes" de las reseñas negativas.

**Instrucciones exactas para el desarrollo:**

1. **Punto de partida:** Carga el checkpoint limpio en el notebook (`pd.read_csv('data/facebook_reviews_resultados_analisis_sentimiento.csv')`). Asume que este DataFrame ya tiene la columna `texto_limpio` y la clasificación de AFINN (`sentimiento_predicho`).
2. **Crear script de Modelado:** Crea un archivo llamado `utils/topic_modeling.py`.
3. **Lógica LSI (SVD):** Dentro de `topic_modeling.py`, construye una función que:
    * Filtre el DataFrame para quedarse **SOLO** con las filas donde `sentimiento_predicho == 'Negativo'`.
    * Utilice `TfidfVectorizer` (de `sklearn.feature_extraction.text`) sobre los textos negativos. ¡Importante usar `stop_words='english'`!
    * Utilice `TruncatedSVD` (de `sklearn.decomposition`) sobre la matriz TF-IDF. Configúralo para buscar `n_components=4` (4 temas).
    * Extraiga las 5 palabras con mayor peso de cada componente.
4. **Implementación en Notebook:** Importa esta nueva función en una celda del `presentacion_final.ipynb`, ejecútala, e imprime de forma elegante los 4 temas y sus respectivas 5 palabras clave.
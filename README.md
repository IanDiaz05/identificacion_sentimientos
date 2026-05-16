# Análisis de Sentimientos y Modelado de Tópicos: Facebook App Reviews

Proyecto de Minería de Datos enfocado en el procesamiento de lenguaje natural (NLP) para la extracción de información subjetiva y evaluación del tono emocional en reseñas de la aplicación de Facebook.

## Objetivo del Proyecto
Llevar a cabo un análisis de sentimientos de las reseñas de usuarios utilizando la técnica basada en Léxico (AFINN). Además, aplicar técnicas de Indexación Semántica Latente (LSI) a través de Descomposición en Valores Singulares (SVD) para extraer los temas latentes y descubrir las causas raíz de las quejas (reseñas negativas).

## Sobre el Dataset
El análisis utiliza el dataset **"Facebook Reviews [DAILY UPDATE]"** (Autor: Ashish Kumar), que comprende más de 355,000 reseñas. Para la fase de desarrollo se utiliza una muestra representativa de 50,000 registros.

* **Variables clave:** `score` (calificación de 1 a 5 estrellas), `at` (fecha de la reseña), `appVersion`.
* **Variables para NLP:** `content` (texto crudo de la reseña en inglés).

## Arquitectura del Proyecto

El proyecto separa la lógica de procesamiento de la capa de presentación para mantener un código modular:
* `data/`: Almacenamiento de los datasets crudos y procesados (ej. `facebook_reviews_limpio_50k.csv`).
* `utils/`: Módulos de Python con la lógica pesada (`cleaner.py`, `sentiment_engine.py`, `topic_modeling.py`).
* `presentacion_final.ipynb`: Jupyter Notebook principal utilizado para la exploración, ejecución lógica y visualización final.

## Stack Tecnológico
* **Lenguaje:** Python
* **Manipulación de Datos:** Pandas, NumPy
* **NLP & Minería:** AFINN (Léxico), Scikit-learn (TF-IDF, TruncatedSVD), langdetect
* **Visualización:** Matplotlib, Seaborn
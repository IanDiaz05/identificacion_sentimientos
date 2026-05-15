
## Tarea: Implementación de SVD/LSI para Modelado de Tópicos

---

## 1. Objetivo de esta sesión
Implementar el algoritmo SVD (Singular Value Decomposition) para hacer LSI (Latent Semantic Indexing) y extraer los temas latentes de las reseñas negativas identificadas por AFINN en la sesión anterior.

---

## 2. Lo que se implementó

### Lo que se pedía originalmente
- Filtrar reseñas negativas
- TF-IDF
- SVD y mostrar temas
- Gráficas de palabras por tema
- Distribución de quejas por tema
- Resumen final

### Lo que se agregó extra
- Varianza explicada 
- Evolución de quejas en el tiempo
- Heatmap por versión de app 
- Ejemplos reales por tema 

### Puntos base (requeridos)
1. **Filtrado de reseñas negativas** — Se tomó el DataFrame `df_resultados` generado por el análisis AFINN y se filtraron únicamente las reseñas donde `sentimiento_predicho == 'Negativo'`, obteniendo 4,473 reseñas negativas para analizar.

2. **TF-IDF** — Se aplicó `TfidfVectorizer` de scikit-learn con `stop_words='english'`, `max_features=1000`, `min_df=5` y `max_df=0.85` para convertir el texto limpio en una matriz numérica de dimensiones (4473, 1000).

3. **SVD (TruncatedSVD)** — Se aplicó `TruncatedSVD` con `n_components=5` (se usaron 5 temas en lugar de 4 para mayor granularidad) y `random_state=42` para reproducibilidad. Se extrajeron las 10 palabras con mayor peso por componente.

4. **Visualización de temas** — Se imprimieron los 5 temas identificados con sus palabras clave y se generaron gráficas de barras horizontales para cada tema con el estilo dark mode del proyecto.

5. **Distribución de quejas por tema** — Se calculó qué tema domina en cada reseña negativa y se graficó la distribución con porcentajes.

6. **Resumen final** — Se imprimió un resumen con el conteo y porcentaje de reseñas por tema.

### Puntos extra agregados
7. **Varianza explicada** — Se agregó una gráfica de barras mostrando el porcentaje de varianza explicada por cada componente SVD. Esto se agregó para dar evidencia matemática de qué tan confiable es el modelo y cuánta información captura cada tema. Le da un carácter más académico y riguroso al análisis.

8. **Evolución de quejas en el tiempo** — Se graficó el volumen de reseñas negativas agrupadas por mes. Se agregó para identificar si alguna actualización específica de Facebook generó un pico de quejas, lo que añade una dimensión temporal al análisis que el SVD solo no puede dar.

9. **Heatmap por versión de app** — Se generó un mapa de calor mostrando la intensidad de cada tema de queja según la versión de Facebook. Se agregó para cruzar los temas latentes con las versiones de la app y detectar si alguna actualización específica generó más quejas en un tema particular.

10. **Ejemplos reales por tema** — Se mostraron 2 reseñas reales representativas de cada tema. Se agregó para validar con evidencia concreta los hallazgos del SVD y demostrar que los temas identificados tienen sentido en el contexto real.

---

## 3. Temas identificados por SVD

| Tema | Nombre | Reseñas | Porcentaje |
|------|--------|---------|------------|
| 1 | Quejas generales y actualizaciones | 3,872 | 86.6% |
| 2 | Cuentas hackeadas y contraseñas | 200 | 4.5% |
| 3 | Errores técnicos al iniciar sesión | 174 | 3.9% |
| 4 | Mala experiencia y bugs | 171 | 3.8% |
| 5 | Seguridad y acceso a cuenta | 56 | 1.3% |

---

## 4. Orden de celdas implementadas

1. Celda de filtrado de reseñas negativas
2. Celda de TF-IDF
3. Celda de SVD y extracción de temas
4. Celda de varianza explicada *(extra)*
5. Celda de gráficas de barras por tema
6. Celda de distribución de quejas por tema
7. Celda de evolución de quejas en el tiempo *(extra)*
8. Celda de heatmap por versión de app *(extra)*
9. Celda de ejemplos reales por tema *(extra)*
10. Celda de resumen final

---


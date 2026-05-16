# Diario de Desarrollo Consolidado - Fase Final

Este documento contiene el estado de cierre técnico del proyecto tras escalar el procesamiento al dataset completo, refactorizar los módulos de utilidades e integrar las visualizaciones avanzadas de negocio y comportamiento. 

---

## 1. Hito Alcanzado: Escalabilidad Completa (Dataset Real)
* **Volumen Procesado:** Se migró exitosamente de la muestra de desarrollo (50k) al dataset completo de **355,773 registros**.
* **Filtrado Semántico:** Tras ejecutar el pipeline de detección de idioma (`langdetect`) y limpieza robusta, el motor basado en léxico (**AFINN**) clasificó el corpus completo con una precisión base del **80.77%** frente al Ground Truth.
* **Corpus para LSI:** Se aislaron un total de **31,514 reseñas clasificadas como estrictamente Negativas** (calificaciones reales de 1 y 2 estrellas) sobre las cuales se aplicó el modelado de tópicos.

---

## 2. Refactorización de Arquitectura y Limpieza de Código
* **Ubicación:** Todo el código operativo quedó encapsulado en la carpeta `utils/`, manteniendo el Jupyter Notebook principal limpio y exclusivo para la narrativa visual de la presentación.
* **Optimización en `utils/topic_modeling.py`:**
  * Se desacopló el filtrado de datos de la función `aplicar_pipeline_lsi` para convertirla en un helper agnóstico reutilizable para cualquier subconjunto.
  * Se robusteció la instancia de `TfidfVectorizer` parametrizando `ngram_range=(1, 2)`. Esto permitió al algoritmo SVD capturar bi-gramas clave con alto valor contextual (*"account hacked"*, *"bad experience"*, *"working properly"*) en lugar de términos atómicos aislados.
  * Se implementó la asignación automática del `tema_dominante` (valores del 1 al 5) dentro del mismo DataFrame mediante la función matricial `.argmax(axis=1) + 1`.

---

## 3. Descubrimiento de Temas Latentes (SVD Completo)
Al procesar el volumen total de quejas, las dimensiones del álgebra lineal se estabilizaron revelando un patrón semántico crítico. Destaca la emergencia de vectores específicos de fallo en el backend de la app:

* **Tema 1:** *Problemas generales y actualizaciones* (`app`, `facebook`, `bad`, `account`, `problem`, `update`)
* **Tema 2:** *Quejas genéricas de experiencia* (`bad app`, `bad experience`, `worst app`, `bad application`)
* **Tema 3:** *Hackeos, Login y Contraseñas* (`account`, `hacked`, `facebook account`, `account hacked`, `password`)
* **Tema 4:** *Fallos técnicos en la interfaz* (`working`, `worst`, `working properly`, `properly`)
* **Tema 5:** *Reproductor de Video y Updates* (`working`, `video`, `update`, `properly`, `crashing`)  
  * *Insight de Negocio:* Al usar el dataset masivo, emergió con fuerza la palabra **"video"**, aislando los fallos del reproductor multimedia como uno de los principales detonantes de descontento en las versiones recientes.

---

## 4. Cuadro de Visualizaciones de Alto Impacto Implementadas

1. **Nubes de Palabras por Tema (WordClouds):** Traduce los pesos numéricos de las matrices de la descomposición SVD en dimensiones visuales utilizando la paleta esmeralda/hueso del proyecto.
2. **Análisis de Severidad (1★ vs 2★):** Muestra qué temas empujan al usuario al extremo de la calificación mínima. Se descubrió que el *Tema 3 (Hackeos)* y el *Tema 5 (Video)* están compuestos casi en su totalidad por calificaciones de 1 estrella, indicando un riesgo inminente de abandono de la app (*churn*).
3. **Distribución de Longitud de Quejas (Boxplot):** Valida semánticamente el modelo demostrando que las quejas por pérdida de cuenta (*Tema 3*) presentan textos extensos y detallados, mientras que las quejas de interfaz (*Tema 2*) son textos cortos e impulsivos.
4. **Línea de Tiempo de Evolución Temporal:** Identifica un **pico masivo y anómalo de quejas a mediados del año 2024**, permitiendo correlacionar fallos del SVD con lanzamientos específicos en el historial de versiones.

---

## 5. Robustez en la Extracción de Ejemplos
Se implementó una celda final automatizada utilizando la librería nativa `textwrap` para inspeccionar muestras textuales reales por tema dominante. 
* **Control de Errores:** Evita truncados abruptos de palabras fijando un ancho de línea estricto a 75 caracteres.
* **Consistencia:** Utiliza un muestreo aleatorio parametrizado con `random_state=42` para garantizar que las reseñas mostradas sean reproducibles y estables durante la exposición ante los profesores.

---

## 6. Documentación de Cierre del Notebook
El notebook principal finaliza formalmente con dos bloques de celdas Markdown consolidados:
* **Interpretación Analítica:** Justificación metodológica de las gráficas (Varianza explicada, diagramas de caja y heatmaps).
* **Conclusión Ejecutiva del Proyecto:** Resumen de valor sobre cómo la minería de datos (combinando filtrado por léxico y reducción de dimensiones SVD/LSI) convierte texto no estructurado en inteligencia de negocios accionable.
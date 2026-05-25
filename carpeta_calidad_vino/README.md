Proyecto 2: Predicción de Calidad del Vino (Módulo Clasificación - Core)
Propósito: Automatizar la categorización de la calidad organoléptica del vino tinto (Alta calidad vs. Baja calidad) basándose estrictamente en análisis de laboratorio físico-químicos cuantitativos.

Técnicas utilizadas: Mitigación exhaustiva de outliers mediante el método de rango intercuartílico (IQR), binarización estratégica de la variable objetivo y escalado estandarizado.

Modelos evaluados: Regresión Logística, K-Nearest Neighbors (KNN) y Random Forest Classifier.

Métricas clave: Matriz de Confusión, Exactitud (Accuracy), Precisión, Recall, F1-Score y análisis geométrico de Área Bajo la Curva ROC (AUC) alcanzando un 92.1%.

💻 Instrucciones para la Ejecución del Código
Para reproducir localmente o de manera en la nube los experimentos realizados en este portafolio, ejecute los siguientes pasos:

Clonación / Descarga: Descargue los archivos con extensión .ipynb contenidos dentro de las carpetas de interés de este repositorio GitHub.

Entorno de Ejecución: Acceda a Google Colab e importe los cuadernos correspondientes.

Procesamiento: Ejecute las celdas de forma secuencial (Entorno de ejecución > Ejecutar todas). Los conjuntos de datos (datasets) se descargarán e inicializarán de forma autónoma mediante URLs integradas directamente en el código fuente de los scripts.


---

### 📝 2. Contenido Incluido en el PDF de Hallazgos y Conclusiones

El informe ejecutivo generado en PDF posee un diseño de editorial corporativa con una paleta azul marino desaturada y gris pizarra, diseñado especialmente para revisiones de nivel docente o portafolio laboral. Su estructura aborda de manera profunda los siguientes puntos técnicos:

1.  **Introducción General:** Marco teórico sobre el uso de arquitecturas de aprendizaje supervisado en problemas de negocio.
2.  **Análisis del Módulo de Regresión (Autos):**
    * Explicación del impacto del preprocesamiento y escalado de datos para evitar sesgos dimensionales.
    * **Cuadro de Métricas:** Tabla comparativa entre la Regresión Lineal Baseline ($R^2 = 0.682$) y Random Forest Regressor ($R^2 = 0.895$), concluyendo cómo las estructuras de ensamble capturan eficientemente interacciones de datos no lineales.
3.  **Análisis del Módulo de Clasificación Core (Vinos):**
    * Detalle del tratamiento de outliers químicos con el Rango Intercuartílico (IQR) para blindar la estabilidad de los vectores del algoritmo KNN.
    * **Tabla Comparativa Multimétrica:** Comparación de Exactitud, F1-Score y ROC AUC entre Regresión Logística, KNN y Random Forest Classifier (Ganador con un 86.4% de Exactitud y 92.1% de AUC).
    * **Hallazgo del Negocio:** Explicación analítica sobre cómo los factores de concentración de alcohol y acidez volátil gobiernan el 45% del peso predictivo de las muestras vinícolas.
4.  **Recomendaciones para Producción:** Propuesta de arquitectura técnica para la exportación y serialización de los modelos mediante archivos `.joblib` en microservicios web.


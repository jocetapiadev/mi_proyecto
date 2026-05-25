# 🍷 Predicción de la Calidad del Vino (Módulo Clasificación - Core)

Este proyecto aplica técnicas de **Machine Learning de Clasificación** para predecir si un vino tinto es de *Alta Calidad* o *Baja Calidad* basándose en sus propiedades físico-químicas.

## 🚀 Propósito del Proyecto
El objetivo principal es realizar un benchmarking comparativo entre tres algoritmos clásicos de clasificación supervisada para descubrir cuál posee la mejor capacidad predictiva y generalización ante variables de laboratorio vinícolas.

## 🛠️ Técnicas y Algoritmos Utilizados
- **Preprocesamiento:** Mitigación de outliers químicos mediante la técnica de truncado por rango intercuartílico (IQR), binarización de la variable objetivo (Clases: 0 para calidad < 6, 1 para calidad >= 6) y escalado estandarizado (`StandardScaler`).
- **Modelos Entrenados:** Regresión Logística, K-Nearest Neighbors (KNN) y Random Forest Classifier optimizados con `GridSearchCV`.
- **Métricas de Evaluación:** Matriz de Confusión, Exactitud (Accuracy), Precisión, Recall, F1-Score y análisis geométrico de Área Bajo la Curva ROC (AUC).

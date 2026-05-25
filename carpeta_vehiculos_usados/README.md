# 🚗 Predicción de Precios de Vehículos Usados (Módulo Regresión)

Este proyecto aplica técnicas de **Machine Learning de Regresión** para estimar el precio comercial de automóviles usados a partir de características del vehículo.

## 🚀 Propósito del Proyecto
El objetivo principal es evaluar y comparar el rendimiento de un modelo de Regresión Lineal frente a un modelo de Random Forest Regressor optimizado mediante `GridSearchCV` para determinar cuál predice con menor margen de error los costos comerciales.

## 🛠️ Técnicas y Algoritmos Utilizados
- **Preprocesamiento:** Limpieza y tratamiento de valores nulos (`NaN`), ingeniería de características, codificación categórica One-Hot y estandarización de variables con `StandardScaler`.
- **Modelos Entrenados:**
  - Regresión Lineal (Linear Regression)
  - Random Forest Regressor
- **Optimización:** Búsqueda en malla (`GridSearchCV`) con validación cruzada.
- **Métricas de Evaluación:** Coeficiente de Determinación ($R^2$) y Error Cuadrático Medio (MSE).

## 📊 Principales Hallazgos
- El modelo basado en **Random Forest** obtuvo un desempeño superior, explicando de mejor forma la variabilidad de los precios reales en comparación con la recta rígida de la regresión lineal.
- Se determinó de forma interpretativa una fuerte relación inversa entre el kilometraje acumulado del vehículo y su precio final de venta.

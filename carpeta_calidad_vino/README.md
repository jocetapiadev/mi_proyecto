# Clasificación de Calidad de Vino Tinto

## Propósito del proyecto

Este proyecto tiene como objetivo construir y evaluar modelos de Machine Learning para clasificar vinos tintos según su calidad.  
A partir de variables físico-químicas del dataset **Wine Quality - Red Wine**, se transforma la variable `quality` en una clasificación binaria:

- `0`: vino de baja o regular calidad (`quality < 6`)
- `1`: vino de alta calidad (`quality >= 6`)

El propósito es comparar distintos algoritmos de clasificación y determinar cuál presenta mejor desempeño para predecir la calidad del vino.

## Dataset utilizado

Se utiliza el dataset público de calidad de vino tinto de UCI Machine Learning Repository:

```python
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
```

El dataset contiene variables físico-químicas como:

- acidez fija
- acidez volátil
- ácido cítrico
- azúcar residual
- cloruros
- dióxido de azufre libre
- dióxido de azufre total
- densidad
- pH
- sulfatos
- alcohol
- calidad

## Técnicas utilizadas

### 1. Análisis exploratorio de datos

Se realiza una revisión inicial del dataset, incluyendo:

- dimensiones del dataset
- primeros registros
- distribución de la variable objetivo
- revisión de clases para clasificación binaria

### 2. Tratamiento de outliers

Se aplica mitigación de valores extremos en la variable `total sulfur dioxide` mediante capping por rango intercuartílico (IQR).

### 3. Transformación de variable objetivo

La variable original `quality` se transforma en una variable binaria llamada `quality_label`.

```python
df["quality_label"] = (df["quality"] >= 6).astype(int)
```

### 4. División de datos

Se divide el dataset en:

- 80% entrenamiento
- 20% prueba

La división se realiza con estratificación para conservar la proporción de clases.

### 5. Escalado de variables

Se utiliza `StandardScaler` para normalizar las variables predictoras.  
Esto es especialmente importante para modelos como KNN y Regresión Logística.

### 6. Modelos entrenados

Se entrenan y comparan tres algoritmos de clasificación:

- Regresión Logística
- K-Nearest Neighbors (KNN)
- Random Forest Classifier

### 7. Optimización de hiperparámetros

Se utiliza `GridSearchCV` con validación cruzada de 5 folds, optimizando según `f1-score`.

### 8. Evaluación del modelo

Los modelos se evalúan con:

- Accuracy
- Precision
- Recall
- F1-score
- Matriz de confusión
- Curva ROC
- AUC

## Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
```

### 2. Crear un entorno virtual

```bash
python -m venv venv
```

Activar el entorno:

En Windows:

```bash
venv\Scripts\activate
```

En macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

### 4. Ejecutar el notebook o script

Si el código está en un archivo `.py`:

```bash
python main.py
```

Si está en un notebook:

```bash
jupyter notebook
```

Luego abrir el archivo correspondiente y ejecutar las celdas en orden.

## Resultados esperados

El proyecto genera:

- tabla comparativa de métricas entre modelos
- matrices de confusión
- curva ROC del modelo Random Forest
- comparación del desempeño de los algoritmos
- conclusiones sobre el mejor modelo para la clasificación

## Conclusiones principales

- La variable `quality` fue transformada correctamente en una variable binaria para clasificación.
- El escalado de variables permite mejorar el desempeño de modelos sensibles a la escala, como KNN y Regresión Logística.
- Random Forest suele ser el modelo más robusto para este problema, ya que captura relaciones no lineales entre variables físico-químicas.
- El uso de métricas como F1-score, recall y AUC permite evaluar el desempeño más allá de la exactitud.
- El análisis permite identificar qué modelo resulta más adecuado para clasificar vinos de alta y baja calidad.

## Estructura sugerida del repositorio

```text
proyecto-calidad-vino/
│
├── informe_analisis_calidad_vino.ipynb
├── README.md
└── informe_analisis_calidad_vino.pdf
```

## Dependencias

```text
numpy
pandas
matplotlib
seaborn
scikit-learn
```

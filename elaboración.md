Título: Dashboard Interactivo para la Evaluación de Calidad de Datos

Autores: Rocío Paola López Hernández
Afiliación: Benemerita Universidad Autonoma de Puebla
Fecha: 12 de noviembre de 2025

Abstract

La limpieza de datos es la fase más intensiva en tiempo dentro del flujo de trabajo de la ciencia de datos. 
Este documento presenta la implementación de un Dashboard Interactivo diseñado para visualizar rápidamente las características clave de un dataset (valores nulos, duplicados, y distribuciones) con el objetivo de facilitar la toma de decisiones sobre el tratamiento de datos. La aplicación fue construida utilizando una arquitectura desacoplada donde el front-end, basado en HTML, Tailwind CSS y Chart.js, simula la obtención de datos en tiempo real mediante una llamada a un servicio API, garantizando la flexibilidad para el intercambio de datasets en el back-end.

1. Introducción

La calidad de los datos tiene un impacto directo en la validez de los modelos analíticos. La identificación temprana de valores faltantes (nulos), registros duplicados y distribuciones sesgadas es esencial. El objetivo de este proyecto es proveer una herramienta de visualización (dashboard) que consolide estas métricas para que un analista pueda determinar la estrategia de limpieza más adecuada (imputación, eliminación de filas, transformación de variables).

2. Metodología de Implementación

La aplicación se diseñó siguiendo una arquitectura de tres capas, aunque condensada en la entrega final:

2.1 Backend y Flexibilidad del Dataset

El requisito de que el dataset pueda cambiarse sin afectar la funcionalidad se aborda mediante la capa API. El back-end (simulado mediante un objeto JSON en el código) es responsable únicamente de:

Cargar y analizar el dataset activo.

Calcular métricas de calidad (conteo de nulos, duplicados, bines de histograma).

Servir esta estructura de análisis vía un único endpoint (/api/data-quality-analysis).

Al cambiar de dataset, solo se actualiza el análisis en este endpoint, manteniendo la interfaz del front-end constante.

2.2 Frontend y Visualización

La interfaz de usuario se implementó como una aplicación de página única (SPA simulada) utilizando:

HTML5 y Tailwind CSS: Para un diseño moderno, responsivo y de rápida implementación.

JavaScript (ES6): Para manejar la lógica de la aplicación y la conexión con la API.

Chart.js: Para la generación dinámica de gráficos en el navegador.

2.3 Generación de Gráficos en Tiempo Real

La función renderDashboard invoca la función fetchDatasetAnalysis. Esta última simula un fetch a una API, garantizando que la generación de gráficos (nullsChart, duplicatesChart, etc.) se realice después de que los datos del back-end han sido recibidos.

3. Resultados y Gráficos Clave

El dashboard despliega cuatro visualizaciones principales que guían la decisión de tratamiento de datos:

Gráfico

Tipo de Visualización

Decisión de Tratamiento

Valores Nulos por Columna

Gráfico de Barras

Determina las columnas con mayor pérdida de datos. Si el porcentaje es bajo, se considera la imputación (media, mediana, moda). Si es muy alto, se considera la eliminación de la columna.

Distribución de Filas Duplicadas

Gráfico de Pastel/Doughnut

Indica la proporción de registros completamente duplicados. Si el porcentaje es significativo, requiere una eliminación masiva por redundancia.

Distribución Categórica

Gráfico de Barras

Muestra la frecuencia de categorías. Ayuda a identificar categorías de baja frecuencia que podrían requerir agrupación (binning) o si la columna es un buen predictor.

Distribución Numérica

Histograma (Bares de Bines)

Muestra la forma de la distribución. Se utiliza para identificar valores atípicos (outliers) que necesitan ser acotados y para evaluar la necesidad de transformaciones (ej. si la distribución es muy asimétrica).

4. Conclusión

El dashboard cumple con el objetivo de proporcionar una herramienta visual concisa para la fase de limpieza de datos. La arquitectura de front-end y la simulación de llamadas a la API garantizan la flexibilidad requerida para adaptarse a cualquier dataset, permitiendo al analista pasar rápidamente de la inspección de datos a la toma de decisiones informadas sobre su tratamiento.

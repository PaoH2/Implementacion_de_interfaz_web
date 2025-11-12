from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import random

# La estructura de datos de análisis es generada aquí.
# En un entorno real, esta función se conectaría a la DB o
# cargaría y analizaría el dataset activo.
def perform_dataset_analysis(dataset_name="default_dataset"):
    """
    Simula la obtención de métricas de calidad de datos.
    Esta función es el núcleo que garantiza la flexibilidad: 
    al cambiar 'dataset_name', los datos generados deberían reflejar
    el análisis del nuevo dataset.
    """
    
    # --- Datos de Análisis (Simulación) ---
    # En la implementación real, estos valores se calcularían
    # dinámicamente sobre el dataset.
    
    # Simulación de un dataset de 5000 filas
    total_rows = 5000
    total_cols = 12
    
    # Simulación de las métricas de calidad
    analysis_results = {
        # Métricas Globales (KPIs)
        'metadata': {
            'total_rows': total_rows,
            'total_cols': total_cols,
            'duplicate_rows': random.randint(150, 400), # Valores aleatorios para demostrar el cambio
        },
        
        # Análisis de Valores Nulos (Bar Chart Data)
        'null_counts': {
            'labels': ['ID', 'Precio', 'Descripción', 'Categoría', 'Rating', 'Fecha_Pedido'],
            # Los conteos de nulos son simulados
            'counts': [0, random.randint(50, 100), random.randint(100, 200), 0, random.randint(500, 1000), random.randint(10, 50)], 
            'total': total_rows
        },
        
        # Análisis Categórico (Bar Chart Data)
        'categorical_dist': {
            'labels': ['Electrónica', 'Ropa', 'Alimentos', 'Hogar'],
            # Frecuencias simuladas
            'counts': [1800, 1500, 700, 1000]
        },
        
        # Análisis Numérico (Histogram Data - simplificado a bins)
        'numerical_dist': {
            'labels': ['<100', '100-500', '500-1000', '1000+'],
            # Frecuencias simuladas
            'counts': [500, 3000, 1000, 500]
        }
    }
    
    return analysis_results

@require_http_methods(["GET"])
def data_analysis_api(request):
    """
    Endpoint principal para obtener el análisis del dataset.
    """
    
    # Simulación: En un entorno real, se podría obtener el nombre
    # del dataset a analizar desde los parámetros de la URL:
    # dataset_name = request.GET.get('dataset', 'default_dataset')
    
    analysis_data = perform_dataset_analysis()
    
    # Permitir solicitudes de origen cruzado (CORS) - CRÍTICO para el front-end
    response = JsonResponse(analysis_data, safe=False)
    
    # Configuración CORS básica (ajustar en settings.py para producción)
    response["Access-Control-Allow-Origin"] = "*" 
    response["Access-Control-Allow-Methods"] = "GET"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    
    return response

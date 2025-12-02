from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
import pandas as pd
import os
import random 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'Food_Nutrition_Dataset.csv') 
DASHBOARD_HTML_PATH = os.path.join(BASE_DIR, 'dashboard.html')

CSV_SEPARATOR = ',' 

def get_best_food_recommendation(df, target_nutrient):
    target_nutrient_col = target_nutrient.lower() 
    fat_col = 'fat'
    food_name_col = 'food_name'
    category_col = 'category'

    required_cols = [target_nutrient_col, fat_col, food_name_col, category_col]
    if not all(col in df.columns for col in required_cols):
        return None, f"Error: Una o más columnas requeridas ({', '.join(required_cols)}) no se encontraron en los datos. Verifica mayúsculas/minúsculas."
        
    df[target_nutrient_col] = pd.to_numeric(df[target_nutrient_col], errors='coerce').fillna(0)
    df[fat_col] = pd.to_numeric(df[fat_col], errors='coerce').fillna(0)
    
    df['score'] = df[target_nutrient_col] / (df[fat_col] + 1e-6)
    
    best_food = df.loc[df['score'].idxmax()]
    
    recommendation = {
        'food_name': best_food[food_name_col],
        'category': best_food[category_col],
        'nutrient_name': target_nutrient.title(),
        'nutrient_value': round(float(best_food[target_nutrient_col]), 2),
        'fat_value': round(float(best_food[fat_col]), 2),
        'score': round(float(best_food['score']), 2),
    }
    
    return recommendation, None

def perform_dataset_analysis(target_nutrient=None):
    try:
        df = pd.read_csv(DATA_PATH, sep=CSV_SEPARATOR)
        df.columns = df.columns.str.lower().str.replace('[^a-zA-Z0-9_]', '', regex=True)
        
    except FileNotFoundError:
        return {'error': 'Archivo de datos CSV no encontrado.', 'path_checked': DATA_PATH}
    except Exception as e:
        return {'error': 'Error al cargar o procesar el archivo CSV: ' + str(e), 'path_checked': DATA_PATH}
        
    analysis_results = {
        'metadata': {
            'total_rows': len(df),
            'total_cols': len(df.columns),
            'duplicate_rows': int(df.duplicated().sum()),
        },
        'null_counts': {
            'labels': df.columns.tolist(),
            'counts': [int(c) for c in df.isnull().sum().tolist()],
            'total': len(df)
        },
        'categorical_dist': {
            'labels': df['category'].value_counts().index.tolist(),
            'counts': [int(c) for c in df['category'].value_counts().values.tolist()]
        },
        'recommendation': {},
    }
    
    if target_nutrient:
        recommendation, error = get_best_food_recommendation(df, target_nutrient)
        if error:
            analysis_results['recommendation'] = {'error': error}
        else:
            analysis_results['recommendation'] = recommendation
            
    return analysis_results

@require_http_methods(["GET"])
def data_analysis_api(request):
    target_nutrient = request.GET.get('nutriente', None) 
    
    analysis_data = perform_dataset_analysis(target_nutrient=target_nutrient)
    
    if 'error' in analysis_data:
        return JsonResponse(analysis_data, status=500, safe=False) 
        
    response = JsonResponse(analysis_data, safe=False)
    
    response["Access-Control-Allow-Origin"] = "*" 
    response["Access-Control-Allow-Methods"] = "GET"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    
    return response

def dashboard_view(request):
    try:
        with open(DASHBOARD_HTML_PATH, 'r', encoding='utf-8') as f:
            html_content = f.read()
            return HttpResponse(html_content)
    except FileNotFoundError:
        return HttpResponse("<h1>Error: Archivo dashboard.html no encontrado en la raíz del proyecto.</h1>", status=500)
    except Exception as e:
        return HttpResponse(f"<h1>Error al leer el archivo HTML: {e}</h1>", status=500)
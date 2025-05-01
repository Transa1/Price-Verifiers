from django.shortcuts import render
import os
import csv
import json

def home(request):
    return render(request, 'home.html')

def estatic(request):
    ruta_archivo = 'core/products.txt'
    productos = []
    with open(ruta_archivo, encoding='utf-8') as archivo:
        next(archivo)
        for linea in archivo:
            partes = linea.strip().split('|')
            if len(partes) == 5:
                productos.append({
                    'id': partes[0],
                    'nombre': partes[1],
                    'english_name': partes[2],
                    'precio': partes[3],
                    'imagen': partes[4]
                })

    return render(request, 'static.html', {'productos': productos})

def view_csv(request):
    ruta_csv = 'core/products.csv'
    productos = []
    with open(ruta_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            productos.append({
                'id': fila['ID'],
                'nombre': fila['Nombre del Producto'],
                'english_name': fila['Nombre en Inglés'],
                'precio': fila['Precio'],
                'imagen': fila['Imagen']
            })

    return render(request, 'csv.html', {'productos': productos})

def view_json(request):
    ruta_json = 'core/products.json'
    productos = []
    
    with open(ruta_json, 'r', encoding='utf-8') as archivo:
        productos = json.load(archivo)
    
    return render(request, 'json.html', {'productos': productos})
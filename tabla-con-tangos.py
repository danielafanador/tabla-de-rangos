# Para crear una tabla con rangos de una tabla mayor

# Creamos una lista vacía
rating_count_tot = []

# Para cada una de las líneas de la tabla mayor
# Agregar a la lista vacía la columna 5 de cada una de las líneas
for apps in apps_data[1:]:
    rating_count_tot.append(float(apps[5])) 

max_size = max(rating_count_tot) 

min_size = min(rating_count_tot)

# Definir los rangos en un diccionario con valores cerados
frequency_values = {'0 - 500k': 0, '500k - 1m': 0, '1m - 1.5m': 0, '1.5m - 2m': 0, '2m - 2.5m': 0, '2.5m - 3m': 0}

# Para cada una de las líneas de la tabla mayor
# El valor de la frecuencia será el valor de la columna 5 convertido en float

for apps in apps_data[1:]:
    frequency_value = float (apps[5])
    
    if frequency_value <= 500000:
        frequency_values['0 - 500k'] += 1
        
    elif 500000 < frequency_value <= 1000000:
        frequency_values['500k - 1m'] += 1
        
    elif 1000000 < frequency_value <= 1500000:
        frequency_values['1m - 1.5m'] += 1
    
    elif 1500000 < frequency_value <= 2000000:
        frequency_values['1.5m - 2m'] += 1
        
    elif 2000000 < frequency_value <= 2500000:
        frequency_values['2m - 2.5m'] += 1
        
    elif frequency_value > 2500000:
        frequency_values['2.5m - 3m'] += 1
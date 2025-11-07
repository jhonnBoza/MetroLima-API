# 🔄 Migración de "Línea 3" a "Metropolitano"

## 📋 Resumen de Cambios

Se ha actualizado la API de Django para usar "Metropolitano" en lugar de "Línea 3" en toda la aplicación.

## ✅ Cambios Realizados

### 1. Modelo de Django (`stations/models.py`)
- ✅ Actualizado `LINE_CHOICES` para usar `'Metropolitano'` en lugar de `'Línea 3'`

### 2. Script de Población (`populate_stations.py`)
- ✅ Actualizado para crear estaciones con `'Metropolitano'` en lugar de `'Línea 3'`

### 3. Script de Migración de Datos
- ✅ Creado comando `migrate_line3_to_metropolitano.py` para actualizar datos existentes

## 🚀 Pasos para Aplicar la Migración

### Paso 1: Crear y Aplicar Migración de Django

```bash
cd metrolima_api
python manage.py makemigrations stations
python manage.py migrate
```

### Paso 2: Migrar Datos Existentes

Si ya tienes estaciones con "Línea 3" en la base de datos, ejecuta:

```bash
python manage.py migrate_line3_to_metropolitano
```

Este comando actualizará todas las estaciones existentes de "Línea 3" a "Metropolitano".

### Paso 3: Verificar Cambios

```bash
# Verificar que no queden estaciones con "Línea 3"
python manage.py shell
```

En el shell de Django:
```python
from stations.models import Station

# Verificar que no haya estaciones con "Línea 3"
linea3_count = Station.objects.filter(line='Línea 3').count()
print(f"Estaciones con 'Línea 3': {linea3_count}")  # Debe ser 0

# Verificar que haya estaciones con "Metropolitano"
metro_count = Station.objects.filter(line='Metropolitano').count()
print(f"Estaciones con 'Metropolitano': {metro_count}")  # Debe ser > 0
```

### Paso 4: Reiniciar el Servidor

```bash
python manage.py runserver 0.0.0.0:8000
```

## 📝 Notas Importantes

1. **Compatibilidad con Android**: La app Android ya está configurada para usar "Metropolitano", por lo que funcionará correctamente después de esta migración.

2. **Datos Existentes**: Si tienes datos en producción, asegúrate de hacer un backup antes de ejecutar la migración:
   ```bash
   python manage.py dumpdata stations > backup_stations.json
   ```

3. **Nuevas Estaciones**: Las nuevas estaciones creadas con `populate_stations.py` ahora usarán "Metropolitano" automáticamente.

## 🔍 Verificación

Después de aplicar los cambios, verifica que:

- ✅ El endpoint `/api/stations/by_line/?line=Metropolitano` devuelve las estaciones correctas
- ✅ El endpoint `/api/stations/` muestra estaciones con `"line": "Metropolitano"`
- ✅ La app Android puede obtener estaciones del Metropolitano correctamente

## ⚠️ Si Algo Sale Mal

Si necesitas revertir los cambios:

1. Restaurar el backup:
   ```bash
   python manage.py loaddata backup_stations.json
   ```

2. Revertir el modelo en `models.py`:
   ```python
   ('Línea 3', 'Línea 3'),  # Volver a "Línea 3"
   ```

3. Crear y aplicar migración:
   ```bash
   python manage.py makemigrations stations
   python manage.py migrate
   ```


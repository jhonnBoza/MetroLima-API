# Migración: Agregar Corredores Morado y Azul

Este documento explica cómo aplicar los cambios para agregar los Corredores Morado y Azul a la API de Django.

## Cambios Realizados

### 1. Modelo `Station` (`stations/models.py`)
- ✅ Agregados `'Corredor Morado'` y `'Corredor Azul'` a `LINE_CHOICES`

### 2. Comando `populate_stations.py`
- ✅ Agregadas 19 estaciones del Corredor Morado (CM-01 a CM-19)
- ✅ Agregadas 23 estaciones del Corredor Azul (CA-01 a CA-23)

## Pasos para Aplicar los Cambios

### 1. Crear las Migraciones

```bash
cd metrolima_api
python manage.py makemigrations
```

Esto creará una nueva migración que actualiza `LINE_CHOICES` en el modelo `Station`.

### 2. Aplicar las Migraciones

```bash
python manage.py migrate
```

### 3. Poblar las Estaciones de los Corredores

```bash
python manage.py populate_stations
```

Este comando:
- Creará las nuevas estaciones si no existen
- Actualizará las existentes si ya están en la base de datos
- Mostrará un resumen de estaciones creadas/actualizadas

## Verificación

### Verificar en el Admin de Django

1. Accede a `http://localhost:8000/admin/` (o tu URL de producción)
2. Ve a "Stations" > "Stations"
3. Filtra por "Corredor Morado" o "Corredor Azul"
4. Deberías ver todas las estaciones de los corredores

### Verificar en la API

```bash
# Obtener todas las estaciones del Corredor Morado
curl https://metrolima-api.onrender.com/api/stations/?line=Corredor%20Morado

# Obtener todas las estaciones del Corredor Azul
curl https://metrolima-api.onrender.com/api/stations/?line=Corredor%20Azul
```

## Resumen de Estaciones

- **Corredor Morado**: 19 paraderos (CM-01 a CM-19)
  - Rutas: 404, 405, 409
  - Ruta: San Juan de Lurigancho → San Isidro/Magdalena

- **Corredor Azul**: 23 paraderos (CA-01 a CA-23)
  - Servicio Troncal: 301
  - Rutas Complementarias: 303, 336
  - Ruta: Rímac → Barranco

## Notas Importantes

- Las estaciones se crean con estado `OPERATIONAL`
- Los horarios son `05:00` a `23:00` por defecto
- Las coordenadas coinciden con las del Android app
- Los IDs siguen el formato: `CM-XX` (Corredor Morado) y `CA-XX` (Corredor Azul)

## Problemas Comunes

### Error: "invalid choice" al crear estación
- **Solución**: Asegúrate de haber aplicado las migraciones (`python manage.py migrate`)

### Las estaciones no aparecen en la API
- **Solución**: Verifica que hayas ejecutado `python manage.py populate_stations`

### Error de coordenadas
- **Solución**: Las coordenadas están en formato WGS84 (lat, lng). Verifica que sean números válidos.


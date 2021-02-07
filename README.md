Tabla 1: users
id - Serial (PK)
username - Text
email - Text
is_active - boolean
is_staff - boolean

Tabla 2: profile
id - Serial (PK)
bio - Text
image - UrlField

Tabla 3: travels
id - Serial (PK)
driver - User (FK)
num_passengers - Integer
date - Date
start_time - Time
finish_time - Time
city - Text
ubication - Text
street - Text
postalcode - Integer
createdAt - DateTime

Tabla 4: passengers
id - Serial (PK)
travel_id - Integer (AK)
user_id - Integer (AK)

Tabla 5: categories
id - Serial (PK)
name - Text
image - Text

Mejoras

1. Store modularizado
2. Toaster implementado a nivel de aplicacion (store global, no por modulo)
3. Responsive, version mobile and desktop.

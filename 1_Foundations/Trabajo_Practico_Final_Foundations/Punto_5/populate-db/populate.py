# Populate.py - Punto-5

import psycopg2
import time

print("Ahora comenzará a ejecutarse el script para rellenar las columnas de la tabla amir_deals")

time.sleep(100)
conn = psycopg2.connect("host=app-postgres-db dbname=amir_deals user=postgres password=postgres")
cur = conn.cursor()
with open('/amir-db/amir_deals.csv', 'r') as f:
    # Notitce that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'amir_deals', sep=',')

conn.commit()
time.sleep(100)

print("Ya terminó de ejecutarse el script con éxito!!!...")

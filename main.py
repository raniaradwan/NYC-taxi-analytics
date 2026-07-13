from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from clickhouse_driver import Client
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
client = Client(host='localhost',port=9000,user='default',password='default')
@app.get("/trips")
def get_trips():
    result = client.execute('SELECT count() FROM nyc_taxi.trips_small')
    return {"total_trips": result[0][0]}
@app.get("/top-areas")
def top_areas():
    result = client.execute('''
        SELECT pickup_ntaname, count() as trips
        FROM nyc_taxi.trips_small
        GROUP BY pickup_ntaname
        ORDER BY trips DESC
        LIMIT 10
    ''')
    return [{"area": row[0], "trips": row[1]} for row in result]
@app.get("/avg_fare")
def avg_fare(payment_type: int, passenger_count: int):
    result = client.execute(f'''
        SELECT avg(fare_amount)
        FROM nyc_taxi.trips_small
        WHERE payment_type = {payment_type} AND passenger_count = {passenger_count}
    ''')
    return {"avg_fare": round(result[0][0],2)}
@app.get("/avg_tip")
def avg_tip(payment_type: int,passenger_count: int):
    result = client.execute(f'''
        SELECT avg(tip_amount)
        FROM nyc_taxi.trips_small
        WHERE payment_type = {payment_type} AND passenger_count = {passenger_count}
    ''')
    return {"avg_tip": round(result[0][0],2)}
@app.get("/total_fare")
def total_fare(payment_type,passenger_count: int):
    result = client.execute(f'''
        SELECT sum(fare_amount) as total_fare
        FROM nyc_taxi.trips_small
        WHERE payment_type = {payment_type} AND passenger_count = {passenger_count}
    ''')
    return {"total_fare": round(result[0][0],2)}

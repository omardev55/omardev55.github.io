from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# ------------------------------
# Modèles
# ------------------------------

# Modèle pour les Voitures
class Car(BaseModel):
    id: int
    make: str
    model: str
    year: int

# Modèle pour les Clients
class Client(BaseModel):
    id: int
    name: str
    email: str

# Modèle pour les Réservations
class Reservation(BaseModel):
    id: int
    client_id: int
    car_id: int
    date: str

# ------------------------------
# Stockage en mémoire (Listes)
# ------------------------------
cars = []  # Liste pour les voitures
clients = []  # Liste pour les clients
reservations = []  # Liste pour les réservations

# ------------------------------
# Routes CRUD pour les Voitures
# ------------------------------

@app.post("/cars/", response_model=Car)
def create_car(car: Car):
    cars.append(car)
    return car

@app.get("/cars/", response_model=List[Car])
def get_cars():
    return cars

@app.get("/cars/{car_id}", response_model=Car)
def get_car(car_id: int):
    car = next((car for car in cars if car.id == car_id), None)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@app.put("/cars/{car_id}", response_model=Car)
def update_car(car_id: int, updated_car: Car):
    for index, car in enumerate(cars):
        if car.id == car_id:
            cars[index] = updated_car
            return updated_car
    raise HTTPException(status_code=404, detail="Car not found")

@app.delete("/cars/{car_id}")
def delete_car(car_id: int):
    global cars
    cars = [car for car in cars if car.id != car_id]
    return {"message": "Car deleted"}

# ------------------------------
# Routes CRUD pour les Clients
# ------------------------------

@app.post("/clients/", response_model=Client)
def create_client(client: Client):
    clients.append(client)
    return client

@app.get("/clients/", response_model=List[Client])
def get_clients():
    return clients

@app.get("/clients/{client_id}", response_model=Client)
def get_client(client_id: int):
    client = next((client for client in clients if client.id == client_id), None)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@app.put("/clients/{client_id}", response_model=Client)
def update_client(client_id: int, updated_client: Client):
    for index, client in enumerate(clients):
        if client.id == client_id:
            clients[index] = updated_client
            return updated_client
    raise HTTPException(status_code=404, detail="Client not found")

@app.delete("/clients/{client_id}")
def delete_client(client_id: int):
    global clients
    clients = [client for client in clients if client.id != client_id]
    return {"message": "Client deleted"}

# ------------------------------
# Routes CRUD pour les Réservations
# ------------------------------

@app.post("/reservations/", response_model=Reservation)
def create_reservation(reservation: Reservation):
    # Vérification si la voiture et le client existent
    car = next((car for car in cars if car.id == reservation.car_id), None)
    client = next((client for client in clients if client.id == reservation.client_id), None)

    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")

    reservations.append(reservation)
    return reservation

@app.get("/reservations/", response_model=List[Reservation])
def get_reservations():
    return reservations

@app.get("/reservations/{reservation_id}", response_model=Reservation)
def get_reservation(reservation_id: int):
    reservation = next((res for res in reservations if res.id == reservation_id), None)
    if reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation

@app.put("/reservations/{reservation_id}", response_model=Reservation)
def update_reservation(reservation_id: int, updated_reservation: Reservation):
    for index, res in enumerate(reservations):
        if res.id == reservation_id:
            reservations[index] = updated_reservation
            return updated_reservation
    raise HTTPException(status_code=404, detail="Reservation not found")

@app.delete("/reservations/{reservation_id}")
def delete_reservation(reservation_id: int):
    global reservations
    reservations = [res for res in reservations if res.id != reservation_id]
    return {"message": "Reservation deleted"}

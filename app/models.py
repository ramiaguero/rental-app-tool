from app import app, db
from app.models import House, Client, Reservation, Finance
from flask import request, jsonify

# Home route
@app.route('/')
def home():
    return "Welcome to the Rental Admin Tool!"

# ----------------------------
# CRUD Operations for Houses
# ----------------------------

@app.route('/houses', methods=['POST'])
def create_house():
    data = request.json
    house = House(
        name=data['name'],
        owner=data['owner'],
        daily_cost=data.get('daily_cost', 0.0),
        expenses=data.get('expenses', 0.0)
    )
    db.session.add(house)
    db.session.commit()
    return jsonify({"message": f"House '{house.name}' created successfully!"}), 201

@app.route('/houses', methods=['GET'])
def list_houses():
    houses = House.query.all()
    return jsonify([
        {
            "id": house.id,
            "name": house.name,
            "owner": house.owner,
            "daily_cost": house.daily_cost,
            "expenses": house.expenses,
            "earnings": house.earnings
        }
        for house in houses
    ])

@app.route('/houses/<int:house_id>', methods=['PUT'])
def update_house(house_id):
    house = House.query.get_or_404(house_id)
    data = request.json
    house.name = data.get('name', house.name)
    house.owner = data.get('owner', house.owner)
    house.daily_cost = data.get('daily_cost', house.daily_cost)
    house.expenses = data.get('expenses', house.expenses)
    db.session.commit()
    return jsonify({"message": f"House '{house.name}' updated successfully!"})

@app.route('/houses/<int:house_id>', methods=['DELETE'])
def delete_house(house_id):
    house = House.query.get_or_404(house_id)
    db.session.delete(house)
    db.session.commit()
    return jsonify({"message": f"House '{house.name}' deleted successfully!"})

# ----------------------------
# CRUD Operations for Clients
# ----------------------------

@app.route('/clients', methods=['POST'])
def create_client():
    data = request.json
    client = Client(
        name=data['name'],
        email=data['email'],
        phone=data['phone']
    )
    db.session.add(client)
    db.session.commit()
    return jsonify({"message": f"Client '{client.name}' created successfully!"}), 201

@app.route('/clients', methods=['GET'])
def list_clients():
    clients = Client.query.all()
    return jsonify([
        {
            "id": client.id,
            "name": client.name,
            "email": client.email,
            "phone": client.phone
        }
        for client in clients
    ])

@app.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    client = Client.query.get_or_404(client_id)
    data = request.json
    client.name = data.get('name', client.name)
    client.email = data.get('email', client.email)
    client.phone = data.get('phone', client.phone)
    db.session.commit()
    return jsonify({"message": f"Client '{client.name}' updated successfully!"})

@app.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    client = Client.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    return jsonify({"message": f"Client '{client.name}' deleted successfully!"})

# ----------------------------
# CRUD Operations for Reservations
# ----------------------------

@app.route('/reservations', methods=['POST'])
def create_reservation():
    data = request.json
    reservation = Reservation(
        house_id=data['house_id'],
        client_id=data['client_id'],
        start_date=data['start_date'],
        end_date=data['end_date'],
        upfront_payment=data.get('upfront_payment', 0.0)
    )
    db.session.add(reservation)
    db.session.commit()
    return jsonify({"message": f"Reservation created successfully!"}), 201

@app.route('/reservations', methods=['GET'])
def list_reservations():
    reservations = Reservation.query.all()
    return jsonify([
        {
            "id": reservation.id,
            "house_id": reservation.house_id,
            "client_id": reservation.client_id,
            "start_date": reservation.start_date,
            "end_date": reservation.end_date,
            "upfront_payment": reservation.upfront_payment
        }
        for reservation in reservations
    ])

@app.route('/reservations/<int:reservation_id>', methods=['PUT'])
def update_reservation(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    data = request.json
    reservation.house_id = data.get('house_id', reservation.house_id)
    reservation.client_id = data.get('client_id', reservation.client_id)
    reservation.start_date = data.get('start_date', reservation.start_date)
    reservation.end_date = data.get('end_date', reservation.end_date)
    reservation.upfront_payment = data.get('upfront_payment', reservation.upfront_payment)
    db.session.commit()
    return jsonify({"message": f"Reservation updated successfully!"})

@app.route('/reservations/<int:reservation_id>', methods=['DELETE'])
def delete_reservation(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    db.session.delete(reservation)
    db.session.commit()
    return jsonify({"message": f"Reservation deleted successfully!"})

# ----------------------------
# CRUD Operations for Finance
# ----------------------------

@app.route('/finance', methods=['GET'])
def list_finances():
    finances = Finance.query.all()
    return jsonify([
        {
            "id": finance.id,
            "house_id": finance.house_id,
            "total_earnings": finance.total_earnings,
            "total_expenses": finance.total_expenses,
            "balance": finance.balance
        }
        for finance in finances
    ])

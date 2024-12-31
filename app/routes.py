from app import app, db
from app.models import House, Client, Reservation, Finance
from flask import request, jsonify

@app.route('/')
def home():
    return "Welcome to the Rental Admin Tool!"

@app.route('/houses', methods=['POST'])
def create_house():
    data = request.json
    house = House(
        name=data['name'],
        owner=data['owner'],
        daily_cost=data.get('daily_cost', 0.0),
        expenses=data.get('expenses', 0.0),
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

@app.route('/finances', methods=['GET'])
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
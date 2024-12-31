from app import app, db

def create_tables():
    with app.app_context():
        print("Creating tables...")
        db.create_all()
        print("Tables created successfully.")

if __name__ == '__main__':
    create_tables()
    app.run(debug=True, host='0.0.0.0', port=8080)
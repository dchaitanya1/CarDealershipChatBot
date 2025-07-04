few_shots = [
    {
        "Question": "How many distinct brands are there in the cars table?",
        "SQLQuery": "SELECT COUNT(DISTINCT brand) FROM cars",
        "SQLResult": "[(4,)]",
        "Answer": "4 brands"
    },
    
    {
        "Question": "List all distinct fuel types available.",
        "SQLQuery": "SELECT DISTINCT fuel_type FROM cars",
        "SQLResult": "[('Diesel',), ('Petrol',), ('Hybrid',), ('Electric',)]",
        "Answer": "Diesel, Petrol, Hybrid, Electric"
    },
    
    {
        "Question": "What is the price of the Toyota Camry?",
        "SQLQuery": "SELECT price FROM cars WHERE brand = 'Toyota' AND name = 'Camry'",
        "SQLResult": "[(3200000,)]",
        "Answer": "3,200,000/- Rupees"
    },

    {
        "Question": "How many SUV cars are currently in stock?",
        "SQLQuery": "SELECT SUM(stock_quantity) FROM cars WHERE model = 'SUV'",
        "SQLResult": "[(31,)]",
        "Answer": "31 SUV cars"
    },

    {
        "Question": "How many distinct models are there in the cars table?",
        "SQLQuery": "SELECT COUNT(DISTINCT model) FROM cars",
        "SQLResult": "[(4,)]",
        "Answer": "4 models"
    },

    {
        "Question": "List all car names by Honda.",
        "SQLQuery": "SELECT DISTINCT name FROM cars WHERE brand = 'Honda'",
        "SQLResult": "[('City',), ('WR-V',)]",
        "Answer": "City, WR-V"
    },

    {
        "Question": "What is the highest priced car in the inventory?",
        "SQLQuery": "SELECT name, price FROM cars ORDER BY price DESC LIMIT 1",
        "SQLResult": "[('Hilux', 3300000)]",
        "Answer": "Hilux, priced at 3,300,000"
    },

    {
        "Question": "Which cars have a discount greater than 15%?",
        "SQLQuery": "SELECT c.name, o.pct_discount FROM cars c JOIN offers o ON c.car_id = o.car_id WHERE o.pct_discount > 15",
        "SQLResult": "[('Endeavour', 15.0), ('Hilux', 20.0), ('Kona Electric', 18.5)]",
        "Answer": "Endeavour (15.0%), Hilux (20.0%), Kona Electric (18.5%)"
    },

    {
        "Question": "Which brands offer hybrid cars?",
        "SQLQuery": "SELECT DISTINCT brand FROM cars WHERE fuel_type = 'Hybrid'",
        "SQLResult": "[('Toyota',)]",
        "Answer": "Toyota"
    }
]
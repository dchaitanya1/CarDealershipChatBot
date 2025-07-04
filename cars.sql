CREATE DATABASE car_dealership;
USE car_dealership;

CREATE TABLE cars (
    car_id INT AUTO_INCREMENT PRIMARY KEY,
    brand varchar(100) NOT NULL,
    name varchar(100) NOT NULL,
    model ENUM('Sedan', 'SUV', 'Hatchback', 'Truck') NOT NULL,
    fuel_type ENUM('Petrol', 'Diesel', 'Electric', 'Hybrid') NOT NULL,
    price INT CHECK,
    stock_quantity INT NOT NULL,
    UNIQUE KEY brand_model_fuel (brand, model, fuel_type)
);

CREATE TABLE offers (
    offer_id INT AUTO_INCREMENT PRIMARY KEY,
    car_id INT NOT NULL,
    pct_discount DECIMAL(5,2) CHECK (pct_discount BETWEEN 0 AND 100),
    offer_start_date DATE NOT NULL,
    offer_end_date DATE NOT NULL,
    FOREIGN KEY (car_id) REFERENCES cars(car_id),
    CHECK (offer_end_date > offer_start_date)
);

INSERT INTO cars (car_id,brand, name, model, fuel_type, price, stock_quantity) VALUES
(1,'Toyota', 'Innova', 'SUV', 'Diesel', 2200000, 12),
(2,'Hyundai', 'i20', 'Hatchback', 'Petrol', 850000, 20),
(3,'Honda', 'City', 'Sedan', 'Petrol', 1200000, 15),
(4,'Ford', 'Endeavour', 'SUV', 'Diesel', 2900000, 5),
(5,'Toyota', 'Camry', 'Sedan', 'Hybrid', 3200000, 7),
(6,'Hyundai', 'Verna', 'Sedan', 'Petrol', 1100000, 10),
(7,'Honda', 'WR-V', 'SUV', 'Diesel', 1300000, 8),
(8,'Ford', 'Figo', 'Hatchback', 'Petrol', 750000, 14),
(9,'Toyota', 'Hilux', 'Truck', 'Diesel', 3300000, 4),
(10,'Hyundai', 'Kona Electric', 'SUV', 'Electric', 2300000, 6);




INSERT INTO offers (offer_id, car_id, pct_discount, offer_start_date, offer_end_date) VALUES
(1,1, 10.00, '2025-07-01', '2025-07-31'),
(2,2, 5.50, '2025-07-01', '2025-07-15'),
(3,3, 7.25, '2025-07-05', '2025-07-20'),
(4,4, 15.00, '2025-07-10', '2025-08-10'),
(5,5, 12.00, '2025-07-01', '2025-07-30'),
(6,6, 6.75, '2025-07-03', '2025-07-25'),
(7,7, 8.00, '2025-07-05', '2025-08-05'),
(8,8, 4.00, '2025-07-07', '2025-07-31'),
(9,9, 20.00, '2025-07-10', '2025-08-15'),
(10,10, 18.50, '2025-07-01', '2025-07-31');

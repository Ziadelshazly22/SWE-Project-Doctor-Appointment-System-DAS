-- To create a user in mysql DB
CREATE USER 'katy'@'localhost' IDENTIFIED BY 'katy';

-- To give all privilige to the new user
GRANT ALL PRIVILEGES ON *.* TO 'katy'@'localhost' WITH GRANT OPTION;

-- To create database
CREATE DATABASE clinical;

-- to view all databases
SHOW DATABASES;

-- To use specific database
USE clinical;

-- to create a user table
CREATE TABLE user(
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255)
    );


-- to create a doctor table
CREATE TABLE doctor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    major VARCHAR(255) NULL,
    certificate_path VARCHAR(255) NULL,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
    );

-- to create a nurse table
CREATE TABLE nurse (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    national_id INT(14) NOT NULL,
    contact_info INT(14) NOT NULL,
    CONSTRAINT fk_user_murse FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
    );


-- to create a patient table
CREATE TABLE patient(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    national_id INT(14) NOT NULL,
    gender BOOL DEFAULT TRUE,
    address VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    nationality VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL,
    CONSTRAINT fk_user_patient FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
    );


-- to create an appointment table
CREATE TABLE appointment (
    id INT PRIMARY KEY AUTO_INCREMENT,
    date DATE NOT NULL,
    time DATETIME NOT NULL,
    status VARCHAR(50) DEFAULT 'pending...',
    notes TEXT NULL,
    patient_id INT,
    CONSTRAINT fk_patient_appointment FOREIGN KEY (patient_id) REFERENCES user(id) ON DELETE CASCADE
);

-- to create an treatment table
CREATE TABLE treatment(
    id INT PRIMARY KEY AUTO_INCREMENT,
    date DATE NOT NULL,
    cost DOUBLE NOT NULL,
    description TEXT NULL,
    appointment_id INT,
    CONSTRAINT fk_treatment_appointment FOREIGN KEY (appointment_id) REFERENCES appointment(id) ON DELETE CASCADE
    );


-- to create an patient history table
CREATE TABLE patient_history (
    id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    appointment_id INT NOT NULL,
    treatment_id INT NOT NULL,
    visits_history TEXT,
    blood_type VARCHAR(20),
    latest_feedback TEXT,
    chronic_conditions TEXT,
    allergies TEXT,
    date DATE NOT NULL,  -- Assumed field for the date
    CONSTRAINT fk_patient_history FOREIGN KEY (patient_id) REFERENCES user(id) ON DELETE CASCADE,
    CONSTRAINT fk_appointment_history FOREIGN KEY (appointment_id) REFERENCES appointment(id) ON DELETE CASCADE,
    CONSTRAINT fk_treatment_history FOREIGN KEY (treatment_id) REFERENCES treatment(id) ON DELETE CASCADE
);


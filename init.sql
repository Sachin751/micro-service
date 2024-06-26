CREATE DATABASE IF NOT EXISTS cafe;
USE cafe;

CREATE TABLE IF NOT EXISTS cafe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    google_maps_url VARCHAR(255) NOT NULL,
    img_url VARCHAR(255) NOT NULL,
    suburb VARCHAR(255) NOT NULL,
    pricey VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255),
    website VARCHAR(255),
    menu VARCHAR(255)
);
GRANT ALL PRIVILEGES ON cafe.* TO 'liya'@'%';

FLUSH PRIVILEGES;

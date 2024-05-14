CREATE DATABASE profiles_db;

-- Conectar a la base de datos recién creada
\c profiles_db;

-- Crear la tabla de usuarios si no existe
CREATE TABLE IF NOT EXISTS profiles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    nickname VARCHAR(255) NOT NULL,
    public_info VARCHAR(255) NOT NULL,
    messaging VARCHAR(255) NOT NULL,
    biography VARCHAR(255) NOT NULL,
    organization VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    social_media VARCHAR(255) NOT NULL,
    email VARCHAR(255)
);


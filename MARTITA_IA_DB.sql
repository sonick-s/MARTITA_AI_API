-- Tabla de unidades organizacionales (departamentos, direcciones, etc.)
CREATE TABLE direcciones (
  id_direcciones INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(255) NOT NULL,
  descripcion TEXT,
  responsable VARCHAR(150),
  correo_responsable VARCHAR(150),
  telefono VARCHAR(100),
  fecha_actualizacion DATE
);

-- Tabla principal de trámites
CREATE TABLE tramites (
  id_tramite INT PRIMARY KEY AUTO_INCREMENT,
  id_unidad INT,
  nombre VARCHAR(255) NOT NULL,
  descripcion TEXT,
  contexto TEXT,
  requisitos TEXT,
  pasos TEXT,
  links_formularios TEXT,
  fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (id_unidad) REFERENCES direcciones(id_direcciones)
);

-- Tabla de usuarios que interactúan con el bot
CREATE TABLE usuarios (
  id_usuario INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  email VARCHAR(150),
  password VARCHAR(255) NOT NULL, 
  fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);


-- Historial de consultas de usuarios
CREATE TABLE interacciones (
  id_interaccion INT PRIMARY KEY AUTO_INCREMENT,
  pregunta TEXT,
  respuesta TEXT,
  respuesta_util TEXT DEFAULT NULL,
  fecha DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE prompts_bot (
  id_prompt INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(255) NOT NULL,               -- Nombre o propósito del prompt
  tipo VARCHAR(50),                           -- system, user, assistant, regla, contexto
  contenido TEXT NOT NULL,                    -- El texto del prompt/instrucción
  prioridad INT DEFAULT 0,                    -- Para ordenar si hay múltiples reglas
  fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
);


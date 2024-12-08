# Generador de Entidades JPA desde una Base de Datos MySQL

Este script genera automáticamente clases de entidad JPA en Java basadas en un esquema de base de datos MySQL.

## Características
- Genera clases con anotaciones JPA (`@Entity`, `@Table`, `@Column`).
- Detecta claves foráneas y agrega relaciones (`@ManyToOne`).
- Personalizable usando plantillas.

## Requisitos
- Python 3.x
- SQLAlchemy
- Jinja2
- MySQL Connector


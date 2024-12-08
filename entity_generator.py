from sqlalchemy import create_engine, inspect
from jinja2 import Environment, FileSystemLoader
import os

# Cargar configuración
from config import DATABASE_CONFIG

# Conectar a la base de datos
engine = create_engine(
    f"mysql+mysqlconnector://{DATABASE_CONFIG['user']}:{DATABASE_CONFIG['password']}@"
    f"{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}"
)

# Configurar Jinja2
env = Environment(loader=FileSystemLoader("templates"))

def generate_entities():
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    for table in tables:
        columns = inspector.get_columns(table)
        foreign_keys = inspector.get_foreign_keys(table)

        # Crear la entidad usando una plantilla
        template = env.get_template("java_entity.jinja2")
        java_code = template.render(
            table_name=table,
            columns=columns,
            foreign_keys=foreign_keys
        )

        # Guardar en archivo
        output_path = f"output/{table.capitalize()}.java"
        os.makedirs("output", exist_ok=True)
        with open(output_path, "w") as file:
            file.write(java_code)

        print(f"Clase generada: {output_path}")

if __name__ == "__main__":
    generate_entities()

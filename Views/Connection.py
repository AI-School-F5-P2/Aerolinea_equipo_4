import json
import mysql.connector
import streamlit as st

# Cargar datos de conexión
with open("./Credentials/DB.json", "r") as conn_data_file:
    data = json.load(conn_data_file)

# Función para ejecutar un archivo SQL
def execute_sql_file(connection, filename):
    try:
        with open(filename, "r") as sql_file:
            sql_script = sql_file.read()
            # Separa las instrucciones SQL en una lista usando el punto y coma como delimitador
            sql_statements = sql_script.split(';')
            cursor = connection.cursor()
            
            for sql_statement in sql_statements:
                if sql_statement.strip():  # Verifica que no sea una línea vacía
                    cursor.execute(sql_statement)
                    
            connection.commit()
    except mysql.connector.Error as e:
        st.error(f"Error al ejecutar el archivo SQL: {e}")
    finally:
        cursor.close()

def check_bbdd():
    # Configuración de la conexión al servidor MySQL sin especificar una base de datos
    db_config = {
        "host": data["SERVER"],
        "user": data["USER"],
        "password": data["PASSWORD"],
    }

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Verificar si la base de datos existe
        cursor.execute("SHOW DATABASES")
        databases = [database[0] for database in cursor]

        if data["DATABASE"] in databases:
            return conn
        else:
            # Crear la base de datos si no existe
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{data['DATABASE']}`")
            conn.commit()
            return conn

    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return None

    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()

def insert_data(conn, data):
    cursor = conn.cursor()
    
    query = """
        INSERT INTO data_client (id_passenger, Gender, Customer_Type, Age, Type_of_Travel, 
        Class, Flight_distance, Inflight_wifi_service, 
        datc, Ease_of_Online_booking, Gate_location, Food_and_drink,
        Online_boarding, Departure_delay_minutes, Seat_comfort, 
        Inflight_entertainment, Onboard_service, Leg_room_service, Baggage_handling, 
        Checkin_service, Inflight_service, Cleanliness, Arrival_delay_minutes) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    try:
        cursor.execute(query, (
            data["id_passenger"], data["Gender"], data["Customer_Type"], data["Age"], data["Type_of_Travel"],
            data["Class"], data["Flight_distance"], data["Inflight_wifi_service"], data["datc"],
            data["Ease_of_Online_booking"], data["Gate_location"], data["Food_and_drink"], data["Online_boarding"],
            data["Departure_delay_minutes"], data["Seat_comfort"], data["Inflight_entertainment"], data["Onboard_service"],
            data["Leg_room_service"], data["Baggage_handling"], data["Checkin_service"], data["Inflight_service"],
            data["Cleanliness"], data["Arrival_delay_minutes"]
        ))
        conn.commit()
    except mysql.connector.Error as e:
        st.error(f"Error al insertar datos: {e}")
    finally:
        cursor.close()
    
    return "Datos insertados correctamente en la tabla 'data_client'"

# Función para establecer la conexión
def establish_connection(data_form):
    conn = check_bbdd()
    
    if conn:
        conn.database = data["DATABASE"]  # Establece la base de datos
        execute_sql_file(conn, "./Credentials/airline.sql")
        insert_data(conn, data_form)
        conn.close()
        return "Conexión establecida correctamente"
    else:
        st.error("Error al conectar con la base de datos")
        return "Error al conectar con la base de datos"

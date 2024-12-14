import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request, jsonify

load_dotenv()

app = Flask(__name__)
url = os.environ.get("DATABASE_URL")

EXTRACT_CREW = """SELECT * FROM crew_crewrequirements LIMIT 1"""

@app.post("/crew_desc")
def crew_extraction():
    """
    Endpoint to extract crew description from the database.

    This function connects to a PostgreSQL database using psycopg2, executes a query to extract crew information,
    and returns the result as a JSON response.

    Returns:
        JSON response containing crew description with status code 200 if data is found.
        JSON response containing an error message with status code 404 if no data is found.
    """
    connection = psycopg2.connect(url)
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(EXTRACT_CREW)
                res = cursor.fetchone()
                print("fetched....", res, " fetched type....", type(res))
        if res:
            result_dict = {
                "project_name": res[1],
                "job_title": res[2],
                "skills": res[3],
                "specializations": res[4],
                "location": res[5],
                "start_date": res[6],
                "end_date": res[7]
            }
            return jsonify(result_dict), 200
        else:
            return jsonify({"error": "No data found"}), 404
    finally:
        connection.close()

EXTRACT_LOCATION = """SELECT location FROM crew_crewrequirements LIMIT 1"""

@app.post("/location")
def loc_extraction():
    """
    Endpoint to extract location data from the database.

    This function connects to a PostgreSQL database using psycopg2, executes a query to extract location data,
    and returns the result as a JSON response.

    Returns:
        JSON response containing the location data with a 200 status code if successful.
        JSON response containing an error message with a 404 status code if no location data is found.
    """
    connection = psycopg2.connect(url)
    try:
        location = None
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(EXTRACT_LOCATION)
                result = cursor.fetchall()
        if result is not None:
            location = result[0]
            print("fetched loc....", location)
            return jsonify({"location": location}), 200
        else:
            return jsonify({"error": "No location found"}), 404
    finally:
        connection.close()

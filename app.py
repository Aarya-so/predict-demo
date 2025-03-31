from flask import Flask, render_template, jsonify, request
import psycopg2

app = Flask(__name__)

# Connect to PostgreSQL Database
conn = psycopg2.connect(
    dbname="mydb",
    user="postgres",
    password="ap@calculas",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# 🏠 Route to render index.html
@app.route('/')
def home():
    return render_template('index.html')  # ✅ Now serves the frontend

# 📊 API Route for Pie Chart Data
@app.route('/get_pie_data', methods=['GET'])
def get_pie_data():
    try:
        district = request.args.get("district", "Kinnaur")  # Default to Pune
        query = """
            SELECT commodity, SUM(arrivals_tonnes) AS total_arrivals
            FROM commodity_data
            WHERE district_name = %s
            GROUP BY commodity
            ORDER BY total_arrivals DESC
            LIMIT 5;
        """
        cursor.execute(query, (district,))
        data = cursor.fetchall()

        # Convert query result to JSON format
        response = {
            "labels": [row[0] for row in data],
            "values": [row[1] for row in data]
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

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

@app.route('/')
def home():
    return render_template('cropdata.html')

@app.route('/apple')
def apple():
    # Fetch min_price & max_price before rendering
    cursor.execute("""
        SELECT MIN(min_price), MAX(max_price)
        FROM commodity_data
        WHERE commodity = 'Apple';
    """)
    result = cursor.fetchone()
    
    return render_template('apple.html', min_price=result[0], max_price=result[1])

# Fetch Pie Chart Data (Apple Varieties)
@app.route('/get_pie_data')
def get_pie_data():
    try:
        query = """
            SELECT variety, COUNT(*) as count
            FROM commodity_data
            WHERE commodity = 'Apple'
            GROUP BY variety;
        """
        cursor.execute(query)
        data = cursor.fetchall()

        response = {
            "labels": [row[0] for row in data],
            "values": [row[1] for row in data]
        }
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/tomato')
def tomato():
    # Fetch min_price & max_price before rendering
    cursor.execute("""
        SELECT MIN(min_price), MAX(max_price)
        FROM commodity_data
        WHERE commodity = 'Tomato';
    """)
    result = cursor.fetchone()
    
    return render_template('tomato.html', min_price=result[0], max_price=result[1])

# Fetch Pie Chart Data (Apple Varieties)
@app.route('/get_pie_data1')
def get_pie_data1():
    try:
        query = """
            SELECT variety, COUNT(*) as count
            FROM commodity_data
            WHERE commodity = 'Tomato'
            GROUP BY variety;
        """
        cursor.execute(query)
        data = cursor.fetchall()

        response = {
            "labels": [row[0] for row in data],
            "values": [row[1] for row in data]
        }
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/cauliflower')
def cauliflower():
    # Fetch min_price & max_price before rendering
    cursor.execute("""
        SELECT MIN(min_price), MAX(max_price)
        FROM commodity_data
        WHERE commodity = 'Cauliflower';
    """)
    result = cursor.fetchone()
    
    return render_template('cauliflower.html', min_price=result[0], max_price=result[1])

# Fetch Pie Chart Data (Apple Varieties)
@app.route('/get_pie_data2')
def get_pie_data2():
    try:
        query = """
            SELECT variety, COUNT(*) as count
            FROM commodity_data
            WHERE commodity = 'Cauliflower'
            GROUP BY variety;
        """
        cursor.execute(query)
        data = cursor.fetchall()

        response = {
            "labels": [row[0] for row in data],
            "values": [row[1] for row in data]
        }
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/pear')
def pear():
    # Fetch min_price & max_price before rendering
    cursor.execute("""
        SELECT MIN(min_price), MAX(max_price)
        FROM commodity_data
        WHERE commodity = 'Pear(Marasebu)';
    """)
    result = cursor.fetchone()
    
    return render_template('pear.html', min_price=result[0], max_price=result[1])


@app.route('/get_pie_data3')
def get_pie_data3():
    try:
        query = """
            SELECT variety, COUNT(*) as count
            FROM commodity_data
            WHERE commodity = 'Pear(Marasebu)'
            GROUP BY variety;
        """
        cursor.execute(query)
        data = cursor.fetchall()

        response = {
            "labels": [row[0] for row in data],
            "values": [row[1] for row in data]
        }
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/potato')
def potato():
    # Fetch min_price & max_price before rendering
    cursor.execute("""
        SELECT MIN(min_price), MAX(max_price)
        FROM commodity_data
        WHERE commodity = 'Potato';
    """)
    result = cursor.fetchone()
    
    return render_template('potato.html', min_price=result[0], max_price=result[1])


@app.route('/get_pie_data4')
def get_pie_data4():
    try:
        query = """
            SELECT variety, COUNT(*) as count
            FROM commodity_data
            WHERE commodity = 'Potato'
            GROUP BY variety;
        """
        cursor.execute(query)
        data = cursor.fetchall()

        response = {
            "labels": [row[0] for row in data],
            "values": [row[1] for row in data]
        }
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/peas')
def peas():
    # Fetch min_price & max_price before rendering
    cursor.execute("""
        SELECT MIN(min_price), MAX(max_price)
        FROM commodity_data
        WHERE commodity = 'Peas Wet';
    """)
    result = cursor.fetchone()
    
    return render_template('peas.html', min_price=result[0], max_price=result[1])


@app.route('/get_pie_data5')
def get_pie_data5():
    try:
        query = """
            SELECT variety, COUNT(*) as count
            FROM commodity_data
            WHERE commodity = 'Peas Wet'
            GROUP BY variety;
        """
        cursor.execute(query)
        data = cursor.fetchall()

        response = {
            "labels": [row[0] for row in data],
            "values": [row[1] for row in data]
        }
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/banana')
def banana():
    # Fetch min_price & max_price before rendering
    cursor.execute("""
        SELECT MIN(min_price), MAX(max_price)
        FROM commodity_data
        WHERE commodity = 'Banana';
    """)
    result = cursor.fetchone()
    
    return render_template('banana.html', min_price=result[0], max_price=result[1])


@app.route('/get_pie_data6')
def get_pie_data6():
    try:
        query = """
            SELECT variety, COUNT(*) as count
            FROM commodity_data
            WHERE commodity = 'Banana'
            GROUP BY variety;
        """
        cursor.execute(query)
        data = cursor.fetchall()

        response = {
            "labels": [row[0] for row in data],
            "values": [row[1] for row in data]
        }
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/cabbage')
def cabbage():
    # Fetch min_price & max_price before rendering
    cursor.execute("""
        SELECT MIN(min_price), MAX(max_price)
        FROM commodity_data
        WHERE commodity = 'Cabbage';
    """)
    result = cursor.fetchone()
    
    return render_template('cabbage.html', min_price=result[0], max_price=result[1])


@app.route('/get_pie_data7')
def get_pie_data7():
    try:
        query = """
            SELECT variety, COUNT(*) as count
            FROM commodity_data
            WHERE commodity = 'Cabbage'
            GROUP BY variety;
        """
        cursor.execute(query)
        data = cursor.fetchall()

        response = {
            "labels": [row[0] for row in data],
            "values": [row[1] for row in data]
        }
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/onion')
def onion():
    # Fetch min_price & max_price before rendering
    cursor.execute("""
        SELECT MIN(min_price), MAX(max_price)
        FROM commodity_data
        WHERE commodity = 'Onion';
    """)
    result = cursor.fetchone()
    
    return render_template('onion.html', min_price=result[0], max_price=result[1])


@app.route('/get_pie_data8')
def get_pie_data8():
    try:
        query = """
            SELECT variety, COUNT(*) as count
            FROM commodity_data
            WHERE commodity = 'Onion'
            GROUP BY variety;
        """
        cursor.execute(query)
        data = cursor.fetchall()

        response = {
            "labels": [row[0] for row in data],
            "values": [row[1] for row in data]
        }
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)}) 
    
@app.route('/cucumbar')
def cucumbar():
    # Fetch min_price & max_price before rendering
    cursor.execute("""
        SELECT MIN(min_price), MAX(max_price)
        FROM commodity_data
        WHERE commodity = 'Cucumbar(Kheera)';
    """)
    result = cursor.fetchone()
    
    return render_template('cucumbar.html', min_price=result[0], max_price=result[1])


@app.route('/get_pie_data9')
def get_pie_data9():
    try:
        query = """
            SELECT variety, COUNT(*) as count
            FROM commodity_data
            WHERE commodity = 'Cucumbar(Kheera)'
            GROUP BY variety;
        """
        cursor.execute(query)
        data = cursor.fetchall()

        response = {
            "labels": [row[0] for row in data],
            "values": [row[1] for row in data]
        }
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)

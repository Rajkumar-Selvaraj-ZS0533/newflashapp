from flask import Flask, render_template, jsonify
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/charts_data')
def charts_data():
    # Read data from Excel file
    excel_file_path = 'data/Demo.xlsx'  # Replace with the actual path to your Excel file
    df = pd.read_excel(excel_file_path)

    # Assuming the Excel file has columns named 'Category' and 'Value'
    categories = df['Category'].tolist()
    values = df['Value'].tolist()

    # Create a bar chart
    bar_chart = create_bar_chart(categories, values)

    # Create a pie chart
    pie_chart = create_pie_chart(categories, values)

    return jsonify({
        'bar_chart': bar_chart,
        'pie_chart': pie_chart
    })

def create_bar_chart(categories, values):
    plt.bar(categories, values)
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    chart_data = base64.b64encode(buffer.read()).decode('utf-8')
    return chart_data

def create_pie_chart(categories, values):
    plt.pie(values, labels=categories, autopct='%1.1f%%')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    chart_data = base64.b64encode(buffer.read()).decode('utf-8')
    return chart_data

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, send_file
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def home():
    # Read data from Excel file
    excel_file_path = 'path/to/your/excel/file.xlsx'  # Replace with the actual path to your Excel file
    df = pd.read_excel(excel_file_path)

    # Assuming the Excel file has columns named 'Category' and 'Value'
    categories = df['Category'].tolist()
    values = df['Value'].tolist()

    # Create a bar chart
    plt.bar(categories, values)

    # Save the plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Return the BytesIO object as an image file
    return send_file(buffer, download_name='chart.png', mimetype='image/png')

@app.route('/about')
def about():
    return 'About'

if __name__ == '__main__':
    app.run(debug=True)

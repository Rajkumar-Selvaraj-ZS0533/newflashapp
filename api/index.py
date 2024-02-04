from flask import Flask, send_file
import matplotlib.pyplot as plt
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def home():
    # Sample data
    categories = ['Category A', 'Category B', 'Category C']
    values = [20, 35, 25]

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

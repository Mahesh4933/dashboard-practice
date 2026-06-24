from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

@app.route('/')
def index():
    # Load your cleaned data
    df = pd.read_csv('data/clean_sales.csv')
    
    # Create an interactive chart using Plotly
    fig = px.bar(df, x='Month', y='Revenue', title='Monthly Revenue Overview')
    chart_html = pio.to_html(fig, full_html=False)
    
    # Render the page
    return f'''
        <h1>My Dashboard</h1>
        {chart_html}
    '''

if __name__ == '__main__':
    app.run(debug=True)
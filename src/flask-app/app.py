from flask import Flask, render_template_string
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)
developer = "Enitan Meduteni"

@app.route('/')
def hello_world():
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>DevSecOps - {developer}</title>
        <style>
            body {{
                background: linear-gradient(135deg, #4f8cff 0%, #a6e1fa 100%);
                min-height: 100vh;
                margin: 0;
                font-family: 'Segoe UI', Arial, sans-serif;
                display: flex;
                align-items: center;
                justify-content: center;
            }}
            .container {{
                background: rgba(255,255,255,0.95);
                border-radius: 18px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.18);
                padding: 48px 36px;
                text-align: center;
                max-width: 400px;
            }}
            h1 {{
                color: #2d3a4a;
                margin-bottom: 12px;
                font-size: 2.5rem;
            }}
            p {{
                color: #4f8cff;
                font-size: 1.2rem;
                margin-bottom: 0;
            }}
            .team-badge {{
                display: inline-block;
                background: #4f8cff;
                color: #fff;
                border-radius: 50px;
                padding: 8px 24px;
                font-size: 1.1rem;
                margin-top: 18px;
                letter-spacing: 1px;
                box-shadow: 0 2px 8px rgba(79, 140, 255, 0.15);
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to C-DAY 2025 Abhijit!</h1>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
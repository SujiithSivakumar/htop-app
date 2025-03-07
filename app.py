from flask import Flask
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get your full name (replace with your actual name)
    full_name = "Sujiith"

    # Get the system username
    username = subprocess.getoutput("whoami")

    # Get the current server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')

    # Get the output of the 'top' command
    top_output = subprocess.getoutput("top -b -n 1")

    # Format the HTML response
    html = f"""
    <html>
    <body>
    <h2>Name: {full_name}</h2>
    <h2>User: {username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <h2>Top Output:</h2>
    <pre>{top_output}</pre>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
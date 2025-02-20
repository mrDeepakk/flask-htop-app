from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getenv('USER', 'codespace')

    # Get current IST time
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')

    # Get `top` command output
    top_output = subprocess.getoutput('top -b -n 1')

    # Prepare HTML output
    html = f"""
    <pre>
    Name: Deepak Kumar
    Username: {username}
    Server Time (IST): {server_time}

    TOP output:
    {top_output}
    </pre>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

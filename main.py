from flask import Flask, render_template
from flask_socketio import SocketIO, send
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret@123')  # Use env var for security
socketio = SocketIO(app, cors_allowed_origins="*")  # Restrict in production if needed

@socketio.on('message')
def handle_message(message):
    print("Received message: " + message)
    if message != "User connected!":
        send(message, broadcast=True)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # Use Render's PORT
    socketio.run(app, host='0.0.0.0', port=port)  # Bind to 0.0.0.0
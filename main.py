from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import datetime
import eventlet
from llama_cpp import Llama
from transformers import AutoTokenizer
from threading import Lock

model_id = 'Bllossom/llama-3.2-Korean-Bllossom-3B'
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = Llama(
    model_path='llama-3.2-Korean-Bllossom-3B-gguf-Q4_K_M.gguf'
)
model_lock = Lock()

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
socketio.init_app(app, ping_interval=30, ping_timeout=180)


def generate_response(instruction):
    messages = [
        {"role": "user", "content": f"{instruction}"}
    ]

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    generation_kwargs = {
        "max_tokens": 512,
        "stop": ["<|eot_id|>"],
        "echo": True,
        "top_p": 0.9,
        "temperature": 0.6,
    }

    # Ensure thread-safe model access
    with model_lock:
        response_msg = model(prompt, **generation_kwargs)

    return response_msg['choices'][0]['text'][len(prompt):]

@app.route('/')
def hello():
    return render_template('index.html')


@socketio.on('connect')
def on_connect():
    """Handles a new client connection."""
    print(f"New client connected: {request.sid}")
    emit('connected', {'message': 'Connected to the server!'})


@socketio.on('disconnect')
def on_disconnect():
    """Handles client disconnection."""
    print(f"Client disconnected: {request.sid}")


@socketio.on('chat')
def handle_client_message(data):
    """
    Handles incoming messages from the client and responds to the same client.
    """
    client_sid = request.sid  # Unique session ID for each client
    print(f"Received message from {client_sid}: {data}")

    response = generate_response(data)  # Generate a response based on client input
    emit('server_response', {
        'message': response,
        'timestamp': datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    }, to=client_sid)  # Respond only to the sender


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 58084)), app)

from flask import Flask, render_template
from flask_socketio import SocketIO
import datetime
import eventlet
from llama_cpp import Llama
from transformers import AutoTokenizer

model_id = 'Bllossom/llama-3.2-Korean-Bllossom-3B'
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = Llama(
    model_path='llama-3.2-Korean-Bllossom-3B-gguf-Q4_K_M.gguf'
)

app = Flask(__name__)
socketio = SocketIO(app)
socketio.init_app(app, ping_interval=30, ping_timeout=180, cors_allowed_origins="*")


def generate_response(instruction):
    messages = [
        {"role": "user", "content": f"{instruction}"}
        ]

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize = False,
        add_generation_prompt=True
    )

    generation_kwargs = {
        "max_tokens":512,
        "stop":["<|eot_id|>"],
        "echo":True,
        "top_p":0.9,
        "temperature":0.6,
    }

    response_msg = model(prompt, **generation_kwargs)
    return response_msg['choices'][0]['text'][len(prompt):]


@app.route('/')
def hello():
    return render_template('index.html')


@socketio.on('chat')
def handle_client_message(data):
    """
    Handles incoming messages from the client.
    """
    print(f"Received message from client: {data}")
    # Example: Echo the message back to the client
    socketio.emit('server_response', {
        'message': f"{generate_response(data)}",
        'timestamp': datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    })


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 58084)), app)
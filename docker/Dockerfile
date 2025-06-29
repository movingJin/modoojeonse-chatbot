FROM python:3.10
LABEL maintainer="shdlehdwls@gmail.com"

WORKDIR /app
COPY ./main.py ./main.py
ADD ./model ./model
ADD ./templates ./templates

# Set up virtual environment and install dependencies
RUN pip install llama-cpp-python transformers
RUN pip install Flask flask_socketio eventlet

EXPOSE 58084
ENTRYPOINT ["python", "main.py"]
CMD ["--host=0.0.0.0"]

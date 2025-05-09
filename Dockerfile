FROM python:3.12-slim
RUN apt-get update && apt-get install -y tor build-essential
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app
CMD ["python","-m","flask","run","--host=0.0.0.0","--port","8000"]

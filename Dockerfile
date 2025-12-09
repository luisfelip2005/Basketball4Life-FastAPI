FROM python:3.9-slim-buster

WORKDIR /app

COPY . ./

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# sudo docker build -t fastapi .
# sudo docker run -p 3000:5000 fastapi
# http://localhost:3000/docs
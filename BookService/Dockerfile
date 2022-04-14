<<<<<<< HEAD
FROM python:3.10-slim-buster
=======
FROM python:3.10-slim
>>>>>>> 65c530dc3ff53bccb3ee14a8f4b31d4238c52a47

WORKDIR /BookService/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
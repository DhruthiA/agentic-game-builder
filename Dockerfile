FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install groq python-dotenv

CMD ["python", "main.py"]
FROM python:latest

WORKDIR /app

COPY entrypoint.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000
CMD [ "python", "entrypoint.py" ]
FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY ./books_store .

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0:8000"]

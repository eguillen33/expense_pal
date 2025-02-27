FROM python:3.12

WORKDIR /app

COPY . .

RUN --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["Python", "expense_pal.py"]
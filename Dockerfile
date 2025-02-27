FROM python:3.12

WORKDIR /app

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["Python3", "expense_pal.py"]
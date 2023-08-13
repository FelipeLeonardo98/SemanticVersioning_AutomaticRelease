FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5001

# ENV FLASK_ENV development

COPY app.py server_england.py ./

CMD [ "flask", "run", "--host", "0.0.0.0" ]
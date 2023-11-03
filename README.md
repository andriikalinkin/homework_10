# Hillel "homework_10" project

---
## How to launch the project
1. Install dependencies
```
pip install -r requirements.txt
```

2. Install Docker. Download "RabbitMQ" official, and run this broker
```
docker -d -p 5672:5672 --name rabbitmq --rm rabbitmq
```
3. Set your TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN environment variables and run worker process in the same terminal window.
```
export TWILIO_ACCOUNT_SID=<your_data>
export TWILIO_AUTH_TOKEN=<your_data>
celery -A homework_10 worker -l INFO
```
4. Set your TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN environment variables and run Django webserver in the same terminal window.
```
export TWILIO_ACCOUNT_SID=<your_data>
export TWILIO_AUTH_TOKEN=<your_data>
python manage.py runserver
```
6. Go to http://127.0.0.1:8000/sms/ in your browser and enter your phone number


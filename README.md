# Django ecommerce application 💲💲

Django web application that allows you to shop for groceries online!

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Javascript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![RabbitMQ](https://img.shields.io/badge/rabbitmq-%23FF6600.svg?&style=for-the-badge&logo=rabbitmq&logoColor=white)

## Features ⭐

- Browsing the list of products by category
- Adding products to the cart - session framework
- Placing an order
- Payment gateway integration - Braintree
- Sending an e-mail notification after placing an order
- Execution of asynchronous tasks using Celery
- Using RabbitMQ for handling message protocols
- Export of orders to CSV files
- Generating bills in PDF format - WeasyPrint
- Sending PDF documents via e-mail



## Environment Setup 🚀

Clone the repo:

```bash
  $ git clone https://github.com/ossker/ecommerce-app.git
```
```bash
  $ cd myshop
```

If virtualenv is not installed:

```bash
  $ pip install virtualenv
```

Create a virtual environment:
```bash
  python3 -m venv env
```

Activate the environment everytime you open the project:
```bash
  env/Scripts/activate
```

Install requirements:
```bash
  $ pip install -r requirements.txt
```

Run migrations for database:
```bash
  $ python manage.py makemigrations
```
```bash
  $ python manage.py migrate
```
Create superuser for admin login:

```bash
  $ python manage.py createsuperuser
```

Now you can run the server to see your application up & running 🚀
```bash
  $ python manage.py runserver
```

To exit the environment:
```bash
  $ deactivate
```

## Leave a ⭐ if you like 👨‍💻

FROM python:3.8.3

# set work directory
WORKDIR /currency_django

# install dependencies
RUN pip install --upgrade pip

COPY ./requirements_app.txt .
RUN pip install -r requirements_app.txt

COPY ./requirements_test.txt .
RUN pip install -r requirements_test.txt

ENTRYPOINT python manage.py runserver 0.0.0.0:8000
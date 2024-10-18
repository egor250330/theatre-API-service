# theatre-API-service

How to run:

1.Clone repository
git clone https://github.com/egor250330/theatre-API-service.git 

2.Create a virtual environment:
python -m venv venv

3.Activate the virtual environment:
On Windows:
venv\Scripts\activate

4.Install dependencies:
pip install -r requirements.txt

5.Apply migrations:
python manage.py migrate

6.Create a superuser account:
python manage.py createsuperuser

7.You are ready to run your server
python manage.py runserver
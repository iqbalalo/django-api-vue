# LeadPlus Test case of News data in Django

## Installation (MAC-OSX)
### Pre-requisits:
- Python >= 3.10
### Clone repository

```
git clone https://github.com/iqbalalo/django-test-leadplus.git
cd django-test-leadplus
```
### Active virtualenv and Install packages
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### DB Migration
```
cd src
python manage.py makemigrations
python manage.py migrate
```

### Set API Key before Download data

```
export API_KEY=Given API key

python manage.py download_news_data
```

### Run local server

```
python manage.py runserver
```

## URL navigation
There are two routes.

To get JSON data (Listing size is 100) 
```
/news
```
To get HTML View (Listing size is 20) 
```
/html/news
```

# 🐱 Django Cat Facts API Project

HNGi13 Backend Stage 0 API

This is my Stage 0 task for HNGi13 — built with Django and hosted on Railway.

## Live URL
https://hngi13-task-0-api-production.up.railway.app/api/me

## Stack
Python / Django

## Author
- Name: Joseph Akpan  
- Email: akpannath84@gmail.com  
- Track: Backend (Python/Django)

## Project Overview
A simple Django REST Framework API exposing `/api/me/`.  
Returns:
- Developer info (name, email, stack)  
- Current timestamp  
- A random cat fact from https://catfact.ninja/fact

## Features
- RESTful API endpoint  
- External API call with timeout/error handling  
- Environment-based configuration  
- Logging for debugging  
- CORS enabled for frontend access  

## Dependencies
- Django  
- djangorestframework  
- python-decouple  
- requests  

## Usage
```bash
git clone https://github.com/nathyjoe001/hngi13-task-0-api.git
cd hngi13-task-0-api
pip install -r requirements.txt
python manage.py runserver

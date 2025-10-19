# 🐱 Django Cat Facts API Project

## 📘 Project Overview
This is a simple Django REST Framework project that exposes an API endpoint `/api/me/`.  
When accessed, it returns:
- The developer’s profile info (name, email, stack)
- The current timestamp
- A random cat fact fetched from an external API (`https://catfact.ninja/fact`)

It includes:
- Graceful handling for external API failures or timeouts
- Environment variables for sensitive configurations
- Logging and CORS support
- Ready for deployment on [Railway.app](https://railway.app)

---

## ⚙️ Features
✅ RESTful API endpoint  
✅ External API call with timeout and error handling  
✅ Environment-based configuration  
✅ Logging for debugging  
✅ CORS headers enabled for frontend access  
✅ Docker-ready & deployable to Railway  

---

## 🏗️ Project Structure
catfact_project/
│
├── catfact_app/
│ ├── views.py
│ ├── urls.py
│ └── ...
│
├── catfact_project/
│ ├── settings.py
│ ├── urls.py
│ └── ...
│
├── manage.py
└── requirements.txt

---


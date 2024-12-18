# FastAPI Project Template by Fajri

This document provides a step-by-step guide to set up and run a FastAPI project.

---

## Setup Environment

1. Create a virtual environment:
   ```bash
   python3 -m venv env
   ```

2. Activate the virtual environment:
   ```bash
   source env/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install fastapi uvicorn sqlalchemy pymysql
   ```

---

## Running the Application

To start the FastAPI application, use the following command:
```bash
uvicorn main:app --reload
```

---

## Additional Features

### JWT Authentication

If you need JWT for authentication, install the required package:
```bash
pip install pyjwt
```

---

### Adding CORS for React or Other Frontend Applications

If you are integrating FastAPI with a frontend application (e.g., React), you can enable Cross-Origin Resource Sharing (CORS). Add the following code snippet to your `main.py` file:

```python
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:3000",  # Example for React application
    "https://example.com",    # Replace with your domain
]

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # List of allowed domains
    allow_credentials=True,         # Allow cookies or credentials
    allow_methods=["*"],            # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],            # Allow all headers
)
```

Replace `https://example.com` with your actual domain if deploying in production.

---

### Notes

- Ensure that all dependencies are installed in your virtual environment.
- Use a `.env` file to manage environment variables for sensitive data (e.g., database URLs, secret keys).

---

Happy coding with FastAPI! 🚀


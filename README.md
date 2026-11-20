# 🚀 FastAPI MLOps Journey

## 📖 Project Overview
This repository documents my journey from a Backend Engineer to an MLOps Engineer. It contains the foundational backend API that will eventually serve Machine Learning models in a production environment. 

The goal of this project is to build a robust, secure, and automated system following industry best practices.

## 🛠️ Tech Stack
*   **Language:** Python 3.12
*   **Framework:** FastAPI (for building high-performance APIs)
*   **Database:** SQLite (for lightweight, file-based data storage)
*   **Environment Management:** `python-dotenv` (for secure secrets management)
*   **Testing:** Pytest (for automated testing)

## ✨ Current Features
*   **Health Check:** A basic `GET` endpoint to verify the server is running.
*   **ML Mock Prediction:** A `POST` endpoint that accepts JSON data (simulating house features) and returns a calculated prediction.
*   **Prediction History:** A `GET` endpoint that retrieves all past predictions from the database.
*   **Error Handling:** Built-in validation to reject impossible data (e.g., negative square footage).
*   **Security:** Database connection strings are hidden using environment variables (`.env`).

## 🚀 How to Run This Project Locally

If you want to run this project on your own machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/moon121314/fastapi-mlops-journey.git
   cd fastapi-mlops-journey/Mlops

# Bug Prediction System

An end-to-end machine learning web application that predicts the risk of software bugs based on code change metrics.  
The system helps developers and testers identify risky commits early and prioritize code reviews and testing.

## Live Demo
- Frontend (AWS S3): [Add your S3 URL here]
- Backend API (Render): [Add your Render URL here]

---

## Features

- Predicts bug risk using machine learning
- Accepts real-world software engineering metrics
- Displays risk percentage and category (Low / Medium / High)
- Modern responsive UI built with React
- Cloud deployment with AWS S3 and Render
- Fast API integration between frontend and backend

---

## Tech Stack

### Frontend
- React
- Vite
- CSS / Tailwind (if used)

### Backend
- Python
- Flask
- Flask-CORS

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib

### Cloud / Deployment
- AWS S3 (Static Website Hosting)
- Render (Backend Hosting)
- GitHub

---

## Input Parameters

The model uses the following metrics:

- total_changes
- total_lines_added
- total_lines_deleted
- avg_complexity
- avg_loc
- num_authors
- bug_fix_commits

---

## Output

The system returns:

- Bug Risk Percentage
- Risk Level:
  - Low Risk
  - Medium Risk
  - High Risk
- Prediction Probability Score

---

## Example

### Input:
```json
{
  "total_changes": 8,
  "total_lines_added": 20,
  "total_lines_deleted": 5,
  "avg_complexity": 2,
  "avg_loc": 30,
  "num_authors": 1,
  "bug_fix_commits": 0
}

Deployment
Frontend

Hosted on AWS S3 Static Website Hosting

http://bug-prediction-frontend-gokul.s3-website.ap-south-1.amazonaws.com

Backend

Hosted on Render

https://bug-prediction-system-backend.onrender.com

Note: Backend may take a few seconds to wake up on first request.


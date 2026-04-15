# Bug Prediction System

## Overview
An end-to-end machine learning project that predicts the probability of bugs in software modules based on repository metrics.

## Tech Stack
- Frontend: React + Vite + Tailwind CSS
- Backend: Flask
- ML: Scikit-learn
- Containerization: Docker
- Cloud Deployment: Render
- Version Control: GitHub

## Features
- Predict bug risk using ML model
- Real-time API integration
- Interactive UI dashboard
- Cloud-hosted application
- Docker support

## Input Metrics
- total_changes
- total_lines_added
- total_lines_deleted
- avg_complexity
- avg_loc
- num_authors
- bug_fix_commits

## Output
- Bug Probability
- Risk Level

## Live Demo
Frontend: https://bug-prediction-system-frontend.onrender.com
Backend: https://dashboard.render.com/web/srv-d7frjvhf9bms73enl6tg

## Run Locally
```bash
docker compose up --build


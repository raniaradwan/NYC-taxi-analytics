# NYC Taxi Analytics Dashboard

## Project Overview

This project demonstrates an end-to-end Data Engineering pipeline for analyzing NYC Taxi trip data.

The pipeline ingests CSV data into Kafka, stores and analyzes it using ClickHouse, exposes REST APIs with FastAPI, and displays analytics through an HTML dashboard.

---

## Architecture

CSV Dataset
↓
Kafka Producer
↓
Kafka Topic
↓
ClickHouse Consumer
↓
ClickHouse Database
↓
FastAPI
↓
HTML Dashboard

---

## Technologies

- Python
- Apache Kafka
- ClickHouse
- FastAPI
- HTML
- Docker Compose

---

## Features

- Total number of taxi trips
- Top pickup areas
- Average fare calculation
- REST API endpoints
- Interactive dashboard

---

## API Endpoints

- /trips
- /top-areas
- /avg_fare

---

## Project Structure


main.py
index.html
docker-compose.yml
requirements.txt
README.md


---

## Author

*Rania Radwan*

LinkedIn:
https://www.linkedin.com/in/rania-s-radwan

GitHub:
https://github.com/raniaradwan

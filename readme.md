# Simple Web Application

This is a simple web application consisting of a **frontend (HTML, JavaScript)** and a **backend (Python Flask)**. The frontend fetches data from the backend and displays it in a table format.

## Project Structure
```
simple-web-app/
├── backend/
│   ├── app.py         # Backend application (Flask API)
│   ├── requirements.txt # Python dependencies
│   ├── Dockerfile     # Backend Dockerfile
├── frontend/
│   ├── index.html     # Frontend (HTML, JavaScript)
│   ├── script.js      # JavaScript to fetch data from backend
│   ├── Dockerfile     # Frontend Dockerfile
├── docker-compose.yml # Docker Compose file to run the app
└── README.md          # Project documentation
```

## Prerequisites
- Docker
- Docker Compose

## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/simple-web-app.git
cd simple-web-app
```

### 2. Run Using Docker Compose
```sh
docker-compose up --build
```
This command will build and start both the frontend and backend containers.

### 3. Access the Application
- **Frontend**: Open `http://localhost:8080`
- **Backend API**: Open `http://localhost:5000/api/data`

## API Endpoints
- `GET /api/data` - Returns JSON data for the frontend.

## Technologies Used
- **Frontend**: HTML, JavaScript, Fetch API
- **Backend**: Python, Flask
- **Docker**: Containerization
- **Docker Compose**: Managing multi-container application

## License
This project is licensed under the MIT License.

## Author
[Nandu Sathyan](https://github.com/pinnnacl/)



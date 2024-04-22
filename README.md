# My Awesome Project

This project is just a very small example for an end-to-end data science project

## Installation

To install the project, follow these steps:

```bash
git clone https://github.com/yourusername/your-repository.git
cd your-repository
pip install -r requirements.txt
```


## Run application

You can run the application locally using the following command:

```bash
uvicorn app.main:app --reload
```
Or 

using docker
```bash
docker build -t my-fastapi-app .
docker run -d -p 8000:8000 --name my-fastapi-container my-fastapi-app
```

Or

using docker-compose
```bash
docker-compose up --build
```
# FastAPI Stock Market App
This application is used to retrieve stock market data for different companies

...

## Getting Started

### Installation

Clone the repository:

   ```bash
   git clone https://github.com/jayprakash2999/stock-market
   cd stock-market

Create a copy of the environment variables file:
    cp .env.example .env
    
Install Mysql and create database and also the user and password
in dummy_data.py, there are dummy datas of various company. So, create a table with those fields and insert these records

Update the .env file with your desired configurations. Make sure to fill in sensitive information like database credentials.

Build and run the Docker containers:

docker-compose up --build

The app will start listening on localhost:8000
go to localhost:8000/docs to see all the APIs created and also use them to get company data

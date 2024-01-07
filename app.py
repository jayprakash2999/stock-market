from fastapi import FastAPI, HTTPException, Depends
from mysql.connector import connect, Error
from database.database import get_database
from models.company_details import CompanyDetails

import uvicorn

app = FastAPI()


@app.get('/')
def index():
    return {'name': 'JP'}


@app.get('/company-detail/{symbol}')
async def company_details(symbol: str, db: connect = Depends(get_database)):
    cursor = db.cursor(dictionary=True)

    try:
        query = "SELECT * FROM company_details WHERE symbol = %s"
        cursor.execute(query, (symbol,))
        result = cursor.fetchone()

        if result is None:
            raise HTTPException(status_code=404, detail="Company not found")

        company_data = CompanyDetails(**result)
        return {'data': company_data, 'error': False}
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        cursor.close()


@app.get("/related_symbols/{symbol}")
async def get_related_symbols(symbol: str, db: connect = Depends(get_database)):
    cursor = db.cursor(dictionary=True)

    try:
        # Retrieve symbols that contain the provided symbol as a substring
        query = "SELECT symbol FROM company_details WHERE symbol LIKE %s"
        cursor.execute(query, (f"%{symbol}%",))
        related_symbols = [result["symbol"] for result in cursor.fetchall()]

        # Retrieve data for each related symbol
        related_data = {}
        for related_symbol in related_symbols:
            query = "SELECT * FROM company_details WHERE symbol = %s"
            cursor.execute(query, (related_symbol,))
            result = cursor.fetchone()

            if result is not None:
                related_data[related_symbol] = CompanyDetails(**result)

        return {'data': related_data, 'error': False}
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        cursor.close()

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

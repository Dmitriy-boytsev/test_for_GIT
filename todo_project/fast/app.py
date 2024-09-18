import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/api/users/{user_id}")
async def get_user_info(user_id: int):
    url = f"http://localhost:8000/api/users/{user_id}/"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError:
            raise HTTPException(status_code=response.status_code, detail="User not found")
        except httpx.RequestError:
            raise HTTPException(status_code=500, detail="API server is unreachable")

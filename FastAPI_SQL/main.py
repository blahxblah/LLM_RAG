
from fastapi import FastAPI

from lib import models
from lib.database import engine
from routers.routers import router

import uvicorn

# 데이터베이스 테이블 생성하기
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
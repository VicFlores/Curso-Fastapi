from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from middleware.error_handler import ErrorHandler
from routes.movies import movie_router
from routes.users import user_router

app = FastAPI()

app.title = 'Mi aplicación con FastAPI'
app.version = '0.0.1'
app.description = 'Esta es una aplicación de ejemplo con FastAPI'

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)


@app.get('/', tags=['Home'])
def message():
    return JSONResponse(content={"message": "Welcome to my FastAPI"}, status_code=status.HTTP_200_OK)

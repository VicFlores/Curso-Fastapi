from fastapi import APIRouter, HTTPException, Path, Query, status, Depends
from typing import List
from fastapi.responses import JSONResponse
from middleware.jwt_bearer import JWTBearer
from schema.movies import Movie
from services.movie import MovieService

movie_router = APIRouter()


@ movie_router.get('/movies', tags=['Movies'], response_model=List[Movie], dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    res = MovieService.get_movies()

    return JSONResponse(content=res, status_code=status.HTTP_200_OK)


@ movie_router.get('/movies/{movie_id}', tags=['Movies'], response_model=Movie)
def get_movie(movie_id: int = Path(ge=1, le=100)) -> Movie:

    res = MovieService.get_movie(movie_id)

    if res:
        return JSONResponse(content=res, status_code=status.HTTP_200_OK)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Movie not found")


@ movie_router.get('/movies/', tags=['Movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=4, max_length=15)) -> List[Movie]:

    res = MovieService.get_movies_by_category(category)

    if res:
        return JSONResponse(content=res, status_code=status.HTTP_200_OK)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Category not found")


@ movie_router.post('/movies', tags=['Movies'], response_model=dict)
def create_movie(movie: Movie) -> dict:

    MovieService.create_movie(movie)

    return JSONResponse(content={"message": "Se ha creado la pelicula"}, status_code=status.HTTP_201_CREATED)


@ movie_router.put('/movies/{movie_id}', tags=['Movies'], response_model=dict)
def update_movie(movie_id: int, movie: Movie) -> dict:

    res = MovieService.update_movie(movie_id, movie)

    if res:
        return JSONResponse(content=res, status_code=status.HTTP_200_OK)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Movie not found")


@ movie_router.delete('/movies/{movie_id}', tags=['Movies'], response_model=dict)
def delete_movie(movie_id: int) -> dict:

    res = MovieService.delete_movie(movie_id)

    if res:
        return JSONResponse(content=res, status_code=status.HTTP_200_OK)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Movie not found")

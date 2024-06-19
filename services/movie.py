from schema.movies import Movie


movies = [
    {
        "id": 1,
        "title": "The Shawshank Redemption",
        "overview": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        "year": 1994,
        "rating": 9.3,
        "category": "Drama"
    },
    {
        "id": 2,
        "title": "The Godfather",
        "overview": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
        "year": 1972,
        "rating": 9.2,
        "category": "Crime"
    },
    {
        "id": 3,
        "title": "The Dark Knight",
        "overview": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
        "year": 2008,
        "rating": 9.0,
        "category": "Action"
    },
    {
        "id": 4,
        "title": "Inception",
        "overview": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
        "year": 2010,
        "rating": 8.8,
        "category": "Action"
    }
]


class MovieService:

    def get_movies():
        return movies

    def get_movie(movie_id: int):
        for movie in movies:
            if movie['id'] == movie_id:
                return movie

        return None

    def get_movies_by_category(category: str):
        moviesByCategory = [
            item for item in movies if item['category'] == category]

        return moviesByCategory

    def create_movie(movie: Movie):
        movie.id = len(movies) + 1
        movies.append(movie.model_dump())

        return {"message": "Se ha creado la pelicula"}

    def update_movie(movie_id: int, movie: Movie):
        for item in movies:
            if item['id'] == movie_id:
                item['title'] = movie.title
                item['overview'] = movie.overview
                item['year'] = movie.year
                item['rating'] = movie.rating
                item['category'] = movie.category
                return {"message": "Se ha modificado la pelicula"}

        return None

    def delete_movie(movie_id: int):
        for movie in movies:
            if movie['id'] == movie_id:
                movies.remove(movie)
                return {"message": "Se ha eliminado la pelicula"}

        return None

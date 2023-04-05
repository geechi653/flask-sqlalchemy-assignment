class MovieRepository:

    def __init__(self, db_url):
        engine = create_engine(db_url)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get_all_movies(self):
        movies = self.session.query(Movie).all()
        return movies

    def get_movie_by_id(self, movie_id):
        movie = self.session.query(Movie).get(movie_id)
        return movie

    def create_movie(self, title, director, rating):
        movie = Movie(title=title, director=director, rating=rating)
        self.session.add(movie)
        self.session.commit()
        return movie.id

    def search_movies(self, title):
        movies = self.session.query(Movie).filter(Movie.title.ilike(f'%{title}%')).all()
        return movies

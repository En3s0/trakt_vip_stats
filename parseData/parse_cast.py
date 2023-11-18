from sqlmodel import Session, create_engine, select
from Models.cast_model import Cast

engine = create_engine("sqlite:///database.db")

def most_watched_actors():
    actors = []

    with Session(engine) as session:
        for cast_data in session.exec(select(Cast.id, Cast.name, Cast.movies, Cast.shows, Cast.episode).where(Cast.gender == 2).order_by((Cast.movies_count + Cast.shows_count).desc()).order_by(Cast.episode)):
            id, name, movies, shows, episode_count = cast_data
            actors.append({id: {
                'name': name,
                'movies': movies,
                'shows': shows,
                'episode': episode_count
            }})
    
    actors = actors[:100]

    return actors

def most_watched_actresses():
    actresses = []

    with Session(engine) as session:
        for cast_data in session.exec(select(Cast.id, Cast.name, Cast.movies, Cast.shows, Cast.episode).where(Cast.gender == 1).order_by((Cast.movies_count + Cast.shows_count).desc()).order_by(Cast.episode)):
            id, name, movies, shows, episode_count = cast_data
            actresses.append({id: {
                'name': name,
                'movies': movies,
                'shows': shows,
                'episode': episode_count
            }})
    
    actresses = actresses[:100]

    return actresses

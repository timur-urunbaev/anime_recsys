import polars as pl

class MAL_Schemas:

    @staticmethod
    def anime():
        schema = {
            'MAL_ID': pl.Int64,
            'Name': pl.String,
            'Score': pl.Float32,
            'Genres': pl.String,
            'English name': pl.String,
            'Japanese name': pl.String,
            'Type': pl.String,
            'Episodes': pl.Int64,
            'Aired': pl.String,
            'Premiered': pl.String,
            'Producers': pl.String,
            'Licensors': pl.String,
            'Studios': pl.String,
            'Source': pl.String,
            'Duration': pl.String,
            'Rating': pl.String,
            'Ranked': pl.Float32,
            'Popularity': pl.Int64,
            'Members': pl.Int64,
            'Favorites': pl.Int64,
            'Watching': pl.Int64,
            'Completed': pl.Int64,
            'On-Hold': pl.Int64,
            'Dropped': pl.Int64,
            'Plan to Watch': pl.Int64,
            'Score-10': pl.Float32,
            'Score-9': pl.Float32,
            'Score-8': pl.Float32,
            'Score-7': pl.Float32,
            'Score-6': pl.Float32,
            'Score-5': pl.Float32,
            'Score-4': pl.Float32,
            'Score-3': pl.Float32,
            'Score-2': pl.Float32,
            'Score-1': pl.Float32
        }
        return schema
    
    @staticmethod
    def animelist():
        schema = {
            'user_id': pl.Int64,
            'anime_id': pl.Int64,
            'rating': pl.Int64,
            'watching_status': pl.Int64,
            'watched_episodes': pl.Int64 
        }
        return schema

    @staticmethod
    def rating():
        schema = {
            'user_id': pl.Int64,
            'anime_id': pl.Int64,
            'rating': pl.Int64
        }
        return schema
    

    @staticmethod
    def anime_with_synopsis():
        schema = {
            'MAL_ID': pl.Int64,
            'Name': pl.String,
            'Score': pl.Float64,
            'Genres': pl.String,
            'sypnopsis': pl.String
        }
        return schema

    @staticmethod
    def watching_status():
        schema = {
            'status': pl.Int64,
            ' description': pl.String
        }
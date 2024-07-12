import strawberry
from .types.playlist import Playlist

#resovler or in OOP terms this is our "getter"
#def get_hello():
 #   return "Hello world"

#equivalent of our query
@strawberry.type
class Query:
    @strawberry.field(description="Playlists hand-picked to be features to all users")
    def features_playlists(self) -> list[Playlist]:
        return [
            Playlist(id="1", name="GraphQL Groovin'", description=None),
            Playlist(id="2", name="Graph Explorer Jams", description=None),
            Playlist(id="3", name="Interpretive GraphQL Dance", description=None),
        ]
    #hello: str = strawberry.field(resolver=get_hello)



"""
examples of other GraphQL tools. 
Probably would make new files to separate them out

class Mutation:
    @strawberry.field()
    def update_field_name(self) -> list[fields]:
        return[]
        
class Subscription:
    @strawberry.field()
        def get_real_time(self) -> list[]:
            return 
            [
            
            ]
"""
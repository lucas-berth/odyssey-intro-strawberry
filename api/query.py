import strawberry
from .types.playlist import Playlist
from mock_spotify_rest_api_client.api.playlists import get_featured_playlists
from mock_spotify_rest_api_client.api.playlists import get_playlist

#resovler or in OOP terms this is our "getter"
#def get_hello():
 #   return "Hello world"

#equivalent of our query
@strawberry.type
class Query:
    @strawberry.field(description="Playlists hand-picked to be features to all users")
    async def features_playlists(self, info: strawberry.Info) -> list[Playlist]:
        spotify_client = info.context["spotify_client"]
        data = await get_featured_playlists.asyncio(client=spotify_client)
        
        return  [
            Playlist(
                id=strawberry.ID(playlist.id),
                name=playlist.name,
                description=playlist.description
            )
            for playlist in data.playlists.items
        ]
    

    @strawberry.field(description="Retrieves a specific playlist.")
    async def playlist(self,
            id: strawberry.ID,
            info: strawberry.Info
            ) -> Playlist | None:
                spotify_client = info.context["spotify_client"]
                data = await get_playlist.asyncio(client=spotify_client, playlist_id=id)
                
                if data is None:
                        return None
                
                return Playlist(
                        id=strawberry.ID(data.id),
                        name=data.name,
                        description=data.description
                )
        


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
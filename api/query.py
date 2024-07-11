import strawberry


def get_hello():
    return "Hello world"

#equivalent of our query
@strawberry.type
class Query:
    hello: str = strawberry.field(resolver=get_hello)

#resovler or in OOP terms this is our "getter"


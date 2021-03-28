import graphene
import gamLog.schema.user
import gamLog.schema.feed
import gamLog.schema.auth

class Query(
    gamLog.schema.user.Query,
    gamLog.schema.feed.Query, # Add your Query objects here
    graphene.ObjectType
):
    pass

class Mutation(
    gamLog.schema.user.Mutation, 
     gamLog.schema.feed.Mutation,# Add your Mutation objects here
    gamLog.schema.auth.Mutation,# Add your Mutation objects here
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)




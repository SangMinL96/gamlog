import graphene
from graphene_django import DjangoObjectType

from gamLog.models.feed_model import FeedModel


class FeedType(DjangoObjectType):
    class Meta:
        model = FeedModel
class Query(graphene.ObjectType):
    feeds = graphene.List(FeedType)
    def resolve_feeds(self, info):
        return FeedType.objects.all()



class CreateFeed(graphene.Mutation):
    id = graphene.Int()
    user_id = graphene.String()
    content = graphene.String()

    class Arguments:
        user_id = graphene.String()
        content = graphene.String()

    def mutate(self, info, user_id, content):
   
        feed = FeedModel(user_id=user_id, content=content)
        feed.save()

        return CreateFeed(
            id=feed.id,
            user_id=feed.first_name,
            content=feed.last_name,
        )

class Mutation(graphene.ObjectType):
    CreateFeed = CreateFeed.Field()

schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)
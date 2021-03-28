import graphene
from graphene_django import DjangoObjectType

from gamLog.models.user_model import UserModel



class UserType(DjangoObjectType):
    class Meta:
        model = UserModel
        fields = "__all__"
        
class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    users_by_id = graphene.Field(UserType, id=graphene.String())
    def resolve_users(self, info):
     
        return UserModel.objects.all()
    def resolve_users_by_id(root, info, id):
        print(id)
        # Querying a single question
        return UserModel.objects.get(pk=id)



class CreateUser(graphene.Mutation):
    id = graphene.Int()
    userId = graphene.String()
    pw = graphene.String()
 
    class Arguments:
        userId = graphene.String()
        pw = graphene.String()

    def mutate(self, info, userId, pw):
        
        user = UserModel(userId=userId, pw=pw)
        print(userId)
        user.save()
         
        return CreateUser(
            id=user.id,
            userId=user.userId,
            pw=user.pw,
        )

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)
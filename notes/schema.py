from django.conf import settings
from graphene_django import DjangoObjectType
import graphene_django 
from .models import Note as NoteModel

class Note(DjangoObjectType):
    class Meta:
        model = NoteModel
        interface = (graphene.relay.Node, )

class Query(graphene.DjangoObjectType):
    notes = graphene.List(Note)

    def resolve_notes(self, info):
        ""Decide which noted to return""

        user = info.context.user
        
        if settings.DEBUG:
            return NoteModel.objects.all()
        elif user.is_anonymous:
            return NoteModel.objects.none()
        else:
            NoteModel.objects.filter(user=user)

#Add a schema and attch the query
schema = graphene.Schema(query=Query)
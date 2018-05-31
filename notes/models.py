
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Author
    title = models.CharField(max_length=200)
    content= models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

#stretch goal ideas":
#Tags/Categories
#sharing notes between users
#hook into bookmarks somehow?
#file attachment uploads

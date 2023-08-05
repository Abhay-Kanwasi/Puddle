from django.contrib.auth.models import User
from django.db import models
from item.models import Item

class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    # Wants many users
    members = models.ManyToManyField(User, related_name='conversations')
    # When it created
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at', )


class ConversationMessage(models.Model):
    # When item deleted all conversation related to item will also be deleted
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # If user deleted delete all messages assosiated with him
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
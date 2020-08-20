from django.db import models


class Fingers(models.Model):
    user_id = models.IntegerField(primary_key=True, db_index=True)
    hash_finger = models.TextField()

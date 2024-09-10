""" Users profile model for Portfolio application """

from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

class Profile(models.Model):
    """ Add some fields to built-in Django user class """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = ProcessedImageField(
        upload_to='avatars',
        processors=[ResizeToFill(256, 256)],
        format='JPEG',
        options={'quality': 90},
        default='default_avatar.jpg'
    )
    avatar_thumbnail = ImageSpecField(source='avatar',
        processors=[ResizeToFill(32, 32)],
        format='JPEG',
        options={'quality': 90}
    )

    def __str__(self):
        """ Show user name """
        return self.user.username

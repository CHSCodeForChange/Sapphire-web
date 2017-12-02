from django.db import models
from django.contrib.auth.models import User


# Custom Profile linked to a User
class Profile(models.Model):
    # The manager to get Profile objects
    objects = models.Manager()
    # The primary key
    # uid = models.IntegerField(primary_key=True)
    timezone = models.CharField(max_length=50, default='EST')
    # A one to many relationship to team members that is connected when the
    # Profile is a TEAM_LEADER with people in their team.
    team = models.ForeignKey(
    'self',
    models.CASCADE
    )
    # The user variable to allow authentication to work
    # user = models.OneToOneField(User)
    #
    bio = models.CharField(max_length=1000)
    hours = models.IntegerField()
    def Profile():
        # self.uid = uid
        self.hours = 0

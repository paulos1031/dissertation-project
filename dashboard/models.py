from django.db import models


class UserData(models.Model):
    rank_position = models.IntegerField()
    first_name = models.CharField(max_length=30, unique=True)
    calls_answered = models.IntegerField()
    tickets_closed = models.IntegerField()
    average_survey_score = models.FloatField(max_length=6)
    counter_queries_taken = models.IntegerField()
    chats_taken = models.IntegerField()
    breached_tickets = models.IntegerField()
    total_score = models.FloatField(max_length=20)

    def __str__(self):
        return f'{self.first_name}'

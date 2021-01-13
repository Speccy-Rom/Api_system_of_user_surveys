from django.db import models


class Survey(models.Model):
    survey_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    end_date = models.DateTimeField()
    survey_description = models.CharField(max_length=200)

    def __str__(self):
        return self.survey_name


class Question(models.Model):
    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    user_id = models.IntegerField()
    survey = models.ForeignKey(Survey, related_name='survey', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='question', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name='choice', on_delete=models.CASCADE, null=True)
    choice_text = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.choice_text

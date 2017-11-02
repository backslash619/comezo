from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone

TAGS_TYPE = {
    (1, "Math"),
    (2, "Chemistry"),
    (3, "Physics"),
    (4, "Biology"),
    (5, "English"),
}


class Tags(models.Model):
    name = models.CharField(max_length=255)
    type = models.IntegerField(choices=TAGS_TYPE)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return '%s %s' % (self.name, self.type)


class Questions(models.Model):
    created_by = models.ForeignKey(User, related_name="ques_created_by")
    created_at = models.DateTimeField(default=timezone.now)
    q_text = models.TextField(max_length=1000)
    tags = models.ManyToManyField(Tags, related_name="tags")
    hint = models.CharField(max_length=255 ,default="", blank=True)

    class Meta:
        verbose_name_plural = "Questions"

    def __str__(self):
        return '%s %s' % (self.q_text, self.created_by)


class Answers(models.Model):
    question = models.ForeignKey(Questions, related_name="related_question")
    a_text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Answers"

    def __str__(self):
        return '%s %s' % (self.a_text, self.question)
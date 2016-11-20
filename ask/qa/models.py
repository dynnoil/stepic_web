#-*-coding: utf-8-*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

##
# Question model manager
##
class QuestionManager(models.Manager):
	def new(self):
		qs = self.get_queryset()
		return qs.order_by('-added_at')
	def popular(self):
		qs = self.get_queryset()
		return qs.order_by('rating')		

##
# Question
##
class Question(models.Model):
	title = models.CharField(max_length = 255)
	text = models.TextField()
	added_at = models.DateTimeField(blank = True)
	rating = models.IntegerField(default = 0)
	author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'question_author')
	likes = models.ManyToManyField(User, related_name = 'question_likes')
	objects = QuestionManager()

	def __unicode__(self):
		return self.title

	def get_url(self):
		return reverse('question', kwargs = {'id': self.id})

class AnswerManager(models.Manager):
	def get_question(self, question):
		qs = self.get_queryset()
		return qs.filter(question__id = question.id)

##
# Answer
##
class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(blank = True)
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	objects = AnswerManager()

	def __unicode__(self):
		return self.text
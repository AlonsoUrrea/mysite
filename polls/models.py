import datetime # added by coder

from django.db import models
from django.utils import timezone # added by coder

# Create your models here.
class Question(models.Model): # Question model
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') # 1st arg is human-readable name of the field

    def __str__(self) -> str: # string representation
        return "%s" %self.question_text
    #end __str__

    def was_published_recently(self) -> bool:
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    #end def
#end Question


class Choice(models.Model): # Choice model
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # associated to a Question object 
                                                                     # note the m.ForeignKey type here
    choice_text = models.CharField(max_length=200) # max length of the field
    votes = models.IntegerField(default=0) #default value

    def __str__(self) -> str: # string representation
        return "%s" %self.choice_text
    #end __str__
#end Choice
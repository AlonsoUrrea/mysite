# Here, the server responses are created and sent to the client as a HTML sheet via HTTP

from django import template
from django.http import HttpResponse # came in the template
from django.http.response import Http404, HttpResponseRedirect # To catch error 404
from django.template import loader # import the loader for templates!
from django.urls import reverse # import function to return HttpResponseRedirect in the POST views
from django.shortcuts import get_object_or_404, render # this is a shortcut for HttpResponses

from .models import Question, Choice # import the model for Question


def index(request): # See all the questions in the polls
    lastest_questions = Question.objects.order_by('-pub_date')[:10] # fetch the lastest 10 questions
    template = loader.get_template('polls/index.html') # load the template
    context = {
        'latest_question_list': lastest_questions,  # variables used within the template
    }

    return HttpResponse(template.render(context, request)) # send the render and stuff
#end def

def detail(request, question_id): # see the details of a especific question
    try:
        question = Question.objects.get(pk=question_id) # search the question by it's PK
    except Question.DoesNotExist:
        raise Http404('Question does not exist') # If question is not found, send the 404 response
    
    template = loader.get_template("polls/detail.html") # load the HTML template
    context = { 'question': question } # variables within the template

    return HttpResponse(template.render(context, request)) # fill the HTML template with the response
#end def

def results(request, question_id): # display results for Question in polls
    question = get_object_or_404(Question, pk=question_id) # get Question object or return 404 error
    template = loader.get_template("polls/results.html") # load template from file
    context = {'question' : question} # variables for the template

    return HttpResponse(template.render(context, request)) # return response to client
#end def

def vote(request, question_id): # React to POST form from detail
    question = get_object_or_404(Question, pk=question_id) # get the object Question by PK or throw 404 error

    try:
        select_choice = question.choice_set.get( # find the choice thar the user selected
            pk=request.POST['choice'] # extract PK from POST request key
        )
    except (KeyError, Choice.DoesNotExist): # catch the not existing POST variable or Choice error
        template = loader.get_template("polls/detail.html") # load the HTML template
        context = { # variables within the template
            'question': question,
            'error_message': 'You didn\'t select a valid choice' 
        }

        return HttpResponse(template.render(context, request)) # fill the HTML template with the response
    #end try

    select_choice.votes += 1 # the votes field increments by one in the Choice object
    select_choice.save() # save changes in the object to the DB

    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
        # Note: reverse('<URL>', (vars,,,):tuple<?>)
    return HttpResponseRedirect(
        reverse('polls:results' # contructor reverse for URLs; View name for redirect as defined in urls.py
        , args=(question.id, ) ) # arguments for the view, as defined in urls.py
        )
#end def
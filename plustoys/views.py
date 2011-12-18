# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    return render_to_response("plustoys/home.html", {
        "toys_list": 
        [{
            "name": "User Badge Generator for Google+",
            "url": reverse("plusbadges_home")
        }]
        #[{
            #"name": "User Badge Generator for Google+",
            #"url": reverse("plusbadges_home")
        #},
        #{
            #"name": "Trello Holodeck for Google+ Hangouts (only the name is fancy, the toy is very simplistic!)",
            #"url": "/hangoutapps/#h-trello-holodeck"
        #}]
    }, context_instance=RequestContext(request))


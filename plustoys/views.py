# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    return render_to_response("plustoys/home.html", {
        "toys_list": 
        [{
            "name": "User Badge Generator",
            "url": reverse("plusbadges_home")
        },
        {
            "name": "Trello Holodeck (only the name is fancy, the toy is very simplistic!)",
            "url": "/hangoutapps/"
        }]
    }, context_instance=RequestContext(request))


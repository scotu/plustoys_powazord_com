# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def home(request):
    return HttpResponseRedirect(reverse("plusbadges_home"))
            


#!/usr/bin/env python3

# Copyright (c) 2016 PyWPS Project Steering Committee
# 
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# PyWPS process import

from .processes.sleep import Sleep
from .processes.ultimate_question import UltimateQuestion
from .processes.centroids import Centroids
from .processes.sayhello import SayHello
from .processes.feature_count import FeatureCount
from .processes.buffer import Buffer
from .processes.area import Area
from .processes.bboxinout import Box
from .processes.jsonprocess import TestJson

#PyWPS import service for application creation
from pywps import Service
processes = [
    FeatureCount(),
    SayHello(),
    Centroids(),
    UltimateQuestion(),
    Sleep(),
    Buffer(),
    Area(),
    Box(),
    TestJson()
]


# For the process list on the home page

process_descriptor = {}
for process in processes:
    abstract = process.abstract
    identifier = process.identifier
    process_descriptor[identifier] = abstract

# This is how you start PyWPS instance as WSGI that is return to the Django project's urls.py
# if the pywps.cfg is inside the app then we need to use ./pywpsApp/pywps.cfg 
application = Service(processes, ['./pywps.cfg'])

#DJANGO
from django.views.generic import TemplateView # Import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"
    # we could have used process_desciptor as a sort of model
    def get_context_data(self, **kwargs):
        return {"process_descriptor":process_descriptor}



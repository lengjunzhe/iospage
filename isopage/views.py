# coding:utf-8
from django.shortcuts import render_to_response, redirect
from django.template import Template, Context
from django.template import RequestContext
import time, re


def simple(request):  # simplepx/模版
    return render_to_response('simple.html', context_instance=RequestContext(request))

def simplechinese(request):  # simplepx/模版
    return render_to_response('simplechinese.html', context_instance=RequestContext(request))

def tem(request):#tem临时网页
    return render_to_response('tem.html',context_instance=RequestContext(request))

def page5302(request):  # page5302
    return render_to_response('page5302.html', context_instance=RequestContext(request))

def page5303(request):  # page5303
    return render_to_response('page5303.html', context_instance=RequestContext(request))

def page5303english(request):  # page5303english
    return render_to_response('page5303english.html', context_instance=RequestContext(request))
    
def page5308(request):  # page5308
    return render_to_response('page5308.html', context_instance=RequestContext(request))

def page5308english(request):  # page5308english
    return render_to_response('page5308english.html', context_instance=RequestContext(request))


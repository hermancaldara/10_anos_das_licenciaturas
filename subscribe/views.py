# coding: utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import EntryForm


def subscribe(request):
    form = EntryForm()
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = EntryForm()
            return render_to_response(
                'subscribe.html',
                {'success': success, 'form': form},
                context_instance = RequestContext(request)
            )

    return render_to_response(
        'subscribe.html',
        {'form': form},
        context_instance=RequestContext(request),
    )

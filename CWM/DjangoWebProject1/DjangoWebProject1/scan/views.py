from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Scan
from .forms import ScanDIRForm


class IndexView(generic.ListView):
    template_name = 'scan/index.html'
    context_object_name = 'latest_scan_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Scan.objects.order_by('-pub_date')[:5]


def get_dir(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ScanDIRForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            ctx ={}
            ctx['rlt'] = request.POST['scan_dir']

        return render(request, "scan/post.html", ctx)
        # return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ScanDIRForm()

    return render(request, 'scan/post.html', {'form': form})

def results(request, scan_dir):
    response = "You're looking at the results of scan %s."
    return HttpResponse(response % scan_dir)

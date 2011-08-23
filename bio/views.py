__author__ = 'alexaled'

from django.shortcuts import render_to_response, RequestContext, \
    HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
import time

from models import MyBio, HttpRequestSave
from context_processors import add_conf_proc
from forms import BioForm, HttpEditForm


def my_bio_view(request):
    """
    for main page view my bio all data
    """
    all_bio = MyBio.objects.all()
    bio_dict = {}
    for bio_inst in all_bio:
        bio_inst_dict = {'id': bio_inst.id,
                         'first_name': bio_inst.first_name,
                         'last_name': bio_inst.last_name,
                         'birth_date': bio_inst.birth_date,
                         'biography': bio_inst.biography,
                         'contacts': bio_inst.contacts}
        bio_dict[bio_inst] = bio_inst_dict

    return render_to_response('bio/my_bio_view.html', {'my_bio': bio_dict})


@login_required
def edit_data(request, id=1, rev=False):
    """
    views for edit data
    """
    try:
        my_bio_edit = MyBio.objects.get(id=id)
    except:
        my_bio_edit = MyBio.objects.create()

    if request.POST:
        # 3 sec sleep for ajax submit
        if request.is_ajax():
            time.sleep(3)
        form = BioForm(request.POST, instance=my_bio_edit)
        if rev:
            form.fields.keyOrder.reverse()
        if form.is_valid():
            form.save()
            if request.is_ajax():
                json_result = simplejson.dumps({'status': "done_status"})
        else:
            if request.is_ajax():
                error_string = 'Errors in the fields '
                for err in form.errors:
                    error_string = error_string + " " + err + " "
                json_result = simplejson.dumps({'status': 'fail_status',
                                                'errors': error_string})
        if request.is_ajax():
            return HttpResponse(json_result, mimetype='application/javascript')
    else:
        form = BioForm(instance=my_bio_edit)
        if rev:
                form.fields.keyOrder.reverse()

    return render_to_response('bio/edit_data.html',
            {'form': form, 'id': id, 'reverse': rev, 'obj': my_bio_edit})


@login_required
def edit_data_http(request, id=1):
    """
    views for edit data
    """

    try:
        http_edit = HttpRequestSave.objects.get(id=id)
    except:
        http_edit = HttpRequestSave.objects.create()

    if request.POST:
        form = HttpEditForm(request.POST, instance=http_edit)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('my-bio/req-list'))#reverse(http_view))
    else:
        form = HttpEditForm(instance=http_edit)

    return render_to_response('bio/http_request_edit.html',
            {'form': form, 'id': id, 'obj': http_edit})


def add_conf(request):
    """
    view apps in settings for context proc
    """
    return render_to_response('bio/cont_proc.html', {},
                              context_instance=RequestContext(request,
                                            processors=[add_conf_proc]))


def http_view(request):
    """
    view http request
    """
    ten_last_req = HttpRequestSave.objects.order_by('-priority')[0:10]
    return render_to_response('bio/http_request.html',
            {'ten_last_req': ten_last_req})

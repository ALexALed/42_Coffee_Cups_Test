__author__ = 'alexaled'

from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from models import MyBio, HttpRequestSave

from context_processors import add_conf_proc
from forms import BioForm

from django.template.loader import get_template


def my_bio_view(request):
    """
    for main page view my bio all data
    """
    all_bio = MyBio.objects.all()
    bio_dict = {}
    for bio_inst in all_bio:
        bio_inst_dict = {'id' : bio_inst.id, 'first_name' : bio_inst.first_name,
                         'last_name' : bio_inst.last_name, 'birth_date' : bio_inst.birth_date,
                         'biography' : bio_inst.biography, 'contacts' : bio_inst.contacts}
        bio_dict[bio_inst] = bio_inst_dict

    return render_to_response('bio/my_bio_view.html', {'my_bio' : bio_dict})

@login_required
def edit_data(request, id=1, reverse=False):
    """
    views for edit data
    """

    try:
        my_bio_edit = MyBio.objects.get(id=id)
    except :
        my_bio_edit = MyBio.objects.create()

    if request.POST:
        form = BioForm(request.POST, instance=my_bio_edit)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/my-bio/get-bio/')
        else:
            if reverse:
                form.fields.keyOrder.reverse()

    else:
        form = BioForm(instance=my_bio_edit)
        if reverse:
                form.fields.keyOrder.reverse()

    return render_to_response('bio/edit_data.html', {'form':form, 'id':id, 'reverse':reverse, 'obj':my_bio_edit})



def add_conf(request):
    """
    view apps in settings for context proc
    """
    return render_to_response('bio/cont_proc.html', {},
                              context_instance=RequestContext(request, processors=[add_conf_proc]))


def http_view(request):
    ten_last_req = HttpRequestSave.objects.order_by('-id')[0:10]
    return render_to_response('bio/http_request.html', {'ten_last_req':ten_last_req})


from django.shortcuts import render_to_response
from models import MyBio

def my_bio_view(request):
    all_bio = MyBio.objects.all()
    bio_dict = {}
    for bio_inst in all_bio:
        bio_inst_dict = {'id' : bio_inst.id, 'first_name' : bio_inst.first_name,
                         'last_name' : bio_inst.last_name, 'birth_date' : bio_inst.birth_date,
                         'biography' : bio_inst.biography, 'contacts' : bio_inst.contacts}
        bio_dict[bio_inst] = bio_inst_dict

    return render_to_response('bio/my_bio_view.html', {'my_bio' : bio_dict})

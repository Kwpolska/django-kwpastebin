from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from kwpastebin.models import Paste, LANGUAGE_CHOICES, LANGUAGE_SHORT_CHOICES
from django.http import HttpResponseForbidden, HttpResponseBadRequest
from django.urls import reverse
from django.conf import settings
# Create your views here.

def index(request):
    has_add_perm =  request.user.has_perm("kwpastebin.add_paste") or getattr(settings, 'KWPASTEBIN_ANONYMOUS_CAN_ADD', False)
    if request.method == "POST":
        if not has_add_perm:
            return HttpResponseForbidden()
        if 'content' not in request.POST or 'language' not in request.POST or request.POST['language'] not in LANGUAGE_SHORT_CHOICES:
            return HttpResponseBadRequest()

        paste = Paste()
        paste.user = request.user if request.user.is_authenticated else None
        paste.content = request.POST['content']
        paste.language = request.POST['language']
        paste.save()
        return redirect(paste.get_absolute_url())


    context = {
        'pid': 'paste_index',
        'title': 'Pastebin',
        'htmltitle': 'Pastebin | go.chriswarrick.com',
        'has_add_perm': has_add_perm,
        'language_choices': LANGUAGE_CHOICES,
    }
    return render(request, "index.html", context)

@login_required
def my_pastes(request):
    pastes = Paste.objects.filter(user=request.user)
    context = {
        'pid': 'my_pastes',
        'title': 'My pastes',
        'htmltitle': 'My pastes | go.chriswarrick.com',
        'pastes': pastes
    }
    return render(request, "my_pastes.html", context)

@permission_required('kwpastebin.list_all_pastes')
def all_pastes(request):
    pastes = Paste.objects.all()
    context = {
        'pid': 'all_pastes',
        'title': 'All pastes',
        'htmltitle': 'All pastes | go.chriswarrick.com',
        'pastes': pastes
    }
    return render(request, "all_pastes.html", context)

@permission_required('kwpastebin.invalidate_cache')
def invalidate_cache(request):
    Paste.objects.all().update(html=None)
    return redirect(reverse('kwpastebin:all_pastes'))

def _can_with_own(request, paste, permission: str) -> bool:
    return request.user.is_authenticated and (
        request.user.has_perm("kwpastebin.{0}_paste".format(permission)) or
        (request.user == paste.user and request.user.has_perm("kwpastebin.{0}_own_paste".format(permission)))
    )

def show_paste(request, id):
    paste = get_object_or_404(Paste, id=id)
    context = {
        'pid': 'paste_show',
        'title': 'Paste {0}'.format(paste.id),
        'htmltitle': 'Paste {0} | go.chriswarrick.com'.format(paste.id),
        'can_change': _can_with_own(request, paste, 'change'),
        'can_delete': _can_with_own(request, paste, 'delete'),
        'paste': paste,
    }
    return render(request, "paste.html", context)

@login_required
def edit_paste(request, id):
    paste = get_object_or_404(Paste, id=id)
    if not _can_with_own(request, paste, 'change'):
        return HttpResponseForbidden()

    if request.method == "GET":
        context = {
            'pid': 'paste_edit',
            'title': 'Edit paste {0}'.format(paste.id),
            'htmltitle': 'Edit Paste {0} | go.chriswarrick.com'.format(paste.id),
            'paste': paste,
            'language_choices': LANGUAGE_CHOICES,
        }
        return render(request, "edit_paste.html", context)
    else:
        if 'content' not in request.POST or 'language' not in request.POST or request.POST['language'] not in LANGUAGE_SHORT_CHOICES:
            return HttpResponseBadRequest()
        paste.content = request.POST['content']
        paste.language = request.POST['language']
        paste.save()

        return redirect(paste.get_absolute_url())

@login_required
def delete_paste(request, id):
    paste = get_object_or_404(Paste, id=id)
    if not _can_with_own(request, paste, 'delete'):
        return HttpResponseForbidden()

    if request.method == "GET":
        context = {
            'pid': 'paste_delete',
            'title': 'Confirm deletion of paste {0}'.format(paste.id),
            'htmltitle': 'Delete Paste {0} | go.chriswarrick.com'.format(paste.id),
            'paste': paste,
        }
        return render(request, "delete_paste.html", context)
    elif request.POST['act'] == 'confirm':
        paste.delete()
        return redirect(reverse('kwpastebin:index'))
    elif request.POST['act'] == 'cancel':
        return redirect(paste.get_absolute_url())

@permission_required('kwpastebin.invalidate_cache')
def invalidate_cache_for_paste(request, id):
    paste = get_object_or_404(Paste, id=id)
    Paste.objects.filter(id=id).update(html=None)  # prevent changing modification date
    return redirect(paste.get_absolute_url())


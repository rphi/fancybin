from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from pastes.models import Paste
from django.http import Http404, HttpResponseForbidden, HttpResponse
from django.core.exceptions import PermissionDenied
import uuid
from django import forms
from django.contrib import messages

# Create your views here.

def home(request):

  pastes = None

  if request.user.is_authenticated:
    pastes = Paste.objects.filter(user=request.user)

  return render(request, 'www/pastes/home.html', {
    'pastes': pastes,
  })

def getPasteByID(request, id):
  try:
    uid = uuid.UUID(id)
  except ValueError:
    raise Http404("Not a valid UUID")

  p = get_object_or_404(Paste, id=uid)

  if p.private:
    if p.user != request.user:
      raise PermissionDenied("This paste is private and doesn't belong to you.")

  return p

@login_required()
def newPaste(request):
  return render(request, 'www/pastes/paste.html', {
    'editing': True,
    'paste': None
  })

def viewPaste(request, id):
  p = getPasteByID(request, id)

  return render(request, 'www/pastes/paste.html', {
    'editing': False,
    'paste': p
  })

@login_required()
def editPaste(request, id):
  p = getPasteByID(request, id)

  if p.user != request.user:
    raise PermissionDenied("This paste doesn't belong to you.")

  return render(request, 'www/pastes/paste.html', {
    'editing': True,
    'paste': p
  })


@login_required()
def deletePaste(request, id):
  p = getPasteByID(request, id)

  if p.user != request.user:
    raise PermissionDenied("This paste doesn't belong to you.")

  p.delete()

  messages.success(request, "Your paste has been deleted.")

  return redirect('home', permanent=False)

class PasteForm(forms.ModelForm):
    class Meta:
      model = Paste
      fields = '__all__'

@login_required()
@require_http_methods(["POST"])
def savePaste(request):
  data = request.POST.copy()
  data['user'] = request.user

  data['private'] = True if data['visibility'] == 'private' else False

  p = None

  if not request.POST['id']:
    # new paste

    form = PasteForm(data=data)

    if form.is_valid():
      print("saving form")
      p = form.save()
      messages.success(request, "Saved paste.")
    else:
      messages.error(request, "Error saving paste.")
      redirect('newpaste', permanent=False)


  else:
    # editing existing
    p = getPasteByID(request, request.POST['id'])

    if p.user != request.user:
      raise PermissionDenied("This paste doesn't belong to you.")
    
    form = PasteForm(instance=p, data=data)
    if form.is_valid():
      print("saving form")
      p = form.save()
      messages.success(request, "Saved paste.")
    else:
      messages.error(request, "Error saving paste.")
      redirect('editpaste', p.id, permanent=False)

  

  return redirect('viewpaste', p.id, permanent=False)
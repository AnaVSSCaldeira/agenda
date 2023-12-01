from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from contact.forms import ContactForm
from contact.models import Contact

#CRUD
def create(request):
    form_action=reverse('contact:create')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {'form': form, 'form_action': form_action}

        if form.is_valid():
            new_contact = form.save()
            # new_contact = form.save(commit=False) #para salvar fazendo alguma alteração
            # new_contact.show = False
            # new_contact.save()
            # new_contact.save() #para salvar direto
            return redirect('contact:update', contact_id = new_contact.id)
        
        return render(request, 'contact/create.html', context)
    
    context = {'form': ContactForm()}
    return render(request, 'contact/create.html', context)



def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action=reverse('contact:update', args=(contact_id,))
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)

        context = {'form': form, 'form_action': form_action}

        if form.is_valid():
            update_contact = form.save()
            return redirect('contact:update', contact_id=update_contact.pk)
        
        return render(request, 'contact/create.html', context)

    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }

    return render(request, 'contact/create.html', context)

def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation,
        }
    )
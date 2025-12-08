from django.contrib import messages
from django.views import generic
from . forms import FormInscription

class Acceuil(generic.FormView):
    template_name = "index.html"
    form_class = FormInscription
    success_url = "/"

    def form_valid(self, form):
        form.save()
        # Message de succès
        messages.success(
            self.request, 
            "Inscription réussie ! Merci de rejoindre notre communauté. Tu recevras bientôt un message WhatsApp avec les instructions."
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # Message d'erreur
        messages.error(
            self.request,
            "Oups ! Il y a une erreur dans le formulaire. Vérifie tes informations."
        )
        return super().form_invalid(form)
from django.contrib import admin

from consultorio.models import Tipo
from consultorio.models import Compromisso
from consultorio.models import Usuario
from consultorio.models import Agenda
from consultorio.models import agendaCompromisso
from consultorio.models import agendaUsuario


admin.site.register(Tipo)
admin.site.register(Compromisso)
admin.site.register(Usuario)
admin.site.register(Agenda)
admin.site.register(agendaCompromisso)
admin.site.register(agendaUsuario)
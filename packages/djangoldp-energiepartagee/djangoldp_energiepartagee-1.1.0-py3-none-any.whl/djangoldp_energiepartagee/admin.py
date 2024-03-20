from django.contrib import admin
from djangoldp.admin import DjangoLDPAdmin
from djangoldp_energiepartagee.models import Actor, Contribution, Region, College, Regionalnetwork, Interventionzone, Legalstructure, Collegeepa, Paymentmethod, Profile, Integrationstep, Relatedactor

@admin.register(College, Collegeepa, Integrationstep, Interventionzone, Legalstructure, Paymentmethod, Profile, Region, Regionalnetwork)
class EPModelAdmin(DjangoLDPAdmin):
    readonly_fields=('urlid',)


@admin.register(Actor)
class ActorAdmin(EPModelAdmin):
    list_display = ('longname', 'shortname', 'updatedate', 'createdate')
    search_fields = ['longname', 'shortname']


@admin.register(Relatedactor)
class RelatedactorAdmin(EPModelAdmin):
    list_display =('__str__', 'role')
    search_fields = ['actor__longname', 'actor__shortname', 'user__first_name', 'user__last_name', 'user__email']


@admin.register(Contribution)
class ContributionAdmin(EPModelAdmin):
    list_display = ('actor', 'year', 'updatedate', 'createdate')
    search_fields = ['actor__longname','actor__shortname']

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.contributionstatus in ('a_ventiler', 'valide',):
            return self.readonly_fields + ('amount',)
        return self.readonly_fields
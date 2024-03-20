from django.db import models

from djangoldp.models import Model
from djangoldp.permissions import AuthenticatedOnly, ReadOnly


COMMUNICATION_PROFILE_REPLICABILITY_CHOICES = [
    ("easy", "Facilement"),
    ("hard", "Difficilement"),
    ("no", "Non"),
    ("unknown", "Je ne sais pas"),
]


class CommunicationProfile(Model):
    is_public = models.BooleanField(
        default=False, blank=True, null=True, verbose_name="Publique?"
    )
    is_featured = models.BooleanField(
        default=False, blank=True, null=True, verbose_name="Mis en avant?"
    )
    crowdfunding_url = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="URL Crowdfunding"
    )
    long_description = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="Description générale du projet",
    )
    star_initiative_briefing = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Briefing projet star"
    )
    stakes_description = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Enjeux"
    )
    replicability = models.CharField(
        choices=COMMUNICATION_PROFILE_REPLICABILITY_CHOICES,
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Réplicabilité",
    )
    additional_informations = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Infos diverses"
    )

    class Meta(Model.Meta):
        ordering = ["pk"]
        permission_classes = [AuthenticatedOnly, ReadOnly]
        rdf_type = "energiepartagee:communication_profile"
        nested_fields = ["testimonies"]

    def __str__(self):
        if self.citizen_project:
            return self.citizen_project.name
        else:
            return self.urlid

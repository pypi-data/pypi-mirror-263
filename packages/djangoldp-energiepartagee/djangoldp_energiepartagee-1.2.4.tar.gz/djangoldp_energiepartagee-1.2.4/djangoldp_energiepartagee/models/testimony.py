from django.db import models

from djangoldp.models import Model
from djangoldp.permissions import AuthenticatedOnly, ReadOnly

from djangoldp_energiepartagee.models.communication_profile import CommunicationProfile


class Testimony(Model):
    communication_profile = models.ForeignKey(
        CommunicationProfile,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Témoignage",
        related_name="testimonies",
    )
    author_name = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Auteur"
    )
    content = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Contenu"
    )

    class Meta(Model.Meta):
        ordering = ["pk"]
        permission_classes = [AuthenticatedOnly, ReadOnly]
        rdf_type = "energiepartagee:testimony"

    def __str__(self):
        return self.urlid

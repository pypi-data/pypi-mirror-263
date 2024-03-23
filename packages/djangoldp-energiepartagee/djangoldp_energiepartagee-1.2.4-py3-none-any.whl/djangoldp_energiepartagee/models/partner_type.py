from django.db import models

from djangoldp.models import Model
from djangoldp.permissions import AuthenticatedOnly, ReadOnly

from djangoldp_energiepartagee.models.partner import Partner


class PartnerType(Model):
    name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Type"
    )
    partners = models.ManyToManyField(
        Partner,
        blank=True,
        verbose_name="Partenaires",
        related_name="types",
    )

    class Meta(Model.Meta):
        ordering = ["name"]
        permission_classes = [AuthenticatedOnly, ReadOnly]
        rdf_type = "energiepartagee:partner_type"
        serializer_fields = ["@id", "name"]

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.urlid

from django.db import models

from djangoldp.models import Model
from djangoldp.permissions import AuthenticatedOnly, ReadOnly


class Collegeepa(Model):
    name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="collège"
    )

    class Meta(Model.Meta):
        ordering = ["pk"]
        permission_classes = [AuthenticatedOnly, ReadOnly]
        rdf_type = "energiepartagee:collegeepa"
        serializer_fields = ["name"]

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.urlid

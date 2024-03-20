from django.db import models

from djangoldp.models import Model
from djangoldp.permissions import AuthenticatedOnly, ReadOnly


class ContractType(Model):
    type = models.CharField(max_length=250, blank=True, null=True, verbose_name="Type")

    class Meta(Model.Meta):
        ordering = ["pk"]
        permission_classes = [AuthenticatedOnly, ReadOnly]
        rdf_type = "energiepartagee:contract_type"

    def __str__(self):
        if self.type:
            return self.type
        else:
            return self.urlid

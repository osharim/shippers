# enconding: utf-8
from django.db.models import Model, DateTimeField
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class ModelDateTimeField(Model):
    """
    Helper to manage in one place the "timing" of creating a new object.

    With the pass of time we can add <deleted_at> to check soft deletes or updated_at,
    and we dont have to add this new fields on every model, we only have to add these
    new fields in this abstract model to spread to all all models that inherit from this
    """

    created = DateTimeField(verbose_name=_('Created'), default=timezone.now)

    class Meta:
        abstract = True

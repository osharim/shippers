# enconding: utf-8
from django.db.models import Model, DateTimeField, CharField
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.safestring import mark_safe


VALIDATION_PROCESS_STATUS = (
    ("VALIDATION_IN_PROCCESS", _("Validation in proccess")),
    ("VALIDATED", _("Validated")),
    ("SUSPENDED", _("Suspended")),
)


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


class StatusRequirementDisplay(Model):
    """
    Abstract model to display a friendly tag validation status proccess
    """

    status = CharField(_("Status"), choices=VALIDATION_PROCESS_STATUS, blank=True,
                       max_length=32, default="VALIDATION_IN_PROCCESS")

    def get_status(self):
        background = '#9e9e9e'
        status = self.get_status_display()

        if self.status == 'VALIDATION_IN_PROCCESS':
            background = '#e89657'

        if self.status == 'SUSPENDED':
            background = '#9e9e9e'

        if self.status == 'VALIDATED':
            background = '#11ad36'

        return mark_safe(F"<div style='background:{background};' class='status-tag'>{status}</div>")

    get_status.allow_tags = True
    get_status.short_description = 'Status'

    class Meta:
        abstract = True
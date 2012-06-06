from django.forms.fields import Field
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class CommaSeparatedCharField(Field):
    """A field consisting of a string of comma separated sub-strings"""
    default_error_messages = {
        'max_length': _(u'Each item must be at most %s characters (it has %s characters).'),
        'min_length': _(u'Each item must be at least %s characters (it has %s characters).'),
        'max_items': _('Ensure that there are no more than %s items in total.')
    }

    def __init__(self, max_length=None, min_length=None, max_items=None, *args, **kwargs):
        self.max_length, self.min_length, self.max_items = max_length, min_length, max_items
        super(CommaSeparatedCharField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        """Normalize data to a list of strings."""

        # Return an empty list if no input was given.
        if value in validators.EMPTY_VALUES:
            return None
        value = value.split(',')
        string_list = []
        for string in value:
            # Don't add empty strings if they somehow get in,
            # e.g. if there's a trailing comma
            if string:
                string_list.append(string.strip())
        return string_list

    def validate(self, value):
        """
        Check if value consists only of the max number of strings and that
        each is of valid length.
        """
        # Use the parent's handling of required fields, etc.
        super(CommaSeparatedCharField, self).validate(value)

        if self.max_items is not None and len(value) > self.max_items:
            raise ValidationError(self.error_messages['max_items']
                                  % self.max_items)
        if self.min_length is not None:
            for string in value:
                if len(string) < self.min_length:
                    raise ValidationError(self.error_messages['min_length']
                                          % self.min_length, len(string))
        if self.max_length is not None:
            for string in value:
                if len(string) > self.max_length:
                    raise ValidationError(self.error_messages['max_length']
                                          % self.max_length, len(string))

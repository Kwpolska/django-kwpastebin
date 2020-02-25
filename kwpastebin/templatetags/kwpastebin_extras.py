"""Extra template tags for KwPastebin."""
from django import template
from django.utils.html import format_html
from django.utils.formats import date_format
from kwpastebin.models import LANGUAGE_CHOICES

register = template.Library()


@register.simple_tag
def paste_li(paste):
    if paste.date_created == paste.date_modified:
        return format_html('<li><a href="{0}">{1}</a> (created by {2} on {3})', paste.get_absolute_url(), paste, paste.user_disp(), date_format(paste.date_created, "SHORT_DATETIME_FORMAT"))
    else:
        return format_html('<li><a href="{0}">{1}</a> (created by {2} on {3}, modified on {4})', paste.get_absolute_url(), paste, paste.user_disp(), date_format(paste.date_created, "SHORT_DATETIME_FORMAT"), date_format(paste.date_modified, "SHORT_DATETIME_FORMAT"))


@register.inclusion_tag('kwpastebin/paste_form.html')
def paste_form(form, paste):
    return {
        'form': form,
        'paste': paste,
        'submit_text': 'Save changes' if paste else 'Submit',
        'language_choices': LANGUAGE_CHOICES,
    }

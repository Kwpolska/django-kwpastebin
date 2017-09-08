from django.db import models
from hashid_field import HashidAutoField
from django.conf import settings
from django.urls import reverse


import pygments
import pygments.lexer
import pygments.lexers
import pygments.formatters.html

LANGUAGE_CHOICES = sorted([(i[1][0], i[0]) for i in pygments.lexers.get_all_lexers()], key=lambda x: x[1].casefold())
LANGUAGE_SHORT_CHOICES = [i[0] for i in LANGUAGE_CHOICES]
HTML_FORMATTER = pygments.formatters.html.HtmlFormatter(linenos='table')

def generate_html(code: str, language: str) -> str:
    lexer = pygments.lexers.get_lexer_by_name(language)  # type: pygments.lexer.Lexer
    return pygments.highlight(code, lexer, HTML_FORMATTER)

class AutoPygmentsHTMLField(models.TextField):
    def pre_save(self, model_instance: 'Paste', add: bool) -> str:
        return generate_html(model_instance.content, model_instance.language)

class Paste(models.Model):
    id = HashidAutoField(primary_key=True, editable=False)
    content = models.TextField()
    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES, default='text')
    html = AutoPygmentsHTMLField(null=True, editable=False)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, null=True)

    def __repr__(self):
        return "<Paste {}>".format(self.id)

    def __str__(self):
        return str(self.id)

    def html_or_generate(self):
        if not self.html:
            self.save()  # pre_save fires
        self.refresh_from_db()
        return self.html

    def get_absolute_url(self):
        return reverse('kwpastebin:show_paste', args=[self.id])

    def user_disp(self):
        return self.user or "anonymous"

    class Meta:
        permissions = (
            ('change_own_paste', 'Can change own paste'),
            ('delete_own_paste', 'Can delete own paste'),
            ('list_all_pastes', 'Can list all pastes'),
            ('invalidate_cache', 'Can invalidate cache'),
        )
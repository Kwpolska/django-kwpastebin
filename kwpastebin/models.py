from django.db import models
from hashid_field import HashidAutoField
from django.conf import settings
from django.urls import reverse

# Pygments: render code
import pygments
import pygments.lexer
import pygments.lexers
import pygments.formatters.html

# Markdown/Bleach: render Markdown (safely)
import markdown
import bleach

# Configuration for Pygments, Markdown, Bleach
LANGUAGE_CHOICES = [(i[1][0], i[0]) for i in pygments.lexers.get_all_lexers()] + [
    ('markdown_kwpastebin', 'markdown (render)')
]
LANGUAGE_CHOICES = sorted(LANGUAGE_CHOICES, key=lambda x: x[1].casefold())

LANGUAGE_SHORT_CHOICES = [i[0] for i in LANGUAGE_CHOICES]
DEFAULT_LANG = 'text'
HTML_FORMATTER = pygments.formatters.html.HtmlFormatter(linenos='table')

ALLOWED_TAGS = bleach.ALLOWED_TAGS + ['br', 'p', 'abbr', 'img', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'pre', 'code', 's']
ALLOWED_ATTRIBUTES = bleach.ALLOWED_ATTRIBUTES.copy()
ALLOWED_ATTRIBUTES['img'] = ['src', 'alt', 'title']
MD_EXTENSIONS = ['markdown.extensions.abbr', 'markdown.extensions.smart_strong', 'markdown.extensions.nl2br', 'mdx_linkify', 'markdown.extensions.toc']

def render_code_html(code: str, language: str) -> str:
    lexer = pygments.lexers.get_lexer_by_name(language)  # type: pygments.lexer.Lexer
    return pygments.highlight(code, lexer, HTML_FORMATTER)

def render_markdown_html(code: str) -> str:
    return bleach.clean(markdown.markdown(code, extensions=MD_EXTENSIONS),
                        tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES)


class AutoRenderHTMLField(models.TextField):
    def pre_save(self, model_instance: 'Paste', add: bool) -> str:
        if model_instance.language == 'markdown_kwpastebin':
            return render_markdown_html(model_instance.content)
        else:
            return render_code_html(model_instance.content, model_instance.language)

class Paste(models.Model):
    id = HashidAutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES, default=DEFAULT_LANG)
    public = models.BooleanField(default=False)
    html = AutoRenderHTMLField(null=True, editable=False)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, null=True)

    def __repr__(self):
        if self.title:
            return "<Paste {0} ({1})>".format(self.id, self.title)
        else:
            return "<Paste {}>".format(self.id)

    def __str__(self):
        return self.title or str(self.id)

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
from django import template
from ..models import Postmodel
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown
 
#built in template filters and tags  and we can make them available to our templates using the {% load %} tag.
register = template.Library()    # each model that contain template_tag needs to define a variable called register to be a valid tag library
      
@register.simple_tag                    #it register the function as a simple_tag
def total_post():
    return Postmodel.published.count()

@register.simple_tag    
def get_most_commented_posts(count=5):
    return Postmodel.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]

@register.inclusion_tag('community/latest_posts.html')   #he type that displays some data by rendering another template name latest_posts
def show_latest_posts(count=5):
    latest_posts = Postmodel.published.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}

@register.filter(name='markdown')    #pip install markdown==3.2.1 / pip3 install django-markdown-deux
def markdown_format(text):
    return mark_safe(markdown.markdown(text))    
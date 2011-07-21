__author__ = 'alexaled'

from django import template

from django.core.urlresolvers import reverse

register = template.Library()

@register.tag
def edit_link(parser, token):
    """
    tag register method
    """
    try:
        tag_name, edit_object = token.contents.split()
    except :
        message = 'tag error'
        raise template.TemplateSyntaxError(message)
    return EditLinkAdminNode(edit_object)

class EditLinkAdminNode(template.Node):
    """
    tag in template node
    """
    def __init__(self, edit_object):
        self.edit_object = template.Variable(edit_object)

    def render(self, context):
        try:
            obj = self.edit_object.resolve(context)
            return reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.module_name), args=(obj.id,))
        except template.VariableDoesNotExist:
            return ''


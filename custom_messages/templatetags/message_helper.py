from django import template
register = template.Library()


@register.simple_tag
def inbox_messages_count(user, is_count=0):
    messages = user.received_messages.filter(
        recipient_deleted_at__isnull=True)
    if is_count:
        return messages.count()
    return messages[:5]


@register.inclusion_tag('django_messages/include/_inbox.html')
def inbox_messages(user):
    messages = user.received_messages.filter(
        recipient_deleted_at__isnull=True)
    return {
        'messages': messages,
    }
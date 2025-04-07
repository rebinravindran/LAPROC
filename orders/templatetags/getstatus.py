from django import template

register=template.Library()

@register.simple_tag(name="getstatus")
def getstatus(status):
    status=status-1
    statusarray=['order_confirm','order_processed','order_delivered','order_rejected']
    return statusarray[status]


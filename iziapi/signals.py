from django.dispatch import Signal

iziapi_post_checkout = Signal(
    providing_args=["order", "user", "request", "response"])

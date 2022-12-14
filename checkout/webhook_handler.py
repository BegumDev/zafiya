# import json
# import time
# from django.http import HttpResponse
# from django.conf import settings
# from products.models import Product
# from profiles.models import UserProfile
# from .models import Order, OrderLineItem


# class StripeWH_Handler:
#     """ Hnadle Stripe webhooks """
#     def __init__(self, request):
#         self.request = request


#     def handle_event(self, event):
#         """ handle an unexpected webhook event """
#         return HttpResponse(
#             content=f'Unhandled webhook received: {event["type"]}',
#             status=200)

    
#     def handle_payment_intent_succeeded(self, event):
#         """ handle payment_intent.suceeded webhook from stripe """
#         intent = event.data.object
#         pid = intent.id
#         bag = intent.metadata.bag
#         save_info = intent.metadata.save_info

#         billing_details = intent.charges.data[0].billing_details
#         shipping_details = intent.shipping
#         grand_total = round(intent.charges.data[0].amount / 100, 2)

#         # clean data in shipping details
#         for field, value in shipping_details.address.items():
#             if value == "":
#                 shipping_details.address[field] = None

#         order_exists = False
#         attempt = 1
#         while attempt <= 5:
#             try:
#                 order = Order.objects.get(
#                     full_name__iexact=shipping_details.name,
#                     email__iexact=billing_details.email,
#                     phone_number__iexact=shipping_details.phone,
#                     country__iexact=shipping_details.address.country,
#                     postcode__iexact=shipping_details.address.postal_code,
#                     town_or_city__iexact=shipping_details.address.city,
#                     street_address1__iexact=shipping_details.address.line1,
#                     street_address2__iexact=shipping_details.address.line2,
#                     county__iexact=shipping_details.address.state,
#                     grand_total=grand_total,
#                     original_bag=bag,
#                     stripe_pid=pid,
#                 )
#                 order_exists = True
#                 break
#             except Order.DoesNotExist:
#                 attempt += 1
#                 time.sleep(1)    
#         if order_exists:
#             return HttpResponse(
#                 content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already exists',
#                 status=200)
#         else:
#             order = None
#             try:
#                 order = Order.objects.create(
#                     full_name=shipping_details.name,
#                     email=billing_details.email,
#                     phone_number=shipping_details.phone,
#                     country=shipping_details.address.country,
#                     postcode=shipping_details.address.postal_code,
#                     town_or_city=shipping_details.address.city,
#                     street_address1=shipping_details.address.line1,
#                     street_address2=shipping_details.address.line2,
#                     county=shipping_details.address.state,
#                     original_bag=bag,
#                     stripe_pid=pid,
#                 )
#                 for item_id, quantity in json.loads(bag).items():
#                     product = Product.objects.get(id=item_id)
#                     order_line_item = OrderLineItem(
#                         order=order,
#                         product=product,
#                         quantity=quantity,
#                     )
#                     order_line_item.save()
#             except Exception as e:
#                 if order:
#                     order.delete()
#                 return HttpResponse(
#                     content=f'Webhook received: {event["type"]} | ERROR: {e}', status=500
#                     )
#         return HttpResponse(
#             content=f'Webhook received: {event["type"]} | SUCCESS: created order in webhook',
#             status=200)


#     def handle_payment_intent_payment_failed(self, event):
#         """ handle payment_intent.payment_failed webhook from stripe """
#         return HttpResponse(
#             content=f'Webhook received: {event["type"]}',
#             status=200)

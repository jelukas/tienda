from paypal.pro.views import PayPalPro
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def buy_my_item(request):
    item = {"amt": "10.00",             # amount to charge for item
            "inv": "inventory",         # unique tracking variable paypal
            "custom": "tracking",       # custom tracking variable for you
            "cancelurl": "http://testing.libresysteam.com/payment-url/",  # Express checkout cancel url
            "returnurl": "http://testing.libresysteam.com/payment-url/"}  # Express checkout return url

    kw = {"item": item,                            # what you're selling
          "payment_template": "payment.html",      # template name for payment
          "confirm_template": "confirmation.html", # template name for confirmation
          "success_url": "/success/"}              # redirect location after success

    ppp = PayPalPro(**kw)
    return ppp(request)
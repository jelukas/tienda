from django.db import models
#from paypal.pro.signals import payment_was_successful
from paypal.standard.ipn.signals import payment_was_successful

def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    # Undertake some action depending upon `ipn_obj`.
    print "TODO OK !"

payment_was_successful.connect(show_me_the_money ,dispatch_uid="somethjjing-rational-here")
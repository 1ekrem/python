from behave import *
from checkout-bdd import *

@given(u'the price of a \'banana\' is 40c')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the price of a \'banana\' is 40c')


@when(u'I checkout 1 \'banana\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I checkout 1 \'banana\'')


@then(u'the total price should be 40c')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the total price should be 40c')

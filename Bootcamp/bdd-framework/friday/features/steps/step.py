from behave import *
from friday import *

@given(u'today is Sunday')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given today is Sunday')


@when(u'I ask whether it\'s Friday yet')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I ask whether it\'s Friday yet')


@then(u'I should be told "Nope"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be told "Nope"')
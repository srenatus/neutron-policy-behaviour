from behave import given, when, then, step
import neutron.context as context
import neutron.policy as policy
from neutron.common import exceptions


@given('we are user "{user}" with role "{role}" in tenant "{tenant}"')
def step_impl(ctx, user, role, tenant):
    ctx.ctx = context.Context(user, tenant, roles=[role], is_admin=(tenant == 'admin'))


@given('we are user "{user}" in tenant "{tenant}"')
def step_impl(ctx, user, tenant):
    ctx.ctx = context.Context(user, tenant, is_admin=(tenant == 'admin'))


@when('we {action} a {something} of tenant "{tenant}"')
def step_impl(ctx, action, something, tenant):
    ctx.action = '%s_%s' % (action, something.lower().replace(' ', ''))
    ctx.target_tenant = tenant


@then('this is allowed')
def step_impl(ctx):
    assert policy.enforce(ctx.ctx, ctx.action, {'tenant_id': ctx.target_tenant})


@then('this is forbidden')
def step_impl(ctx):
    try:
        policy.enforce(ctx.ctx, ctx.action, {'tenant_id': ctx.target_tenant})
    except exceptions.PolicyNotAuthorized:
        return True
    return False

Feature: Floating IPs

  Scenario: creating a floating IP as admin
    Given we are user "admin" in tenant "admin"
    When we create a floating IP of tenant "foo"
    Then this is allowed

  Scenario: creating a floating IP of my tenant
    Given we are user "alice" in tenant "alice-tenant"
    When we create a floating IP of tenant "alice-tenant"
    Then this is forbidden

  Scenario: creating a floating IP of another tenant
    Given we are user "alice" with role "floating_user" in tenant "alice-tenant"
    When we create a floating IP of tenant "bob-tenant"
    Then this is forbidden

  Scenario: deleting a floating IP as admin
    Given we are user "admin" in tenant "admin"
    When we delete a floating IP of tenant "foo"
    Then this is allowed

  Scenario: deleting a floating IP of my tenant
    Given we are user "alice" in tenant "alice-tenant"
    When we delete a floating IP of tenant "alice-tenant"
    Then this is allowed

  Scenario: deleting a floating IP of another tenant
    Given we are user "alice" in tenant "alice-tenant"
    When we delete a floating IP of tenant "bob-tenant"
    Then this is forbidden

# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import json

import requests
import responses
from nose.tools import (
  assert_equal,
  assert_is_instance,
  assert_is_none,
  assert_is_not_none,
  assert_not_equal,
  assert_raises
)

from gocardless_pro.errors import MalformedResponseError
from gocardless_pro import resources
from gocardless_pro import list_response

from .. import helpers
  

@responses.activate
def test_bank_authorisations_create():
    fixture = helpers.load_fixture('bank_authorisations')['create']
    helpers.stub_response(fixture)
    response = helpers.client.bank_authorisations.create(*fixture['url_params'])
    body = fixture['body']['bank_authorisations']

    assert_is_instance(response, resources.BankAuthorisation)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.authorisation_type, body.get('authorisation_type'))
    assert_equal(response.authorised_at, body.get('authorised_at'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.expires_at, body.get('expires_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.last_visited_at, body.get('last_visited_at'))
    assert_equal(response.redirect_uri, body.get('redirect_uri'))
    assert_equal(response.url, body.get('url'))
    assert_equal(response.links.billing_request,
                 body.get('links')['billing_request'])
    assert_equal(response.links.institution,
                 body.get('links')['institution'])

@responses.activate
def test_bank_authorisations_create_new_idempotency_key_for_each_call():
    fixture = helpers.load_fixture('bank_authorisations')['create']
    helpers.stub_response(fixture)
    helpers.client.bank_authorisations.create(*fixture['url_params'])
    helpers.client.bank_authorisations.create(*fixture['url_params'])
    assert_not_equal(responses.calls[0].request.headers.get('Idempotency-Key'),
                     responses.calls[1].request.headers.get('Idempotency-Key'))

def test_timeout_bank_authorisations_create_idempotency_conflict():
    create_fixture = helpers.load_fixture('bank_authorisations')['create']
    get_fixture = helpers.load_fixture('bank_authorisations')['get']
    with helpers.stub_timeout_then_idempotency_conflict(create_fixture, get_fixture) as rsps:
      response = helpers.client.bank_authorisations.create(*create_fixture['url_params'])
      assert_equal(2, len(rsps.calls))

    assert_is_instance(response, resources.BankAuthorisation)

@responses.activate
def test_timeout_bank_authorisations_create_retries():
    fixture = helpers.load_fixture('bank_authorisations')['create']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.bank_authorisations.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['bank_authorisations']

    assert_is_instance(response, resources.BankAuthorisation)

def test_502_bank_authorisations_create_retries():
    fixture = helpers.load_fixture('bank_authorisations')['create']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.bank_authorisations.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['bank_authorisations']

    assert_is_instance(response, resources.BankAuthorisation)
  

@responses.activate
def test_bank_authorisations_get():
    fixture = helpers.load_fixture('bank_authorisations')['get']
    helpers.stub_response(fixture)
    response = helpers.client.bank_authorisations.get(*fixture['url_params'])
    body = fixture['body']['bank_authorisations']

    assert_is_instance(response, resources.BankAuthorisation)
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.authorisation_type, body.get('authorisation_type'))
    assert_equal(response.authorised_at, body.get('authorised_at'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.expires_at, body.get('expires_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.last_visited_at, body.get('last_visited_at'))
    assert_equal(response.redirect_uri, body.get('redirect_uri'))
    assert_equal(response.url, body.get('url'))
    assert_equal(response.links.billing_request,
                 body.get('links')['billing_request'])
    assert_equal(response.links.institution,
                 body.get('links')['institution'])

@responses.activate
def test_timeout_bank_authorisations_get_retries():
    fixture = helpers.load_fixture('bank_authorisations')['get']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.bank_authorisations.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['bank_authorisations']

    assert_is_instance(response, resources.BankAuthorisation)

def test_502_bank_authorisations_get_retries():
    fixture = helpers.load_fixture('bank_authorisations')['get']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.bank_authorisations.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['bank_authorisations']

    assert_is_instance(response, resources.BankAuthorisation)
  

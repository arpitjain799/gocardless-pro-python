# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import requests
import responses
from nose.tools import assert_is_instance, assert_raises

from gocardless_pro import Client
from gocardless_pro import services

access_token = 'access-token-xyz'
client = Client(access_token=access_token, base_url='http://example.com')

def test_requires_valid_environment():
    assert_raises(ValueError, Client, access_token=access_token, environment='invalid')

def test_bank_details_lookups_returns_service():
    assert_is_instance(client.bank_details_lookups, services.BankDetailsLookupsService)

def test_creditors_returns_service():
    assert_is_instance(client.creditors, services.CreditorsService)

def test_creditor_bank_accounts_returns_service():
    assert_is_instance(client.creditor_bank_accounts, services.CreditorBankAccountsService)

def test_currency_exchange_rates_returns_service():
    assert_is_instance(client.currency_exchange_rates, services.CurrencyExchangeRatesService)

def test_customers_returns_service():
    assert_is_instance(client.customers, services.CustomersService)

def test_customer_bank_accounts_returns_service():
    assert_is_instance(client.customer_bank_accounts, services.CustomerBankAccountsService)

def test_customer_notifications_returns_service():
    assert_is_instance(client.customer_notifications, services.CustomerNotificationsService)

def test_events_returns_service():
    assert_is_instance(client.events, services.EventsService)

def test_instalment_schedules_returns_service():
    assert_is_instance(client.instalment_schedules, services.InstalmentSchedulesService)

def test_mandates_returns_service():
    assert_is_instance(client.mandates, services.MandatesService)

def test_mandate_imports_returns_service():
    assert_is_instance(client.mandate_imports, services.MandateImportsService)

def test_mandate_import_entries_returns_service():
    assert_is_instance(client.mandate_import_entries, services.MandateImportEntriesService)

def test_mandate_pdfs_returns_service():
    assert_is_instance(client.mandate_pdfs, services.MandatePdfsService)

def test_payer_authorisations_returns_service():
    assert_is_instance(client.payer_authorisations, services.PayerAuthorisationsService)

def test_payments_returns_service():
    assert_is_instance(client.payments, services.PaymentsService)

def test_payouts_returns_service():
    assert_is_instance(client.payouts, services.PayoutsService)

def test_payout_items_returns_service():
    assert_is_instance(client.payout_items, services.PayoutItemsService)

def test_redirect_flows_returns_service():
    assert_is_instance(client.redirect_flows, services.RedirectFlowsService)

def test_refunds_returns_service():
    assert_is_instance(client.refunds, services.RefundsService)

def test_scenario_simulators_returns_service():
    assert_is_instance(client.scenario_simulators, services.ScenarioSimulatorsService)

def test_subscriptions_returns_service():
    assert_is_instance(client.subscriptions, services.SubscriptionsService)

def test_tax_rates_returns_service():
    assert_is_instance(client.tax_rates, services.TaxRatesService)

def test_webhooks_returns_service():
    assert_is_instance(client.webhooks, services.WebhooksService)


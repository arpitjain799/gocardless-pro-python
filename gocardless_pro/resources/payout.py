# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

class Payout(object):
    """A thin wrapper around a payout, providing easy access to its
    attributes.

    Example:
      payout = client.payouts.get()
      payout.id
    """

    def __init__(self, attributes, api_response):
        self.attributes = attributes
        self.api_response = api_response

    @property
    def amount(self):
        return self.attributes.get('amount')

    @property
    def arrival_date(self):
        return self.attributes.get('arrival_date')

    @property
    def created_at(self):
        return self.attributes.get('created_at')

    @property
    def currency(self):
        return self.attributes.get('currency')

    @property
    def deducted_fees(self):
        return self.attributes.get('deducted_fees')

    @property
    def id(self):
        return self.attributes.get('id')

    @property
    def links(self):
        return self.Links(self.attributes.get('links'))

    @property
    def payout_type(self):
        return self.attributes.get('payout_type')

    @property
    def reference(self):
        return self.attributes.get('reference')

    @property
    def status(self):
        return self.attributes.get('status')

    class Links(object):
        """Wrapper for the response's 'links' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes

        @property
        def creditor(self):
            return self.attributes.get('creditor')

        @property
        def creditor_bank_account(self):
            return self.attributes.get('creditor_bank_account')


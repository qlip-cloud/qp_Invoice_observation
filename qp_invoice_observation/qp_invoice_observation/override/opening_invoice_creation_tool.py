import frappe
from erpnext.accounts.doctype.opening_invoice_creation_tool.opening_invoice_creation_tool import OpeningInvoiceCreationTool


class CustomOpeningInvoiceCreationTool(OpeningInvoiceCreationTool):

    def get_invoice_dict(self, row=None):

        invoice = super(CustomOpeningInvoiceCreationTool, self).get_invoice_dict(row)

        if row.get('remarks'):
            invoice.update({
                "remarks": row.remarks
            })

        return invoice

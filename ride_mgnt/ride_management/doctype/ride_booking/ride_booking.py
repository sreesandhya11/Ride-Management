# Copyright (c) 2025, Sandhya and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def before_save(self):
		total_amount(self)

def total_amount(self):
	if self.price_per_km and self.estimate_km:
		if self.services:
			for a in self.services:
				if a.amount:
					print(a.amount)
				total_amount = (self.price_per_km * self.estimate_km) + a.amount
			self.total_amount = total_amount

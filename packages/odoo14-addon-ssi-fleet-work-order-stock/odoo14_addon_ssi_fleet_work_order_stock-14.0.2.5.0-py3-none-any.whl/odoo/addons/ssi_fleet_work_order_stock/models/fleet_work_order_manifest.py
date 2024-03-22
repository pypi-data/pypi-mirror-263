# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FleetWorkOrderManifest(models.Model):
    _name = "fleet_work_order_manifest"
    _description = "Fleet Work Order Manifest"
    _rec_name = "product_id"

    work_order_id = fields.Many2one(
        string="Work Order",
        comodel_name="fleet_work_order",
        ondelete="cascade",
    )
    product_id = fields.Many2one(
        comodel_name="product.product", string="Product", required=True
    )
    uom_quantity = fields.Float(string="Quantity", required=False)
    uom_id = fields.Many2one(comodel_name="uom.uom", string="UoM", required=True)

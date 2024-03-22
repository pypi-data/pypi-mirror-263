# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError

from odoo.addons.ssi_decorator import ssi_decorator


class FleetWorkOrder(models.Model):
    _name = "fleet_work_order"
    _inherit = ["fleet_work_order"]

    picking_ids = fields.One2many(
        comodel_name="stock.picking",
        string="Picking",
        inverse_name="fleet_work_order_id",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    allowed_picking_type_ids = fields.Many2many(
        comodel_name="stock.picking.type",
        string="Allowed Picking Types",
        related="type_id.allowed_picking_type_ids",
        store=False,
    )
    move_ids = fields.Many2many(
        string="Move",
        comodel_name="stock.move",
        compute="_compute_move_ids",
    )
    move_line_ids = fields.Many2many(
        string="Operations",
        comodel_name="stock.move.line",
        compute="_compute_move_ids",
    )
    manifest_ids = fields.One2many(
        comodel_name="fleet_work_order_manifest",
        inverse_name="work_order_id",
        string="Manifest",
        required=False,
    )

    @api.depends(
        "picking_ids",
    )
    def _compute_move_ids(self):
        for record in self:
            move = ml = []
            for picking in record.picking_ids:
                ml += picking.move_line_ids.ids
                move += picking.move_ids_without_package.ids
            record.move_line_ids = ml
            record.move_ids = move

    @ssi_decorator.pre_open_check()
    def _30_check_picking_done(self):
        self.ensure_one()
        for picking in self.picking_ids.filtered(lambda r: r.state != "done"):
            error_message = """
                Context: Start fleet work order
                Database ID: %s
                Problem: picking %s is not done
                Solution: Process on progress done
                """ % (
                self.id,
                picking.name,
            )
            raise UserError(_(error_message))

    def action_populate_manifest(self):
        for rec in self:
            rec.manifest_ids.unlink()
            product_qty_dict = {}
            for picking_id in rec.picking_ids:
                for move_id in picking_id.move_ids_without_package:
                    product_qty_dict[move_id.product_id] = product_qty_dict.get(
                        move_id.product_id, 0
                    ) + move_id.product_uom._compute_quantity(
                        move_id.product_uom_qty, move_id.product_id.uom_id
                    )
            for product_id, qty in product_qty_dict.items():
                self.env["fleet_work_order_manifest"].create(
                    {
                        "work_order_id": rec.id,
                        "product_id": product_id.id,
                        "uom_quantity": qty,
                        "uom_id": product_id.uom_id.id,
                    }
                )

    @ssi_decorator.post_confirm_action()
    def _recompute_computation(self):
        self.ensure_one()
        self.action_populate_manifest()

# -*- coding: utf-8 -*-


from openerp import models, fields, api, exceptions


class importes(models.Model):

    _name = "importes"
    _description = "prueba de api con decoradores"

    importe1 = fields.Integer('importe1', size = 5, select = True)
    importe2 = fields.Integer('importe2', size = 5, select = True)
    importe3 = fields.Integer(compute = '_calcula_importe3', store = True)

    @api.one
    @api.depends('importe1', 'importe2')
    def _calcula_importe3(self):
        self.importe3 = 0
        if self.importe1 and self.importe2:
            self.importe3 = (self.importe1 * self.importe2)

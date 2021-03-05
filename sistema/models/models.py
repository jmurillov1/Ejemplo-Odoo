# -*- coding: utf-8 -*-

from odoo import models, fields, api


def compute_default_codigo(self, tam):
    listado = self.env[self._name].search([])
    numero = str(int(listado[-1].codigo if listado else '0') + 1)
    return numero.zfill(tam)

def compute_default_codigo_contacto(self, tam):
    numero = str(len(self.persona_id.contactos_ids) + 1)
    return numero.zfill(tam)


class Persona(models.Model):
    _name = 'sistema.persona'
    _description = 'Clase Persona del Modulo Sistema'
    _rec_name = 'nombre'

    codigo = fields.Char(size=4, string='Codigo', readonly=True,
                         default=lambda self: compute_default_codigo(self, 4))
    nombre = fields.Char(string='Nombre', required=True, default=lambda self: "Jordan")
    apellido = fields.Char(string='Apellido', required=True)
    direccion = fields.Text(string='Dirección', required=True)
    contactos_ids = fields.One2many(
        'sistema.contacto', 'persona_id', string="Lista de Contactos", required=True)
    pais_id = fields.Many2one('sistema2.pais', string="Pais", required=True)
    provincia_id = fields.Many2one('sistema2.provincia', string="Provincia", required=True)

class Contacto(models.Model):
    _name = 'sistema.contacto'
    _description = 'Clase Contacto del Modulo Sistema'
    _rec_name = 'numero'

    codigo = fields.Char(size=4, string='Codigo', readonly=True,
                         default=lambda self: compute_default_codigo_contacto(self, 4))
    numero = fields.Char(size=10, string='Número de Celular')
    value = fields.Integer(string='Valor')
    value2 = fields.Float(compute="_value_pc", store=True)
    extranjero = fields.Boolean(string='Es Extranjero', default=False)
    operadora = fields.Selection(
        [('claro', 'Claro'), ('movistar', 'Movistar'), ('tuenti', 'Tuenti')], string='Operadora')
    persona_id = fields.Many2one(
        'sistema.persona', string="Persona", required=True, ondelete="cascade")

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

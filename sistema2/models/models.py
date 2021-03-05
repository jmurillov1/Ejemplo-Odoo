# -*- coding: utf-8 -*-

from odoo import models, fields, api


def compute_default_codigo(self, tam):
    listado = self.env[self._name].search([])
    numero = str(int(listado[-1].codigo if listado else '0') + 1)
    return numero.zfill(tam)


class pais(models.Model):
    _name = 'sistema2.pais'
    _description = 'Clase Pais del modulo Sistema2'
    _rec_name = 'nombre'

    codigo = fields.Char(size=4, string='Codigo', readonly=True,
                         default=lambda self: compute_default_codigo(self, 4))
    nombre = fields.Char(string='Nombre', required=True)

# class region(models.Model):
#     _name = 'sistema2.region'
#     _description = 'sistema2.sistema2'
#     _rec_name = 'nombre'

#     codigo = fields.Char(size=4, string='Codigo', readonly=True,
#                          default=lambda self: compute_default_codigo(self, 4))
#     nombre = fields.Char(string='Nombre', required=True)


class provincia(models.Model):
    _name = 'sistema2.provincia'
    _description = 'Clase Provincia del modulo Sistema2'
    _rec_name = 'nombre'

    codigo = fields.Char(size=4, string='Codigo', readonly=True,
                         default=lambda self: compute_default_codigo(self, 4))
    nombre = fields.Char(string='Nombre', required=True)
    pais_id = fields.Many2one('sistema2.pais', string="Pais", required=True)


class canton(models.Model):
    _name = 'sistema2.canton'
    _description = 'Clase Cantón del modulo Sistema2'
    _rec_name = 'nombre'

    codigo = fields.Char(size=4, string='Codigo', readonly=True,
                         default=lambda self: compute_default_codigo(self, 4))
    nombre = fields.Char(string='Nombre', required=True)
    pais_id = fields.Many2one(
        'sistema2.pais', string="Pais", required=True, store=False)
    provincia_id = fields.Many2one(
        'sistema2.provincia', string="Provincia", required=True, domain="[('pais_id','=', pais_id)]")


class parroquia(models.Model):
    _name = 'sistema2.parroquia'
    _description = 'Clase Parroquia del modulo Sistema2'
    _rec_name = 'nombre'

    codigo = fields.Char(size=4, string='Codigo', readonly=True,
                         default=lambda self: compute_default_codigo(self, 4))
    nombre = fields.Char(string='Nombre', required=True)
    pais_id = fields.Many2one(
        'sistema2.pais', string="Pais", required=True, store=False)
    provincia_id = fields.Many2one('sistema2.provincia', string="Provincia",
                                   required=True, domain="[('pais_id','=', pais_id)]", store=False)
    canton_id = fields.Many2one('sistema2.canton', string="Cantón",
                                required=True, domain="[('provincia_id','=', provincia_id)]")
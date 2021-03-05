# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
import re


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
        'sistema2.pais', string="Pais", required=True, store=False, default=lambda self: self.provincia_id.pais_id)
    provincia_id = fields.Many2one(
        'sistema2.provincia', string="Provincia", required=True, domain="[('pais_id','=', pais_id)]")

    _sql_constraints = [
        ('sistema2_canton_unique', 'unique(nombre, provincia_id)',
         'Validación Planificaciòn -> Ya existe un registro con estos datos.'),
    ]


class parroquia(models.Model):
    _name = 'sistema2.parroquia'
    _description = 'Clase Parroquia del modulo Sistema2'
    _rec_name = 'nombre'

    codigo = fields.Char(string='Codigo', readonly=True,
                         compute='calcular_codigo', store=True, help='Código')
    nombre = fields.Char(string='Nombre', required=True)
    pais_id = fields.Many2one(
        'sistema2.pais', string="Pais", required=True, store=False, default=lambda self: self.canton_id.provincia_id.pais_id)
    provincia_id = fields.Many2one('sistema2.provincia', string="Provincia",
                                   required=True, domain="[('pais_id','=', pais_id)]", store=False, default=lambda self: self.canton_id.provincia_id)
    canton_id = fields.Many2one('sistema2.canton', string="Cantón",
                                required=True, domain="[('provincia_id','=', provincia_id)]")

    @api.constrains('nombre')
    def _check_numero(self):
        for rec in self:
            if not(re.match("[A-Z]", rec.nombre)):
                raise exceptions.ValidationError(
                    'Campo No. -> Solo puede ingresar letras mayusculas')

    @api.depends('pais_id', 'provincia_id', 'canton_id')
    def calcular_codigo(self):
        codigo = ''
        for rec in self:
            if rec.pais_id:
                codigo += rec.pais_id.codigo
            if rec.provincia_id:
                codigo += rec.provincia_id.codigo
            if rec.canton_id:
                codigo += rec.canton_id.codigo
            rec.codigo = codigo
        return True
    
    @api.onchange('pais_id')
    def val_pais(self):
        mess = {
            'title': "Hola",
            'type': 'info',
            'message': "Llegue"
        }
        return {'warning': mess}
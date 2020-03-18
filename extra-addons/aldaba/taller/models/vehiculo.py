# -*- coding: utf-8 -*-

from odoo import models, fields

class Vehiculo(models.Model):
    _name = 'taller.vehiculo'
    _decription = 'Gestión Vehículos'

    name = fields.Char(string='Name',required=True, help="Introduzca el nombre", size=20, default="Nuevo")
    active = fields.Char(string='Active')
    matricula = fields.Char('Matricula')
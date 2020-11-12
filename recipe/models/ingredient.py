# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import Warning

class RecipeIngredientTable(models.Model):
    _name = 'recipe.ingredient.table'
    _description = 'Table of Ingredients'
    _rec_name = 'ingredient_id'

    recipe_id = fields.Many2one('recipe.recipe', string="Recette")
    ingredient_id = fields.Many2one('recipe.ingredient', string="Ingrédient")
    quantity = fields.Float(string="Quantité")
    uom_id = fields.Many2one('recipe.ingredient.uom', string="UOM")    


class RecipeIngredient(models.Model):
    _name = 'recipe.ingredient'
    _description = 'Ingredients'

    name = fields.Char(string="Nom")
    ingredient_table_ids = fields.One2many('recipe.ingredient.table', 'ingredient_id')


class RecipeIngredientUom(models.Model):
    _name = 'recipe.ingredient.uom'
    _description = 'Units of Mesure'

    name = fields.Char(string="Nom")

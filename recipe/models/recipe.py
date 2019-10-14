# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import Warning

class RecipeBook(models.Model):
    _name = 'recipe.book'

    name = fields.Char()
    recipe_type = fields.Selection([('starter','Starter'),('course','Course'),('dessert','Dessert')])
    season_ids = fields.Many2many('recipe.season')
    image = fields.Binary()
    time = fields.Float()

    description = fields.Text()

    ingredient_table_ids = fields.One2many('recipe.ingredient.table', 'recipe_id')


class RecipeIngredientTable(models.Model):
    _name = 'recipe.ingredient.table'

    recipe_id = fields.Many2one('recipe.book')
    ingredient_id = fields.Many2one('recipe.ingredient')
    quantity = fields.Float()
    uom = fields.Selection([('kg','Kg'),('pc','Pc')])    


class RecipeIngredient(models.Model):
    _name = 'recipe.ingredient'

    name = fields.Char()

    ingredient_table_ids = fields.One2many('recipe.ingredient.table', 'ingredient_id')


class RecipeSeason(models.Model):
    _name = 'recipe.season'

    name = fields.Char()
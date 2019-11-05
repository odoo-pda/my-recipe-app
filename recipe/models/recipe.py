# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import Warning

class RecipeBook(models.Model):
    _name = 'recipe.recipe'
    _description = 'Recipe'

    name = fields.Char()
    recipe_type_ids = fields.Many2many('recipe.type', string="Type of Recipe")
    season_ids = fields.Many2many('recipe.season', string="Seasons")
    image = fields.Binary()
    time = fields.Float(compute='_compute_time', string="Time")
    preparation_time = fields.Float()
    cooking_time = fields.Float()
    shelf_life_time = fields.Char()
    nb_portions = fields.Integer(string="Number of Portions")

    description = fields.Text(string="Instructions")

    ingredient_table_ids = fields.One2many('recipe.ingredient.table', 'recipe_id')

    @api.depends('preparation_time', 'cooking_time')
    def _compute_time(self):
        for rec in self:
            rec.time = rec.preparation_time + rec.cooking_time


class RecipeType(models.Model):
    _name = 'recipe.type'
    _description = 'Type of Recipe'

    name = fields.Char()


class RecipeIngredientTable(models.Model):
    _name = 'recipe.ingredient.table'
    _description = 'Table of Ingredients'

    recipe_id = fields.Many2one('recipe.recipe')
    ingredient_id = fields.Many2one('recipe.ingredient')
    quantity = fields.Float()
    uom_id = fields.Many2one('recipe.ingredient.uom')    


class RecipeIngredient(models.Model):
    _name = 'recipe.ingredient'
    _description = 'Ingredients'

    name = fields.Char()

    ingredient_table_ids = fields.One2many('recipe.ingredient.table', 'ingredient_id')


class RecipeIngredientUom(models.Model):
    _name = 'recipe.ingredient.uom'
    _description = 'Units of Mesure'

    name = fields.Char()


class RecipeSeason(models.Model):
    _name = 'recipe.season'
    _description = 'Seasons'

    name = fields.Char()
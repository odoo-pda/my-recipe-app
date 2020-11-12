# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import Warning

class RecipeBook(models.Model):
    _name = 'recipe.recipe'
    _description = 'Recipe'

    name = fields.Char(string="Nom")
    recipe_type_ids = fields.Many2many('recipe.type', string="Type de Recette")
    main_type_id = fields.Many2one('recipe.type', compute='_compute_main_type_id')
    season_ids = fields.Many2many('recipe.season', string="Saisons")
    image = fields.Binary("Image", attachment=True)
    time = fields.Float(compute='_compute_time', string="Timing")
    preparation_time = fields.Float(string="Temps de préparation")
    cooking_time = fields.Float(string="Temps de cuisson")
    shelf_life_time = fields.Char(string="Durée de conservation")
    nb_portions = fields.Integer(string="Number of Portions")
    cooking_type = fields.Many2many('recipe.cooking.type', string="Type de Cuisine")
    description = fields.Text(string="Instructions")
    ingredient_table_ids = fields.One2many('recipe.ingredient.table', 'recipe_id', string="Ingrédients")
    author = fields.Char(string="Copyright")

    @api.depends('recipe_type_ids')
    def _compute_main_type_id(self):
        for rec in self:
            rec.main_type_id = rec.recipe_type_ids.filtered(lambda t: t.is_principal)[:1]
                
    @api.depends('preparation_time', 'cooking_time')
    def _compute_time(self):
        for rec in self:
            rec.time = rec.preparation_time + rec.cooking_time


class RecipeType(models.Model):
    _name = 'recipe.type'
    _description = 'Type of Recipe'
    _order = 'sequence'

    name = fields.Char(string="Nom")
    is_principal = fields.Boolean(string="Principal")
    sequence = fields.Integer("Séquence", default=100)


class RecipeCookingType(models.Model):
    _name = 'recipe.cooking.type'
    _description = 'Type of Cooking'

    name = fields.Char()


class RecipeSeason(models.Model):
    _name = 'recipe.season'
    _description = 'Seasons'

    name = fields.Char(string="Nom")
    color = fields.Integer(string="Couleur")
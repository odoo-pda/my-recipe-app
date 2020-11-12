# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import Warning

class RecipeBook(models.Model):
    _name = 'recipe.recipe'
    _description = 'Recipe'

    name = fields.Char(string="Nom")
    recipe_type_ids = fields.Many2many('recipe.type', string="Type de Recette")
    main_type_id = fields.Many2one('recipe.type', compute='_compute_main_type_id', store=True)
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

    @api.depends('recipe_type_ids')
    def _compute_main_type_id(self):
        for rec in self:
            if rec.env.ref('recipe_data.recipe_type_main_dish') in rec.recipe_type_ids:
                rec.main_type_id = rec.env.ref('recipe_data.recipe_type_main_dish')
            elif rec.env.ref('recipe_data.recipe_type_starter') in rec.recipe_type_ids:
                rec.main_type_id = rec.env.ref('recipe_data.recipe_type_starter')
            elif rec.env.ref('recipe_data.recipe_type_dessert') in rec.recipe_type_ids:
                rec.main_type_id = rec.env.ref('recipe_data.recipe_type_dessert')
            else:
                rec.main_type_id = rec.env.ref('recipe_data.recipe_type_other')
                
    @api.depends('preparation_time', 'cooking_time')
    def _compute_time(self):
        for rec in self:
            rec.time = rec.preparation_time + rec.cooking_time


class RecipeType(models.Model):
    _name = 'recipe.type'
    _description = 'Type of Recipe'

    name = fields.Char(string="Nom")


class RecipeCookingType(models.Model):
    _name = 'recipe.cooking.type'
    _description = 'Type of Cooking'

    name = fields.Char()


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
    ingredient_type = fields.Many2one('recipe.ingredient.type', string="Type d'ingrédient")


class RecipeIngredientType(models.Model):
    _name = 'recipe.ingredient.type'
    _description = 'Type of Ingredients'

    name = fields.Char(string="Nom")


class RecipeIngredientUom(models.Model):
    _name = 'recipe.ingredient.uom'
    _description = 'Units of Mesure'

    name = fields.Char(string="Nom")


class RecipeSeason(models.Model):
    _name = 'recipe.season'
    _description = 'Seasons'

    name = fields.Char(string="Nom")
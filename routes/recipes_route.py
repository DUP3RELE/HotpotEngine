from flask import request, jsonify, Blueprint
from models import db
from models.recipes import Recipes
from flask_jwt_extended import jwt_required
from datetime import datetime, timezone

recipe_bp = Blueprint('recipies_bp', __name__, url_prefix='/api')


@recipe_bp.route('/create_recipe', methods=['POST'])
@jwt_required()
def create_recipe():
    data = request.get_json()
    restaurant_id = data.get('restaurant_id')
    title = data.get('title')
    content_ingredients = data.get('content_ingredients')
    content_methods = data.get('content_methods')
    date_added = datetime.now(timezone.utc)
    employee_id = data.get('employee_id')

    if not restaurant_id:
        return jsonify({'message': 'Brak restaurant_id'}), 400

    if not title:
        return jsonify({'message': 'Brak tytułu przepisu'}), 400

    if not content_ingredients:
        return jsonify({'message': 'Brak składników'}), 400

    if not content_methods:
        return jsonify({'message': 'Brak metod'}), 400

    existing_recipe = Recipes.query.filter_by(title=title).first()
    if existing_recipe:
        return jsonify({'message': 'Przepis o danym tytule już istnieje'}), 400

    new_recipe = Recipes(
        restaurant_id=restaurant_id,
        title=title,
        content_ingredients=content_ingredients,
        content_methods=content_methods,
        date_added=date_added,
        employee_id=employee_id
    )

    db.session.add(new_recipe)
    db.session.commit()

    return jsonify({'message': 'Przepis został zapisany'}), 200


@recipe_bp.route('/get_recipes', methods=['GET'])
@jwt_required()
def get_recipes():
    restaurant_id = request.args.get('restaurant_id')
    if not restaurant_id:
        return jsonify({'message': 'Brak ID restauracji w żądaniu'}), 400

    recipes = Recipes.query.filter_by(restaurant_id=restaurant_id).all()
    recipes_list = [{'id': rec.id,
                     'title': rec.title,
                     'content_ingredients': rec.content_ingredients,
                     'content_methods': rec.content_methods,
                     'date_added': rec.date_added,
                     'employee_id': rec.employee_id} for rec in recipes]

    return jsonify(recipes_list), 200


@recipe_bp.route('/edit_recipe/<int:recipe_id>', methods=['PUT'])
@jwt_required()
def edit_recipes(recipe_id):
    data = request.get_json()
    recipe = Recipes.query.get(recipe_id)
    if not recipe:
        return jsonify({'message': 'Przepis nie istnieje'}), 404

    recipe.title = data.get('title', recipe.title)
    recipe.content_ingredients = data.get('content_ingredients', recipe.content_ingredients)
    recipe.content_methods = data.get('content_methods', recipe.content_methods)
    recipe.employee_id = data.get('employee_id', recipe.employee_id)
    recipe.date_added = datetime.now(timezone.utc)

    db.session.commit()
    return jsonify({'message': 'Przepis został zaktualizowany'}), 200


@recipe_bp.route('/delete_recipe/<int:recipe_id>', methods=['DELETE'])
@jwt_required()
def delete_recipe(recipe_id):
    recipe = Recipes.query.get(recipe_id)
    if not recipe:
        return jsonify({'message': 'Przepis nie istnieje'}), 400

    db.session.delete(recipe)
    db.session.commit()
    return jsonify({'message': 'Przepis został pomyślnie usunięty'}), 200

from datetime import datetime
from ariadne import convert_kwargs_to_snake_case

from api import db
from api.models import Post


@convert_kwargs_to_snake_case
def create_post_resolver(obj, info, title, description):
    try:
        today = datetime.now()
        post = Post(title=title, description=description, created_at=today)
        db.session.add(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()

        }
    except Exception as e:
        payload = {
            "success": False,
            "errors": [str(e)]
        }
    return payload


@convert_kwargs_to_snake_case
def update_post_resolver(obj, info, id, title, description):
    try:
        post = Post.query.get(id)
        post.title = title
        post.description = description
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except Exception as e:
        payload = {
            "success": False,
            "errors": [str(e)]
        }
    return payload


@convert_kwargs_to_snake_case
def delete_post_resolver(obj, info, id):
    try:
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except Exception as e:
        payload = {
            "success": False,
            "errors": [str(e)]
        }
    return payload


from .models import Post 
def listPosts_resolver(obj, info):
    try:
        posts = [post.to_dict() for post in Post.query.all()]
        
        print("Todos los posts: ", posts)
        payload = {
            "success": True,
            "posts": posts,
        }

    except Exception as e:
        payload = {
            "success": False,
            "errors": [str(e)]
        }
    return payload


from ariadne import convert_kwargs_to_snake_case


@convert_kwargs_to_snake_case
def getPost_resolver(obj, info, id):
    try:
        post = Post.query.get(id)
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except Exception as e:
        payload = {
            "success": False,
            "errors": ["Post item matching id {id} not found".format(id=id)]
        }
    return payload


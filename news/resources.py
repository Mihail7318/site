from import_export import resources
from news.models import Post

class PostResource(resources.ModelResource):
    class Meta:
        model = Post
from views import *

urlpatterns = [
    ('cars/', car_list),
    ('product-create/', car_create),
    ('product-detail/id', car_detail),
    ('product-update/id', car_update),
    ('product-delete/id', car_delete),
    ('comment-create/', comment_create),
    ('like-add', add_like)
]

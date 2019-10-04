from flask_appbuilder import ModelView, AppBuilder, expose, BaseView, has_access
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.widgets import ListBlock, ShowBlockWidget

from . import appbuilder, db
from .models import ProductType, Product


class ProductTypeView(ModelView):
    datamodel = SQLAInterface(ProductType)

    list_columns = ["id", "name"]

    base_order = ("name", "asc")

    show_fieldsets = [
        ("Summary", {"fields": ["id", "name"]}),
    ]

    add_fieldsets = [
        ("Summary", {"fields": ["name"]}),

    ]

    edit_fieldsets = [
        ("Summary", {"fields": ["name"]}),
    ]


class ProductView(ModelView):
    datamodel = SQLAInterface(Product)

    label_columns = {"photo_img": "Photo"}

    list_columns = ["name", "photo_img", "price_label"]
    search_columns = ["name", "price", "product_type"]

    show_fieldsets = [
        ("Summary", {"fields": ["name", "price_label", "photo_img", "product_type"]}),
        ("Description", {"fields": ["description"], "expanded": True}),
    ]


class MyCustomView(BaseView):
    route_base = "/"

    @expose('/<string:param1>')
    @has_access
    def method1(self, param1):
        # do something with param1
        # and return it
        return "<h1>Hello world</h1>"

    @expose('/method2/<string:param1>')
    @has_access
    def method2(self, param1):
        # do something with param1
        # and render it
        param1 = 'Hello %s' % (param1)
        return param1


db.create_all()
appbuilder.add_view(
    ProductTypeView, "List Product Type", icon="fa-envelope", category="Product Type"
)

appbuilder.add_view(
    ProductView, "List Product", icon="fa-envelope", category="Products"
)
appbuilder.add_view_no_menu(MyCustomView())
appbuilder.add_link("Method3", href='/myview/method1/john', category='My View')

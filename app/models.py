from flask import Markup, url_for
from flask_appbuilder import Model
from flask_appbuilder.filemanager import ImageManager
from flask_appbuilder.models.mixins import ImageColumn
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship


class ProductType(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Product(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    price = Column(Float, nullable=False)
    photo = Column(ImageColumn)
    description = Column(Text())
    product_type_id = Column(Integer, ForeignKey("product_type.id"), nullable=False)
    product_type = relationship("ProductType")

    def __repr__(self):
        return self.name

    def photo_img(self):
        im = ImageManager()
        if self.photo:
            return Markup(
                '<a href="' +
                url_for("ProductView.show", pk=str(self.id)) +
                '" class="thumbnail"><img src="' +
                im.get_url(self.photo) +
                '" alt="Photo" class="img-rounded img-responsive"></a>'
            )
        else:
            return Markup(
                '<a href="' +
                + url_for("ProductView.show", pk=str(self.id)) +
                '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive">'
                '</a>'
            )

"""
Products
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class ProductForm(FlaskForm):
    """
    Product Form
    """
    name = StringField(
        label="Product name",
        name="product-name",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
        # render_kw={'class': 'form-control'}
    )
    # description = TextAreaField(validators=[DataRequired()])

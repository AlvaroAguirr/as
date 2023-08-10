from flask import Blueprint, render_template, redirect ,url_for,request,flash
from models.brand import Brand

from forms.brand_forms import CreateBrandForm, UpdateBrandForm
brand_views = Blueprint ('brand',__name__)

@brand_views.route("/Marca/")
def brands():
    brand=Brand.get_all()
    return render_template('brand/brand.html',brand=brand)

@brand_views.route("/Marca/crear", methods=('Get','Post'))
def create_bra():
    form= CreateBrandForm()
    return render_template('/brand/create_bra.html', form=form )

@brand_views.route("/Marca/Editar", methods=('Get','Post'))
def editar_bra():
    return render_template('/brand/create_bra.html',)

@brand_views.route("/Marca/Editar", methods=('POST',))
def eliminar_bra():
    return render_template('/brand/create_bra.html',)

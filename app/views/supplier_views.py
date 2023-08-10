from flask import Blueprint, render_template, redirect ,url_for,request,flash
from models.supplier import Supplier

from forms.supplier_forms import CreateSupplierForm,UpdateSupplierForm
supplier_views = Blueprint ('supplier',__name__)

@supplier_views.route("/supplier/")
def suppliers():
    supplier=Supplier.get_all()
    return render_template('supplier/supplier.html', supplier=supplier )

@supplier_views.route("/supplier/create_sup", methods=('GET','POST'))
def create_sup():
    form=CreateSupplierForm()
    if form.validate_on_submit():
        nombre=form.nombre.data
        sup= Supplier(nombre)
        sup.save()
        return redirect(url_for('supplier.suppliers'))

    return render_template("/supplier/create_sup.html", form=form)

@supplier_views.route("/supplier/Editar")
def editar_sup():
    return render_template("/supplier/create_sup.html")


@supplier_views.route("/supplier/del")
def delete_sup():
    return render_template("/supplier/create_sup.html")
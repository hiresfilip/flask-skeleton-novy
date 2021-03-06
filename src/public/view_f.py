"""
Logic for dashboard related routes
"""
import math

from flask import Blueprint, render_template
from .forms import LogUserForm, secti,masoform, formfiliph,formfiliph2
from ..data.database import db
from ..data.models import LogUser
from views import blueprint



@blueprint.route('/vypis_filip',methods=['GET'])
def Vypis_filip():
    pole=[[0,1],[2,3], [20,30]]
    return render_template("public/vypis_filiph.tmpl", data = pole)
@blueprint.route('/formular_filiph', methods=['GET', 'POST'])
def Formular_filiph1():
    form = formfiliph()
    if form.validate_on_submit():
        return 0
    return render_template("public/formular_filiph.tmpl", form=form)

@blueprint.route('/formularfiliptest', methods=['GET', 'POST'])
def Formular_filiph():
    form = formfiliph()
    if form.validate_on_submit():
        return str(form.a.data * form.b.data)
    return render_template("public/formularfiliptest.tmpl", form=form)

@blueprint.route('/advancedforms', methods=['GET', 'POST'])
def jgdfjksdghfjksd():
    form = formfiliph2()
    if form.validate_on_submit():
        return "OK"
        '''obvod ctverec
        if int(form.oo.data) == 1 and int(form.obrazec.data) == 1:
            hodnota = str(4*form.a.data)
            return render template("public/vystupnihodnoty.tmpl")
        if int(form.oo.data) == 1 and int (form.obrazec.data == 2):
            return str((form.a.data) * (form.b.data))
        if int (form.oo.data) == 1 and int (form.obrazec.data == 3):
            return str(((form.a.data) * math.sqrt(form.a.data * form.a.data - ((form.c.data * form.c.data) / 2))) / 2)
        if int (form.oo.data == 2) and int (form.obrazec.data == 1):
            return str(4 * form.a.data)
        if int (form.oo.data == 2) and int (form.obrazec.data == 2):
            return str(2 * form.a.data + 2 * form.b.data)
        if int (form.oo.data) == 2 and int (form.obrazec.data == 3):
            return str(form.a.data + form.b.data + form.c.data)'''
    return render_template("public/formularfiliptest.tmpl", form=form)


@blueprint.route("/simple_chart")
def chart():
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('public/graf.tmpl', values=values, labels=labels, legend=legend)


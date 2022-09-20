import json
from landing import app
from flask import render_template,request,redirect
from .forms import LandingForm

from .models import EmailSignup


@app.route('/', methods=['GET','POST'])
@app.route('/home/', methods=['GET','POST'])
def home():
  form = LandingForm()
  if form.validate_on_submit():
    data = form.data 
    if 'csrf_token' in data:
      del data['csrf_token']
    obj = EmailSignup.query.filter_by(email=form.email.data).first()
    print(obj)
    if obj is None:
      obj = EmailSignup(**data)
      obj.save()
    return redirect("/item/{}".format(obj.id))
  
  
  return render_template('home.html', form=form)

@app.route("/item/<int:id>", methods=["GET", "POST"])
def item_detail(id):
  if request.method == "GET":
    instance = EmailSignup.query.filter_by(id=id).first_or_404()
    return render_template("items/detail.html", instance=instance)    
  else :
    return render_template("home.html", form=form)

@app.route("/item/<int:id>/update/", methods=['GET', 'POST'])  
def item_update(id):
  instance = EmailSignup.query.filter_by(id=id).first_or_404()
  form = LandingForm(obj=instance)
  if form.validate_on_submit():
    full_name = form.full_name.data
    email = form.email.data
    instance.full_name=full_name
    instance.email=email
    instance.save()
    return redirect("/item/{}".format(instance.id))
  return render_template('items/form.html', instance=instance, form=form)
  
  
from landing import app
from flask import render_template

@app.route("/profiles/<name>")
def profile(name):
  context = {"name":name}
  context["usr_msg"] = "Unknown"
  if name=='aanv':
    context["usr_msg"]="Approved "
    
  return render_template('profile_details.html', context=context)
  

@app.route("/profileview")
def profileview():
  return render_template("profiles_list.html")
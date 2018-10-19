from flask import Flask, render_template,request,redirect
app = Flask(__name__)
id=1
tasks = {
	1 : {
		"id": 1,
		"name": "get coffee",
		"description": "none of that cheap stuff",
		"urgent": False,
		"done": True
	},
	2 : {
		"id": 2,
		"name": "get milk",
		"description": "in a carton",
		"urgent": True,
		"done":False
	},
}
next_id=3

@app.route("/")
def show_hi():
	return render_template("index.html", tasks=tasks) 
    
@app.route('/add',methods=["GET","POST"])
def you_add():
	global next_id
	if request.method=="POST":
		new_item={
			"id":next_id,
    		"name":request.form["name"],
    		"description":request.form["desc"],
    		"urgent":"urgent" in request.form,
    		"done":"done" in request.form
    	}
		tasks[next_id]=new_item
		next_id +=1
		return redirect("/")
	else:
		return render_template("add.html")
    	
@app.route('/edit/<int:id>',methods=["GET","POST"])
def edit(id):
	if request.method=="POST":
		item={
			"id":id,
			"name":request.form["edit_name"],
			"description":request.form["edit_desc"],
			"urgent":"urgent" in request.form,
			"done":"done" in request.form
		}
		tasks[id]=item
		return redirect("/")
	else:
		return render_template("edit_form.html", task=tasks[id])
 
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=8080, debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
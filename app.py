from flask import Flask ,render_template, request

app = Flask(__name__)

with open('ingredients.txt','r') as IL:
    ing_dict = {}
    for line in IL:
        key, value = line.strip().split(':')
        ing_dict[key] = value

with open('instructions.txt','r') as I:
    ins_dict = {}
    for line in I:
        key, value = line.strip().split(':')
        ins_dict[key] = value

with open('yield.txt','r') as Y:
    yield_dict = {}
    for line in Y:
        key, value = line.strip().split(':')
        yield_dict[key] = value

@app.route("/")
def homePage():
    return render_template('home.html')

@app.route("/menu" , methods = ['GET', 'POST']) 
def menu():
    if request.method == 'POST':
        meal = request.form['Meal']
        ingre = ing_dict[meal]
        ins = ins_dict[meal]
        yd = yield_dict[meal]
        return render_template('menu.html', food = meal, des1 = ingre, des2 = ins, des3 = yd)

if __name__ == "__main__":
   app.run(debug=True)
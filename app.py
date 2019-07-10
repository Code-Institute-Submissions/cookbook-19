import os
from flask import Flask, render_template, request, redirect, flash, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app=Flask(__name__)

app.secret_key=os.getenv("SECRET","randomstring123")

app.config["MONGO_DBNAME"]='milestone-3'
app.config["MONGO_URI"]='mongodb+srv://Shilldon:Palad1n1@myfirstcluster-gzjbi.mongodb.net/milestone-3'

mongo=PyMongo(app)

@app.route("/")

def index():
   return render_template("index.html",title_text='Perfect dishes on demand')

@app.route("/add_recipe")

def add_recipe():
    return render_template("add_recipe.html", title_text='Add recipe')

@app.route("/insertrecipe/", methods=['POST'])
def insertrecipe():
    #check whether the user is adding a new recipe or editting a recipe
    edit=request.args.get('edit',None)
    
    #if editing a recipe get the ID of the recipe to edit
    if edit=='True':
        recipe_id=request.args.get('recipe_id',None)
    
    recipes=mongo.db.recipeDB
    #request form data not in flat format - arrays are created in the form for ingredients and allergen information
    new_recipe=request.form.to_dict(flat=False)
    ingredients=[]
    ingredient={}
    #initialise cook time variable to convert hours and minutes to minutes total for ease of search DB in recipe_list
    cook_time=0
    for key, key_name in new_recipe.items():
        #flatten dict for non-array items which have become arrays through request object
        if key!='type' and key!='amount' and key!='unit' and key!='allergens':
            new_recipe[key]=new_recipe[key][0]

            if key=='favourite':
                if new_recipe[key].lower() =='true':
                    new_recipe[key]=True
                else:
                    new_recipe[key]=False    
            if key=='hours' or key=='minutes' or key=='calories':
                #convert from string to int, if needed
                try:
                    new_recipe[key]=int(new_recipe[key])
                except ValueError:
                    pass
            if key=='hours':
                #convert hours to minutes and add to cook time
                cook_time=new_recipe[key]*60
            if key=='minutes':
                cook_time=cook_time+new_recipe[key]
            
        elif key=='type':
            #cycle through the ingredient information and create objects for each ingredient with key values of ingredient type, amount and units
            i=0
            for ingredient_type in key_name:

                ingredient={ 'type' : ingredient_type , 'amount' : new_recipe['amount'][i] , 'unit' : new_recipe['unit'][i] }
                #insert ingredient object into array of ingredients
                ingredients.append(ingredient)
                i+=1       
    #insert the new cook_time key into the new_recipe dict
    new_recipe["cook_time"]=cook_time
    #insert the new ingredients array into the new_receipe dict
    new_recipe['ingredients']=ingredients            
    
    #need to remove the type, amount and unit arrays from the dict having imported them into ingredients objects
    #done by error testing because ingredients may not have been added via the form
    try:
        del new_recipe['type']
    except KeyError:
        pass
    try:
        del new_recipe['amount']
    except KeyError:
        pass    
    try:
        del new_recipe['unit']
    except KeyError:
        pass    
    
    if edit=='True':
        recipes.update({'_id':ObjectId(recipe_id)},new_recipe)
    else:
        recipes.insert_one(new_recipe)
        print("New recipe added",new_recipe)
    return render_template('display_recipe.html',title_text='Your recipe',recipe=new_recipe)

@app.route("/search")

def search():
    return render_template("search.html",title_text="Find your favourites")

@app.route("/recipe_list", methods=['POST','GET'])
def recipe_list():
   # print("recipe list form",session["filters"])
    
    dict=request.form.to_dict()
    if dict:
        for key, value in dict.items():
            if value=='false':
                dict[key]=False
            elif value=='true':
                dict[key]=True
            elif key=="calories":
                print("upddate calories in dict")
                if int(value)==999:
                    dict[key]={'$gt':int(value)}
                else:
                    dict[key]={'$lt':int(value)}    
            elif key=="cook_time":
                if int(value)==179:
                    dict[key]={'$gt':int(value)}
                else:
                    dict[key]={'$lt':int(value)}                 


    print("dict updated",dict)
    
    try:
        print("recipe list form",session["filters"])
    except KeyError:
        pass
    
    if dict:
        print("search dictionary exists, therefore searching against it")
        _recipe_list=mongo.db.recipeDB.find(dict)
    else:
        _recipe_list=mongo.db.recipeDB.find()    

    #create a list of countries and authors referred to in recipe db to generate filters in recipe_list
    full_list_of_country_recipes=mongo.db.recipeDB.find({"country":{'$exists':True}})
    full_list_of_author_recipes=mongo.db.recipeDB.find({ "author":{'$exists':True}})
    
    unsorted_country_list=[]
    unsorted_author_list=[]
    
    for recipe in full_list_of_country_recipes:
        #if the country key value is not blank add it to the list
        if recipe["country"]:
            unsorted_country_list.append(recipe["country"]) 
            
    for recipe in full_list_of_author_recipes:
        #if the author key value is not blank add it to the list
        if recipe["author"]:
            unsorted_author_list.append(recipe["author"]) 
    
    #remove duplicates from the lists
    _country_list=list(dict.fromkeys(unsorted_country_list))
    _author_list=list(dict.fromkeys(unsorted_author_list))

    
    _todo=request.args.get('action',None)
    if _todo=="delete":
        title_text_value="Delete recipes"
    elif _todo=="edit":
        title_text_value="Edit recipes"
    else:
        title_text_value="Your recipes"
    
    try:
        del request.session['filters']
    except AttributeError:
        pass
    
    return render_template("recipe_list.html",title_text=title_text_value,recipes=_recipe_list,countries=_country_list,authors=_author_list,action=_todo)

@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    _recipe=mongo.db.recipeDB.find_one({"_id":ObjectId(recipe_id)})
    return render_template('display_recipe.html',title_text="Your recipe",recipe=_recipe)

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    _recipe=mongo.db.recipeDB.find_one({"_id":ObjectId(recipe_id)})
    return render_template('edit_recipe.html',title_text="Edit your recipes",recipe=_recipe)

#@app.route('/update_recipe')
#def update_recipe():
#    return True

@app.route('/delete_recipe',methods=['POST'])
def delete_recipe():
    recipe_id=request.form.get('recipe_id')
    _recipe=mongo.db.recipeDB.remove({"_id":ObjectId(recipe_id)})
    print("delete ",recipe_id)
    return redirect('recipe_list')

@app.route('/filter_recipes', methods=['POST'])
def filter_recipes():
    session["filters"]=request.form.to_dict()
    calories=request.form["calories"]
    if calories:
        session["filters"]["calories"]=calories
    print("calories:",calories)
    return redirect('recipe_list')
    
if __name__ =="__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)    
    
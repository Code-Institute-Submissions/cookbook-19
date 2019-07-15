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
    print("blanking session variable")
    session["filters"]={}
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
    return render_template('display_recipe.html',title_text='Your recipe',recipe=new_recipe,added="true")

@app.route("/search")

def search():
    return render_template("search.html",title_text="Find your favourites")

@app.route("/recipe_list", methods=['POST','GET'])
def recipe_list():

    _sort=session["sort"]
    _filter_dict=session["filters"]
    if _filter_dict==None:
        _filter_dict={}
        
    allergen_list=[]
    #get the action request from the page to determine what sort of list is to be displayed and display appropriate title text 
    _todo=request.args.get('action',None)
    if _todo=="delete":
        title_text_value="Delete recipes"
    elif _todo=="edit":
        title_text_value="Edit recipes"
    else:
        title_text_value="Your recipes"

    #check if the results are to be filtered/sorted using variable passed from recipe_list
    filter=request.args.get('filter',None)

    if filter=='true':    
        _currentsort=request.form.get('sort_by')
        print("_sort=",_sort)
        if _currentsort!=None:
            _sort=_currentsort
            session["sort"]=_sort
        else:
            filter_favourites=request.form.get('favourite')
            if filter_favourites:
                if filter_favourites=='false':
                    filter_favourites=False
                elif filter_favourites=='true':
                    filter_favourites=True 
                _filter_dict.update({"favourite" : filter_favourites })
            else:
                _filter_dict.pop("favourite",None)            
                    
            filter_meal=request.form.get('meal')
            print("filter meal ",filter_meal)
            if filter_meal!="" and filter_meal!=None:
                _filter_dict.update({"meal":filter_meal})
            else:
                _filter_dict.pop("meal",None)
            
            filter_allergens=request.form.getlist('allergens')
            if filter_allergens:
                loop=0
                for allergen in filter_allergens:
                    allergen_list.append(allergen)
                filter_allergens={  '$nin' : allergen_list }   
                _filter_dict.update({"allergens" : filter_allergens}) 
            else:
                _filter_dict.pop("allergens",None)
                
            filter_calories=request.form.get('calories')
            if filter_calories!="" and filter_calories!=None:
                if filter_calories==999:
                    filter_calories={'$gt':filter_calories}
                else:
                    filter_calories={'$lt':filter_calories}  
                _filter_dict.update({"calories":filter_calories})
            else:
                _filter_dict.pop("calories",None)
                
            filter_cooktime=request.form.get('cook_time')
            if filter_cooktime!="" and filter_cooktime!=None:
                if filter_cooktime==179:
                    filter_cooktime={'$gt':filter_cooktime}
                else:
                    filter_cooktime={'$lt':filter_cooktime}  
                _filter_dict.update({"cook_time" : filter_cooktime})
            else:
                _filter_dict.pop("cook_time",None)
                
            filter_country=request.form.get('country')
            if filter_country!="" and filter_country!=None:
                _filter_dict.update({"country" : filter_country})
            else:
                _filter_dict.pop("country",None)
            
            filter_author=request.form.get('author')
            if filter_author!="" and filter_author!=None:
                _filter_dict.update({"author" : filter_author})
            else:
                _filter_dict.pop("author",None)
                
            session["filters"]=_filter_dict

        
    if filter=='true':
    #do the appropriate search and sort against the mongoDB depending on input from form/session variable
        if _sort!=None and _sort!="none":
            _recipe_list=mongo.db.recipeDB.find(_filter_dict).sort(_sort,1) 
        else:
            _recipe_list=mongo.db.recipeDB.find(_filter_dict)
    else:
        if _sort!="none" and _sort!=None:
            _recipe_list=mongo.db.recipeDB.find().sort(_sort,1) 
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
    
    _total_results=_recipe_list.count()

    return render_template("recipe_list.html",title_text=title_text_value,recipes=_recipe_list,countries=_country_list,authors=_author_list,action=_todo,filters=_filter_dict, allergens=allergen_list, sort=_sort, total_results=_total_results)
'''
    _sort=request.form.get('sort_by')
    print("sort=",_sort)
    
    #get details of any filters applied
    if _sort==None:
        _filter_dict=request.form.to_dict(flat=False)
        print("got filter dict from form")
    else:
        _filter_dict=session["filters"]
        print("got filter dict from session")
    
    allergen_list=[]

    #check if the results are to be filtered using variable passed from recipe_list
    filter=request.args.get('filter',None)
    
    #if so cycle through the dictionary and convert form results to mongo search strings to enable the mongo request to run correctly.

    if filter=='true':
        if _filter_dict:
            #if the filters have been submitted from the form, apply them to a session variable to retrieve later
            session["filters"]=_filter_dict 
            #flatten dictionary as all results but allergens should not be lists:
            for key, value in _filter_dict.items():
                if key !="allergens":
                    _filter_dict[key]=_filter_dict[key][0]
        else:
            #if filters not retrieved from the form, apply from session variable.
            #This ensures if the user presses 'back' from display recipe the filters on the search list are retained
            _filter_dict=session["filters"]
            print("_filter_dict updated from session ",_filter_dict)
        
        #check if the results list is to be filtered in order to return appropriate list in mongo request
        _sort=_filter_dict.get("sort_by","none")
        
        if _sort!="none":
            #need to remove sort_by from the dictionary before applying filters - sort_by is not a valid filter
            _sort=str(_filter_dict["sort_by"])
            del _filter_dict["sort_by"]
            session["sort"]=_sort
      #  else:
      #      _sort=session["sort"]
        
        #iterate through the filter dictionary and standardise the values for mongoDB search    
        for key, value in _filter_dict.items():
            if value=='false':
                _filter_dict[key]=False
            elif value=='true':
                _filter_dict[key]=True
            elif key=="calories":
                if int(value)==999:
                    _filter_dict[key]={'$gt':int(value)}
                else:
                    _filter_dict[key]={'$lt':int(value)}    
            elif key=="cook_time":
                if value==179:
                    _filter_dict[key]={'$gt':int(value)}
                else:
                    _filter_dict[key]={'$lt':int(value)}  
            elif key=="allergens":
                allergen_list=[]
                loop=0
                for allergen in _filter_dict[key]:
                    allergen_list.append(allergen)
                _filter_dict[key]={  '$nin' : allergen_list }   

'''
@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    _recipe=mongo.db.recipeDB.find_one({"_id":ObjectId(recipe_id)})
    print("checking session variable=",session["filters"])    
    return render_template('display_recipe.html',title_text="Your recipe",recipe=_recipe)

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    _recipe=mongo.db.recipeDB.find_one({"_id":ObjectId(recipe_id)})
    return render_template('edit_recipe.html',title_text="Edit your recipes",recipe=_recipe)

@app.route('/delete_recipe',methods=['POST'])
def delete_recipe():
    recipe_id=request.form.get('recipe_id')
    _recipe=mongo.db.recipeDB.remove({"_id":ObjectId(recipe_id)})
    return redirect(url_for('.recipe_list',action='delete'))

@app.route('/filter_recipes', methods=['POST'])
def filter_recipes():
    session["filters"]=request.form.to_dict()
    calories=request.form["calories"]
    if calories:
        session["filters"]["calories"]=calories
    return redirect('recipe_list')
    
if __name__ =="__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)    
    
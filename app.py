import os
from flask import Flask, render_template, request, redirect, flash, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app=Flask(__name__)

app.secret_key=os.getenv("SECRET","randomstring123")

app.config["MONGO_DBNAME"]='milestone-3'
app.config["MONGO_URI"]='mongodb+srv://Shilldon:Palad1n1@myfirstcluster-gzjbi.mongodb.net/milestone-3'

mongo=PyMongo(app)

@app.route("/check_user",methods=['POST','GET'])
def check_user():
    usersdb=mongo.db.usersDB
    
    user=request.form.to_dict()
    if user['username']=="logout":
        session.pop('user')
    else:    
        session["user"]=user['username']

    if user['username'] not in usersdb.find():
        usersdb.insert({'name':user['username'],'favourites':[], 'liked':[]})  
        
    return redirect(url_for('index'))

@app.route("/")

def index():
    session["filters"]={}
    return render_template("index.html",title_text='Perfect dishes on demand')

@app.route("/add_recipe")

def add_recipe():
    #get list of ingredients to display in auto complete form for ingredients in add_recipe.html
    ingredientsdb=mongo.db.ingredientsDB
    ingredients=ingredientsdb.find()
    _ingredients={}
    for ingredient in ingredients:
        new_ingredient={ingredient["name"]:None}
        _ingredients.update(new_ingredient)
        
    #get list of authors to display in auto complete form for authors in add_recipe.html
    authordb=mongo.db.authorDB
    authors=authordb.find()
    _authors={}
    for author in authors:
        new_author={author["name"]:None}
        _authors.update(new_author)

    #get list of countries to display in auto complete form for countries in add_recipe.html
    countrydb=mongo.db.countriesDB
    countries=countrydb.find()
    _countries={}
    for country in countries:
        new_country={country["name"]:None}
        _countries.update(new_country)

    return render_template("add_recipe.html", title_text='Add recipe',ingredients_list=_ingredients, author_list=_authors, country_list=_countries)

@app.route("/insertrecipe/", methods=['POST'])
def insertrecipe():
    #check whether the user is adding a new recipe or editting a recipe
    edit=request.args.get('edit',None)
        
    recipes=mongo.db.recipeDB
    
    #if editing a recipe get the ID of the recipe to edit
    if edit=='True':
        recipe_id=ObjectId(request.args.get('recipe_id'))
    else:
        recipe_id=recipes.insert({'name':'new'})
    
    #request form data not in flat format - arrays are created in the form for ingredients and allergen information
    new_recipe=request.form.to_dict(flat=False)
    print("new_Recipe[type]",new_recipe["type"])
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
                print("key name ",key_name)
                print('ingredient_Type ',ingredient_type)
                ingredient={ 'type' : ingredient_type , 'amount' : new_recipe['amount'][i] , 'unit' : new_recipe['unit'][i] }
                #insert ingredient object into array of ingredients
                ingredients.append(ingredient)
                print("ingredient added=",ingredient)
                i+=1       
    #insert the new cook_time key into the new_recipe dict
    new_recipe["cook_time"]=cook_time
    #insert the new ingredients array into the new_receipe dict
    new_recipe['ingredients']=ingredients            

    current_recipe=recipes.find_one({"_id" : ObjectId(recipe_id)})
    print("recipe id ",recipe_id)
    print("new_recipe", new_recipe)
    print("current_recipe ", current_recipe)
    
    new_ingredients=ingredients
    ingredientsdb=mongo.db.ingredientsDB

    for ingredient in new_ingredients:
        ingredient_type=ingredient
        print("ingredient_type",ingredient_type)
        if edit=="True":
            current_ingredients=current_recipe["ingredients"]
            print("current_ingredients", current_ingredients)
            if ingredient in current_ingredients:
                ingredient_index=current_ingredients.index(ingredient)
                current_ingredients.remove(ingredient)
            
        new_ingredient_doc=ingredientsdb.find_one({"name" : ingredient})
        if new_ingredient_doc!=None:
            new_ingredient_id=new_ingredient_doc["_id"]
        else:
            new_ingredient_id=ingredientsdb.insert({"name" : ingredient["type"], "recipe":[]})
            new_ingredient_doc=ingredientsdb.find_one({"_id" : new_ingredient_id})
        if recipe_id not in new_ingredient_doc["recipe"]:
            ingredientsdb.update({"_id": new_ingredient_id},{"$push":{"recipe" : recipe_id}})

    if edit=="True":
        print("current recipe !=None")
        for ingredient in current_ingredients:
            if ingredient not in new_ingredients:
                print("ingredient not in new ingredients=",ingredient)
                current_ingredient_doc=ingredientsdb.find_one({"name" : ingredient["type"]})  
                current_ingredient_id=current_ingredient_doc["_id"]
                ingredientsdb.update({"_id": current_ingredient_id},{"$pull":{"recipe" : recipe_id}})
                current_ingredient_doc=ingredientsdb.find_one({"_id": current_ingredient_id})
                if len(current_ingredient_doc["recipe"])==0:
                    ingredientsdb.remove({"_id": current_ingredient_id})  
    
    categories=["allergens","meal","country","author"]
    for category in categories:
        if category in new_recipe:
            if type(new_recipe[category]) is list:
                new_category=new_recipe[category]
            else:    
                new_category=[]
                new_category.append(new_recipe[category])
        else:
            new_category=[]
        
        if category=="allergens":    
            categorydb=mongo.db.allergensDB
        elif category=="meal":
            categorydb=mongo.db.mealDB
        elif category=="country":
            categorydb=mongo.db.countriesDB
        elif category=="author":
            categorydb=mongo.db.authorDB            
        elif category=="difficulty":
            categorydb=mongo.db.difficultyDB   
            
        print("new_category=",category)
        for value in new_category:
            print("value=",value)
            #check if we are edtting an existing recipe, if so check whether any values existing in both the updated and current recipes 
            #if so remove them from the list to later delete the recipe ID from the values that remain in the list
            if edit=="True":
                if category in current_recipe:
                    if type(new_recipe[category]) is list:
                        current_category=current_recipe[category]
                    else:    
                        current_category=[]
                        current_category.append(new_recipe[category])                    
                    if value in current_category:
                        category_index=current_category.index(value)
                        print("category_index=",category_index)
                        print("current_Category=",type(current_category))
                        current_category.remove(value)
        
            #get the name of the new value in this category        
            new_category_doc=categorydb.find_one({"name" : value}) 
            if new_category_doc!=None:
                #if the particular object exists then get the associated doc
                new_category_id=new_category_doc["_id"]
            else:
                #if it doesn't exist createa a new doc with the name and the ID of this recipe
                new_category_id=categorydb.insert({"name" : value, "recipe":[]})
                new_category_doc=categorydb.find_one({"_id" : new_category_id})
            if recipe_id not in new_category_doc["recipe"]:
                #check if the recipe is already in the new doc, if it isn't add the recipe ID to this particular category in the DB
                categorydb.update({"_id" : new_category_id},{"$push":{"recipe":recipe_id}})

        if edit=="True":
            #if we are editing a recipe check whether there are any remaining values in the category list
            if category in current_recipe:
                #if so, then for all the values remove the recipe ID from the particular category in the DB
                for value in current_category:
                    if value not in new_category:
                        current_category_doc=categorydb.find_one({"name" : value})
                        current_category_id=current_category_doc["_id"]
                        categorydb.update({"_id" : current_category_id},{"$pull" : {"recipe" : recipe_id}})
                        current_category_doc=categorydb.find_one({"_id" : current_category_id})
                        #if this particular category is empty, delete it from the DB
                        if len(current_category_doc["recipe"])==0:
                            categorydb.remove({"_id" : current_category_id})


                    
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
        recipes.update({'_id':ObjectId(recipe_id)},new_recipe)
        
    return redirect(url_for('show_recipe',recipe_id=recipe_id,added_recipe="true"))

'''
def update_category_database(edit,recipe_id,recipes,new_recipe,category,category_db):

    #Update category database
    if edit=="True":
        current_recipe_doc=recipes.find_one({"_id" :recipe_id})
        print("current recipe doc", current_recipe_doc)
    else:
        current_recipe_doc={}

    if new_recipe[category]:
        new_category_doc=category_db.find_one({"name" : new_recipe[category]})
        if new_category_doc!=None:
            new_category_id=new_category_doc["_id"]
        else:
            new_category_id=category_db.insert({"name" : new_recipe[category]})
            new_category_doc=category_db.find_one({"_id" : new_category_id})
    else:
        new_category_doc={}
        new_category_id=""

    if current_recipe_doc!={}:
        current_category_id=current_recipe_doc[category]
        if current_category_id!="":
            category_id=ObjectId(current_category_id)
            current_category_doc=category_db.find_one({"name" : category})
        else:
            category_id=""
            current_category_doc={}
    else:
        current_category_id=""
        current_category_doc={}
        
    if new_category_doc!=current_category_doc:
        if current_category_doc!={}:
            if current_category_id!=None:
                category_id=ObjectId(current_category_id)
            else:
                category_id=""
            category_db.update({"_id": category_id},{"$pull":{"recipe" : recipe_id}})
            current_category_doc=category_db.find_one({"_id": category_id})
            if len(current_category_doc["recipe"])==0:
                category_db.remove({"_id": category_id})    
    if new_category_doc!={}:
        #new_recipe[category]=str(new_category_doc["_id"])
        category_db.update({"_id": new_category_id},{"$push":{"recipe" : recipe_id}})
    return  
'''

@app.route("/search")
def search():
    return render_template("search.html",title_text="Find your favourites")

@app.route("/recipe_list", methods=['POST','GET'])
def recipe_list():

    if session.get('sort')==True:
        _sort=session["sort"]
    else:
        _sort='none'
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

    #create a list of countries and authors referred to in recipe db to generate filters in recipe_list
    list_of_countries=mongo.db.countriesDB.find()
    list_of_authors=mongo.db.authorDB.find()

    #define filter author and country for passing to filter list in recipe_list.html.
    #Will check for "" value and if so, not display author/country filter
    filter_country=""
    filter_author=""

    print("filter=",filter)
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
 #               country=mongo.db.countriesDB.find_one({"name" : filter_country})
  #              _filter_dict.update({"country" : str(country["_id"])})
                _filter_dict.update({"country" : filter_country })
            else:
                _filter_dict.pop("country",None)
            
            filter_author=request.form.get('author')
            if filter_author!="" and filter_author!=None:
   #             author=mongo.db.authorDB.find_one({"name" : filter_author})
#                _filter_dict.update({"author" : str(author["_id"])})
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
        print("_sort",_sort)
        if _sort!="none" and _sort!=None:
            _recipe_list=mongo.db.recipeDB.find().sort(_sort,1) 
        else:      
            _recipe_list=mongo.db.recipeDB.find()

    #remove duplicates from the lists
    _author_list=[]
    for author in list_of_authors:
        _author_list.append(author["name"])
            
    _country_list=[]
    for country in list_of_countries:
        _country_list.append(country["name"])    
    
    
    _total_results=_recipe_list.count()
  #  print("selected author=",filter_author)
    return render_template("recipe_list.html",title_text=title_text_value,recipes=_recipe_list,selected_country=filter_country, selected_author=filter_author,countries=_country_list,authors=_author_list,action=_todo,filters=_filter_dict, allergens=allergen_list, sort=_sort, total_results=_total_results)


@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    _recipe=mongo.db.recipeDB.find_one({"_id":ObjectId(recipe_id)})
    _added=request.args.get('added_recipe',None)    
    print("added=",_added)
#    categories=["country","author"]
#    for category in categories:
#        if category=="country":
#            database=mongo.db.countriesDB
#        elif category=="author":
#            database=mongo.db.authorDB
#        if _recipe[category]:
#            _categorydoc=database.find_one({"_id":ObjectId(_recipe[category])})
#            print("category doc",_categorydoc)
#            _recipe[category]=_categorydoc["name"]
    title_text='Your recipe'
#    print("checking session variable=",session["filters"])    
    return render_template('display_recipe.html',title_text='Your recipe',recipe=_recipe,added=_added)

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    _recipe=mongo.db.recipeDB.find_one({"_id":ObjectId(recipe_id)})
 #   categories=["country","author"]
 #   for category in categories:
 #       if category=="country":
 #           database=mongo.db.countriesDB
 #       elif category=="author":
 #           database=mongo.db.authorDB
 #       if _recipe[category]:
 #           _categorydoc=database.find_one({"_id":ObjectId(_recipe[category])})
 #           print("category doc",_categorydoc)
 #           _recipe[category]=_categorydoc["name"]    
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
    
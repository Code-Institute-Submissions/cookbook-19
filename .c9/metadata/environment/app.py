{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":463,"column":75},"end":{"row":463,"column":83},"action":"insert","lines":[".lower()"],"id":16030}],[{"start":{"row":465,"column":65},"end":{"row":465,"column":73},"action":"insert","lines":[".lower()"],"id":16031}],[{"start":{"row":462,"column":108},"end":{"row":463,"column":0},"action":"insert","lines":["",""],"id":16032},{"start":{"row":463,"column":0},"end":{"row":463,"column":12},"action":"insert","lines":["            "]},{"start":{"row":463,"column":12},"end":{"row":463,"column":13},"action":"insert","lines":["p"]},{"start":{"row":463,"column":13},"end":{"row":463,"column":14},"action":"insert","lines":["r"]},{"start":{"row":463,"column":14},"end":{"row":463,"column":15},"action":"insert","lines":["i"]},{"start":{"row":463,"column":15},"end":{"row":463,"column":16},"action":"insert","lines":["n"]},{"start":{"row":463,"column":16},"end":{"row":463,"column":17},"action":"insert","lines":["t"]}],[{"start":{"row":463,"column":17},"end":{"row":463,"column":19},"action":"insert","lines":["()"],"id":16033}],[{"start":{"row":463,"column":18},"end":{"row":463,"column":20},"action":"insert","lines":["\"\""],"id":16034}],[{"start":{"row":463,"column":19},"end":{"row":463,"column":20},"action":"insert","lines":["s"],"id":16035},{"start":{"row":463,"column":20},"end":{"row":463,"column":21},"action":"insert","lines":["e"]},{"start":{"row":463,"column":21},"end":{"row":463,"column":22},"action":"insert","lines":["a"]},{"start":{"row":463,"column":22},"end":{"row":463,"column":23},"action":"insert","lines":["r"]},{"start":{"row":463,"column":23},"end":{"row":463,"column":24},"action":"insert","lines":["f"]},{"start":{"row":463,"column":24},"end":{"row":463,"column":25},"action":"insert","lines":["c"]},{"start":{"row":463,"column":25},"end":{"row":463,"column":26},"action":"insert","lines":["h"]}],[{"start":{"row":463,"column":26},"end":{"row":463,"column":27},"action":"insert","lines":[" "],"id":16036}],[{"start":{"row":463,"column":26},"end":{"row":463,"column":27},"action":"remove","lines":[" "],"id":16037},{"start":{"row":463,"column":25},"end":{"row":463,"column":26},"action":"remove","lines":["h"]},{"start":{"row":463,"column":24},"end":{"row":463,"column":25},"action":"remove","lines":["c"]},{"start":{"row":463,"column":23},"end":{"row":463,"column":24},"action":"remove","lines":["f"]}],[{"start":{"row":463,"column":23},"end":{"row":463,"column":24},"action":"insert","lines":["c"],"id":16038},{"start":{"row":463,"column":24},"end":{"row":463,"column":25},"action":"insert","lines":["h"]}],[{"start":{"row":463,"column":25},"end":{"row":463,"column":26},"action":"insert","lines":[" "],"id":16039},{"start":{"row":463,"column":26},"end":{"row":463,"column":27},"action":"insert","lines":["c"]},{"start":{"row":463,"column":27},"end":{"row":463,"column":28},"action":"insert","lines":["o"]},{"start":{"row":463,"column":28},"end":{"row":463,"column":29},"action":"insert","lines":["u"]},{"start":{"row":463,"column":29},"end":{"row":463,"column":30},"action":"insert","lines":["n"]},{"start":{"row":463,"column":30},"end":{"row":463,"column":31},"action":"insert","lines":["t"]},{"start":{"row":463,"column":31},"end":{"row":463,"column":32},"action":"insert","lines":["r"]},{"start":{"row":463,"column":32},"end":{"row":463,"column":33},"action":"insert","lines":["y"]},{"start":{"row":463,"column":33},"end":{"row":463,"column":34},"action":"insert","lines":["-"]}],[{"start":{"row":463,"column":33},"end":{"row":463,"column":34},"action":"remove","lines":["-"],"id":16040}],[{"start":{"row":463,"column":33},"end":{"row":463,"column":34},"action":"insert","lines":["="],"id":16041}],[{"start":{"row":463,"column":35},"end":{"row":463,"column":36},"action":"insert","lines":["."],"id":16042}],[{"start":{"row":463,"column":36},"end":{"row":463,"column":55},"action":"insert","lines":["recipe[key].lower()"],"id":16043}],[{"start":{"row":463,"column":35},"end":{"row":463,"column":36},"action":"remove","lines":["."],"id":16044}],[{"start":{"row":463,"column":35},"end":{"row":463,"column":36},"action":"insert","lines":[","],"id":16045}],[{"start":{"row":464,"column":34},"end":{"row":464,"column":35},"action":"remove","lines":["p"],"id":16046}],[{"start":{"row":464,"column":34},"end":{"row":464,"column":35},"action":"insert","lines":["o"],"id":16047}],[{"start":{"row":462,"column":61},"end":{"row":462,"column":62},"action":"insert","lines":["."],"id":16048},{"start":{"row":462,"column":62},"end":{"row":462,"column":63},"action":"insert","lines":["l"]},{"start":{"row":462,"column":63},"end":{"row":462,"column":64},"action":"insert","lines":["o"]},{"start":{"row":462,"column":64},"end":{"row":462,"column":65},"action":"insert","lines":["w"]},{"start":{"row":462,"column":65},"end":{"row":462,"column":66},"action":"insert","lines":["e"]},{"start":{"row":462,"column":66},"end":{"row":462,"column":67},"action":"insert","lines":["r"]}],[{"start":{"row":462,"column":67},"end":{"row":462,"column":69},"action":"insert","lines":["()"],"id":16049}],[{"start":{"row":461,"column":0},"end":{"row":473,"column":0},"action":"remove","lines":["        if key==\"country\":","            mongo.db.countriesDB.update({\"name\" : recipe[key].lower()},{\"$pull\" : {\"recipe\" : ObjectId(recipe_id)}})","            print(\"search country=\",recipe[key].lower())","            country_doc=mongo.db.countriesDB.find_one({\"name\" : recipe[key].lower()})","            if len(country_doc[\"recipe\"])==0:","                mongo.db.countriesDB.remove({\"name\" : recipe[key].lower()})            ","            #delete country if empty","        if key==\"author\":","            mongo.db.authorDB.update({\"name\" : recipe[key].lower()},{\"$pull\" : {\"recipe\" : ObjectId(recipe_id)}})","            author_doc=mongo.db.authorDB.find_one({\"name\" : recipe[key].lower()})","            if len(author_doc[\"recipe\"])==0:","                mongo.db.authorDB.remove({\"name\" : recipe[key].lower()})",""],"id":16050}],[{"start":{"row":467,"column":106},"end":{"row":468,"column":0},"action":"insert","lines":["",""],"id":16051},{"start":{"row":468,"column":0},"end":{"row":468,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":468,"column":0},"end":{"row":480,"column":0},"action":"insert","lines":["        if key==\"country\":","            mongo.db.countriesDB.update({\"name\" : recipe[key].lower()},{\"$pull\" : {\"recipe\" : ObjectId(recipe_id)}})","            print(\"search country=\",recipe[key].lower())","            country_doc=mongo.db.countriesDB.find_one({\"name\" : recipe[key].lower()})","            if len(country_doc[\"recipe\"])==0:","                mongo.db.countriesDB.remove({\"name\" : recipe[key].lower()})            ","            #delete country if empty","        if key==\"author\":","            mongo.db.authorDB.update({\"name\" : recipe[key].lower()},{\"$pull\" : {\"recipe\" : ObjectId(recipe_id)}})","            author_doc=mongo.db.authorDB.find_one({\"name\" : recipe[key].lower()})","            if len(author_doc[\"recipe\"])==0:","                mongo.db.authorDB.remove({\"name\" : recipe[key].lower()})",""],"id":16052}],[{"start":{"row":479,"column":72},"end":{"row":480,"column":16},"action":"remove","lines":["","                "],"id":16053}],[{"start":{"row":477,"column":81},"end":{"row":478,"column":0},"action":"insert","lines":["",""],"id":16054},{"start":{"row":478,"column":0},"end":{"row":478,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":478,"column":12},"end":{"row":478,"column":124},"action":"insert","lines":["#check if there are any recipes stored against this ingredient. If not delete the ingredient from the collection"],"id":16055}],[{"start":{"row":478,"column":64},"end":{"row":478,"column":74},"action":"remove","lines":["ingredient"],"id":16056},{"start":{"row":478,"column":64},"end":{"row":478,"column":65},"action":"insert","lines":["a"]},{"start":{"row":478,"column":65},"end":{"row":478,"column":66},"action":"insert","lines":["u"]},{"start":{"row":478,"column":66},"end":{"row":478,"column":67},"action":"insert","lines":["t"]},{"start":{"row":478,"column":67},"end":{"row":478,"column":68},"action":"insert","lines":["h"]},{"start":{"row":478,"column":68},"end":{"row":478,"column":69},"action":"insert","lines":["o"]},{"start":{"row":478,"column":69},"end":{"row":478,"column":70},"action":"insert","lines":["r"]}],[{"start":{"row":478,"column":90},"end":{"row":478,"column":100},"action":"remove","lines":["ingredient"],"id":16057},{"start":{"row":478,"column":90},"end":{"row":478,"column":91},"action":"insert","lines":["a"]},{"start":{"row":478,"column":91},"end":{"row":478,"column":92},"action":"insert","lines":["u"]},{"start":{"row":478,"column":92},"end":{"row":478,"column":93},"action":"insert","lines":["t"]},{"start":{"row":478,"column":93},"end":{"row":478,"column":94},"action":"insert","lines":["h"]},{"start":{"row":478,"column":94},"end":{"row":478,"column":95},"action":"insert","lines":["o"]},{"start":{"row":478,"column":95},"end":{"row":478,"column":96},"action":"insert","lines":["r"]}],[{"start":{"row":474,"column":0},"end":{"row":474,"column":36},"action":"remove","lines":["            #delete country if empty"],"id":16058}],[{"start":{"row":473,"column":87},"end":{"row":474,"column":0},"action":"remove","lines":["",""],"id":16059}],[{"start":{"row":470,"column":0},"end":{"row":471,"column":0},"action":"remove","lines":["            print(\"search country=\",recipe[key].lower())",""],"id":16060},{"start":{"row":470,"column":0},"end":{"row":470,"column":112},"action":"insert","lines":["#check if there are any recipes stored against this ingredient. If not delete the ingredient from the collection"]}],[{"start":{"row":470,"column":0},"end":{"row":470,"column":4},"action":"insert","lines":["    "],"id":16061}],[{"start":{"row":470,"column":4},"end":{"row":470,"column":8},"action":"insert","lines":["    "],"id":16062}],[{"start":{"row":470,"column":8},"end":{"row":470,"column":12},"action":"insert","lines":["    "],"id":16063}],[{"start":{"row":470,"column":136},"end":{"row":471,"column":0},"action":"insert","lines":["",""],"id":16064},{"start":{"row":471,"column":0},"end":{"row":471,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":470,"column":93},"end":{"row":470,"column":105},"action":"remove","lines":[" ingredient "],"id":16065},{"start":{"row":470,"column":93},"end":{"row":470,"column":94},"action":"insert","lines":["c"]},{"start":{"row":470,"column":94},"end":{"row":470,"column":95},"action":"insert","lines":["o"]},{"start":{"row":470,"column":95},"end":{"row":470,"column":96},"action":"insert","lines":["u"]},{"start":{"row":470,"column":96},"end":{"row":470,"column":97},"action":"insert","lines":["n"]},{"start":{"row":470,"column":97},"end":{"row":470,"column":98},"action":"insert","lines":["t"]},{"start":{"row":470,"column":98},"end":{"row":470,"column":99},"action":"insert","lines":["r"]},{"start":{"row":470,"column":99},"end":{"row":470,"column":100},"action":"insert","lines":["y"]}],[{"start":{"row":470,"column":100},"end":{"row":470,"column":101},"action":"insert","lines":[" "],"id":16066}],[{"start":{"row":470,"column":93},"end":{"row":470,"column":94},"action":"insert","lines":[" "],"id":16067}],[{"start":{"row":470,"column":64},"end":{"row":470,"column":74},"action":"remove","lines":["ingredient"],"id":16068},{"start":{"row":470,"column":64},"end":{"row":470,"column":65},"action":"insert","lines":["c"]},{"start":{"row":470,"column":65},"end":{"row":470,"column":66},"action":"insert","lines":["o"]},{"start":{"row":470,"column":66},"end":{"row":470,"column":67},"action":"insert","lines":["u"]},{"start":{"row":470,"column":67},"end":{"row":470,"column":68},"action":"insert","lines":["n"]},{"start":{"row":470,"column":68},"end":{"row":470,"column":69},"action":"insert","lines":["t"]},{"start":{"row":470,"column":69},"end":{"row":470,"column":70},"action":"insert","lines":["r"]},{"start":{"row":470,"column":70},"end":{"row":470,"column":71},"action":"insert","lines":["y"]}],[{"start":{"row":491,"column":0},"end":{"row":492,"column":0},"action":"insert","lines":["",""],"id":16069},{"start":{"row":492,"column":0},"end":{"row":493,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":492,"column":0},"end":{"row":492,"column":1},"action":"insert","lines":["d"],"id":16070},{"start":{"row":492,"column":1},"end":{"row":492,"column":2},"action":"insert","lines":["e"]},{"start":{"row":492,"column":2},"end":{"row":492,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":492,"column":3},"end":{"row":492,"column":4},"action":"insert","lines":[" "],"id":16071},{"start":{"row":492,"column":4},"end":{"row":492,"column":5},"action":"insert","lines":["d"]},{"start":{"row":492,"column":5},"end":{"row":492,"column":6},"action":"insert","lines":["e"]},{"start":{"row":492,"column":6},"end":{"row":492,"column":7},"action":"insert","lines":["l"]},{"start":{"row":492,"column":7},"end":{"row":492,"column":8},"action":"insert","lines":["e"]},{"start":{"row":492,"column":8},"end":{"row":492,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":492,"column":9},"end":{"row":492,"column":10},"action":"insert","lines":["e"],"id":16072}],[{"start":{"row":492,"column":9},"end":{"row":492,"column":10},"action":"remove","lines":["e"],"id":16073},{"start":{"row":492,"column":8},"end":{"row":492,"column":9},"action":"remove","lines":["t"]},{"start":{"row":492,"column":7},"end":{"row":492,"column":8},"action":"remove","lines":["e"]},{"start":{"row":492,"column":6},"end":{"row":492,"column":7},"action":"remove","lines":["l"]},{"start":{"row":492,"column":5},"end":{"row":492,"column":6},"action":"remove","lines":["e"]},{"start":{"row":492,"column":4},"end":{"row":492,"column":5},"action":"remove","lines":["d"]}],[{"start":{"row":492,"column":4},"end":{"row":492,"column":5},"action":"insert","lines":["c"],"id":16074},{"start":{"row":492,"column":5},"end":{"row":492,"column":6},"action":"insert","lines":["h"]},{"start":{"row":492,"column":6},"end":{"row":492,"column":7},"action":"insert","lines":["e"]},{"start":{"row":492,"column":7},"end":{"row":492,"column":8},"action":"insert","lines":["c"]},{"start":{"row":492,"column":8},"end":{"row":492,"column":9},"action":"insert","lines":["k"]}],[{"start":{"row":492,"column":8},"end":{"row":492,"column":9},"action":"remove","lines":["k"],"id":16075},{"start":{"row":492,"column":7},"end":{"row":492,"column":8},"action":"remove","lines":["c"]},{"start":{"row":492,"column":6},"end":{"row":492,"column":7},"action":"remove","lines":["e"]},{"start":{"row":492,"column":5},"end":{"row":492,"column":6},"action":"remove","lines":["h"]},{"start":{"row":492,"column":4},"end":{"row":492,"column":5},"action":"remove","lines":["c"]}],[{"start":{"row":492,"column":4},"end":{"row":492,"column":5},"action":"insert","lines":["d"],"id":16076},{"start":{"row":492,"column":5},"end":{"row":492,"column":6},"action":"insert","lines":["e"]},{"start":{"row":492,"column":6},"end":{"row":492,"column":7},"action":"insert","lines":["l"]},{"start":{"row":492,"column":7},"end":{"row":492,"column":8},"action":"insert","lines":["e"]},{"start":{"row":492,"column":8},"end":{"row":492,"column":9},"action":"insert","lines":["t"]},{"start":{"row":492,"column":9},"end":{"row":492,"column":10},"action":"insert","lines":["e"]},{"start":{"row":492,"column":10},"end":{"row":492,"column":11},"action":"insert","lines":["_"]}],[{"start":{"row":492,"column":4},"end":{"row":492,"column":11},"action":"remove","lines":["delete_"],"id":16077}],[{"start":{"row":492,"column":4},"end":{"row":492,"column":5},"action":"insert","lines":["c"],"id":16078},{"start":{"row":492,"column":5},"end":{"row":492,"column":6},"action":"insert","lines":["h"]},{"start":{"row":492,"column":6},"end":{"row":492,"column":7},"action":"insert","lines":["e"]},{"start":{"row":492,"column":7},"end":{"row":492,"column":8},"action":"insert","lines":["c"]},{"start":{"row":492,"column":8},"end":{"row":492,"column":9},"action":"insert","lines":["k"]},{"start":{"row":492,"column":9},"end":{"row":492,"column":10},"action":"insert","lines":["_"]},{"start":{"row":492,"column":10},"end":{"row":492,"column":11},"action":"insert","lines":["a"]},{"start":{"row":492,"column":11},"end":{"row":492,"column":12},"action":"insert","lines":["n"]},{"start":{"row":492,"column":12},"end":{"row":492,"column":13},"action":"insert","lines":["d"]},{"start":{"row":492,"column":13},"end":{"row":492,"column":14},"action":"insert","lines":["_"]},{"start":{"row":492,"column":14},"end":{"row":492,"column":15},"action":"insert","lines":["d"]}],[{"start":{"row":492,"column":15},"end":{"row":492,"column":16},"action":"insert","lines":["e"],"id":16079},{"start":{"row":492,"column":16},"end":{"row":492,"column":17},"action":"insert","lines":["l"]},{"start":{"row":492,"column":17},"end":{"row":492,"column":18},"action":"insert","lines":["e"]},{"start":{"row":492,"column":18},"end":{"row":492,"column":19},"action":"insert","lines":["t"]},{"start":{"row":492,"column":19},"end":{"row":492,"column":20},"action":"insert","lines":["e"]},{"start":{"row":492,"column":20},"end":{"row":492,"column":21},"action":"insert","lines":["_"]},{"start":{"row":492,"column":21},"end":{"row":492,"column":22},"action":"insert","lines":["e"]},{"start":{"row":492,"column":22},"end":{"row":492,"column":23},"action":"insert","lines":["m"]},{"start":{"row":492,"column":23},"end":{"row":492,"column":24},"action":"insert","lines":["p"]},{"start":{"row":492,"column":24},"end":{"row":492,"column":25},"action":"insert","lines":["t"]},{"start":{"row":492,"column":25},"end":{"row":492,"column":26},"action":"insert","lines":["y"]}],[{"start":{"row":492,"column":26},"end":{"row":492,"column":27},"action":"insert","lines":["_"],"id":16080},{"start":{"row":492,"column":27},"end":{"row":492,"column":28},"action":"insert","lines":["d"]},{"start":{"row":492,"column":28},"end":{"row":492,"column":29},"action":"insert","lines":["o"]},{"start":{"row":492,"column":29},"end":{"row":492,"column":30},"action":"insert","lines":["c"]}],[{"start":{"row":492,"column":30},"end":{"row":492,"column":32},"action":"insert","lines":["()"],"id":16081}],[{"start":{"row":492,"column":31},"end":{"row":492,"column":32},"action":"insert","lines":["n"],"id":16082},{"start":{"row":492,"column":32},"end":{"row":492,"column":33},"action":"insert","lines":["a"]},{"start":{"row":492,"column":33},"end":{"row":492,"column":34},"action":"insert","lines":["m"]},{"start":{"row":492,"column":34},"end":{"row":492,"column":35},"action":"insert","lines":["e"]},{"start":{"row":492,"column":35},"end":{"row":492,"column":36},"action":"insert","lines":[","]},{"start":{"row":492,"column":36},"end":{"row":492,"column":37},"action":"insert","lines":["c"]},{"start":{"row":492,"column":37},"end":{"row":492,"column":38},"action":"insert","lines":["a"]},{"start":{"row":492,"column":38},"end":{"row":492,"column":39},"action":"insert","lines":["t"]},{"start":{"row":492,"column":39},"end":{"row":492,"column":40},"action":"insert","lines":["e"]},{"start":{"row":492,"column":40},"end":{"row":492,"column":41},"action":"insert","lines":["g"]}],[{"start":{"row":492,"column":41},"end":{"row":492,"column":42},"action":"insert","lines":["o"],"id":16083},{"start":{"row":492,"column":42},"end":{"row":492,"column":43},"action":"insert","lines":["r"]},{"start":{"row":492,"column":43},"end":{"row":492,"column":44},"action":"insert","lines":["y"]}],[{"start":{"row":492,"column":45},"end":{"row":492,"column":46},"action":"insert","lines":[":"],"id":16084}],[{"start":{"row":492,"column":46},"end":{"row":493,"column":0},"action":"insert","lines":["",""],"id":16085},{"start":{"row":493,"column":0},"end":{"row":493,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":493,"column":0},"end":{"row":496,"column":8},"action":"insert","lines":["                    ingredient_doc=mongo.db.ingredientsDB.find_one({\"name\" : ingredient})","                    if len(ingredient_doc[\"recipe\"])==0:","                        mongo.db.ingredientsDB.remove({\"name\" : ingredient})                      ","        "],"id":16086}],[{"start":{"row":493,"column":0},"end":{"row":493,"column":4},"action":"remove","lines":["    "],"id":16087},{"start":{"row":493,"column":0},"end":{"row":493,"column":4},"action":"remove","lines":["    "]},{"start":{"row":493,"column":0},"end":{"row":493,"column":4},"action":"remove","lines":["    "]},{"start":{"row":493,"column":0},"end":{"row":493,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":494,"column":0},"end":{"row":494,"column":4},"action":"remove","lines":["    "],"id":16088},{"start":{"row":494,"column":0},"end":{"row":494,"column":4},"action":"remove","lines":["    "]},{"start":{"row":494,"column":0},"end":{"row":494,"column":4},"action":"remove","lines":["    "]},{"start":{"row":494,"column":0},"end":{"row":494,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":495,"column":0},"end":{"row":495,"column":4},"action":"remove","lines":["    "],"id":16089},{"start":{"row":495,"column":0},"end":{"row":495,"column":4},"action":"remove","lines":["    "]},{"start":{"row":495,"column":0},"end":{"row":495,"column":4},"action":"remove","lines":["    "]},{"start":{"row":495,"column":0},"end":{"row":495,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":492,"column":44},"end":{"row":492,"column":45},"action":"insert","lines":[","],"id":16090},{"start":{"row":492,"column":45},"end":{"row":492,"column":46},"action":"insert","lines":["d"]},{"start":{"row":492,"column":46},"end":{"row":492,"column":47},"action":"insert","lines":["a"]},{"start":{"row":492,"column":47},"end":{"row":492,"column":48},"action":"insert","lines":["t"]},{"start":{"row":492,"column":48},"end":{"row":492,"column":49},"action":"insert","lines":["a"]},{"start":{"row":492,"column":49},"end":{"row":492,"column":50},"action":"insert","lines":["b"]},{"start":{"row":492,"column":50},"end":{"row":492,"column":51},"action":"insert","lines":["a"]},{"start":{"row":492,"column":51},"end":{"row":492,"column":52},"action":"insert","lines":["s"]},{"start":{"row":492,"column":52},"end":{"row":492,"column":53},"action":"insert","lines":["e"]}],[{"start":{"row":493,"column":4},"end":{"row":493,"column":18},"action":"remove","lines":["ingredient_doc"],"id":16091},{"start":{"row":493,"column":4},"end":{"row":493,"column":5},"action":"insert","lines":["d"]},{"start":{"row":493,"column":5},"end":{"row":493,"column":6},"action":"insert","lines":["o"]},{"start":{"row":493,"column":6},"end":{"row":493,"column":7},"action":"insert","lines":["c"]},{"start":{"row":493,"column":7},"end":{"row":493,"column":8},"action":"insert","lines":["u"]},{"start":{"row":493,"column":8},"end":{"row":493,"column":9},"action":"insert","lines":["m"]},{"start":{"row":493,"column":9},"end":{"row":493,"column":10},"action":"insert","lines":["e"]},{"start":{"row":493,"column":10},"end":{"row":493,"column":11},"action":"insert","lines":["n"]},{"start":{"row":493,"column":11},"end":{"row":493,"column":12},"action":"insert","lines":["t"]}],[{"start":{"row":484,"column":132},"end":{"row":485,"column":0},"action":"insert","lines":["",""],"id":16092},{"start":{"row":485,"column":0},"end":{"row":485,"column":20},"action":"insert","lines":["                    "]},{"start":{"row":485,"column":20},"end":{"row":485,"column":21},"action":"insert","lines":["c"]},{"start":{"row":485,"column":21},"end":{"row":485,"column":22},"action":"insert","lines":["h"]},{"start":{"row":485,"column":22},"end":{"row":485,"column":23},"action":"insert","lines":["e"]},{"start":{"row":485,"column":23},"end":{"row":485,"column":24},"action":"insert","lines":["c"]},{"start":{"row":485,"column":24},"end":{"row":485,"column":25},"action":"insert","lines":["k"]},{"start":{"row":485,"column":25},"end":{"row":485,"column":26},"action":"insert","lines":["_"]}],[{"start":{"row":485,"column":26},"end":{"row":485,"column":27},"action":"insert","lines":["a"],"id":16093},{"start":{"row":485,"column":27},"end":{"row":485,"column":28},"action":"insert","lines":["n"]},{"start":{"row":485,"column":28},"end":{"row":485,"column":29},"action":"insert","lines":["d"]},{"start":{"row":485,"column":29},"end":{"row":485,"column":30},"action":"insert","lines":["_"]},{"start":{"row":485,"column":30},"end":{"row":485,"column":31},"action":"insert","lines":["d"]},{"start":{"row":485,"column":31},"end":{"row":485,"column":32},"action":"insert","lines":["e"]},{"start":{"row":485,"column":32},"end":{"row":485,"column":33},"action":"insert","lines":["l"]},{"start":{"row":485,"column":33},"end":{"row":485,"column":34},"action":"insert","lines":["e"]},{"start":{"row":485,"column":34},"end":{"row":485,"column":35},"action":"insert","lines":["t"]},{"start":{"row":485,"column":35},"end":{"row":485,"column":36},"action":"insert","lines":["e"]},{"start":{"row":485,"column":36},"end":{"row":485,"column":37},"action":"insert","lines":["_"]},{"start":{"row":485,"column":37},"end":{"row":485,"column":38},"action":"insert","lines":["e"]},{"start":{"row":485,"column":38},"end":{"row":485,"column":39},"action":"insert","lines":["m"]},{"start":{"row":485,"column":39},"end":{"row":485,"column":40},"action":"insert","lines":["p"]},{"start":{"row":485,"column":40},"end":{"row":485,"column":41},"action":"insert","lines":["t"]}],[{"start":{"row":485,"column":41},"end":{"row":485,"column":42},"action":"insert","lines":["y"],"id":16094},{"start":{"row":485,"column":42},"end":{"row":485,"column":43},"action":"insert","lines":["_"]},{"start":{"row":485,"column":43},"end":{"row":485,"column":44},"action":"insert","lines":["d"]},{"start":{"row":485,"column":44},"end":{"row":485,"column":45},"action":"insert","lines":["o"]},{"start":{"row":485,"column":45},"end":{"row":485,"column":46},"action":"insert","lines":["c"]}],[{"start":{"row":485,"column":46},"end":{"row":485,"column":48},"action":"insert","lines":["()"],"id":16095}],[{"start":{"row":485,"column":47},"end":{"row":485,"column":48},"action":"insert","lines":["i"],"id":16096},{"start":{"row":485,"column":48},"end":{"row":485,"column":49},"action":"insert","lines":["t"]},{"start":{"row":485,"column":49},"end":{"row":485,"column":50},"action":"insert","lines":["e"]},{"start":{"row":485,"column":50},"end":{"row":485,"column":51},"action":"insert","lines":["m"]}],[{"start":{"row":485,"column":50},"end":{"row":485,"column":51},"action":"remove","lines":["m"],"id":16097},{"start":{"row":485,"column":49},"end":{"row":485,"column":50},"action":"remove","lines":["e"]},{"start":{"row":485,"column":48},"end":{"row":485,"column":49},"action":"remove","lines":["t"]},{"start":{"row":485,"column":47},"end":{"row":485,"column":48},"action":"remove","lines":["i"]}],[{"start":{"row":485,"column":47},"end":{"row":485,"column":48},"action":"insert","lines":["i"],"id":16098},{"start":{"row":485,"column":48},"end":{"row":485,"column":49},"action":"insert","lines":["n"]},{"start":{"row":485,"column":49},"end":{"row":485,"column":50},"action":"insert","lines":["g"]},{"start":{"row":485,"column":50},"end":{"row":485,"column":51},"action":"insert","lines":["e"]},{"start":{"row":485,"column":51},"end":{"row":485,"column":52},"action":"insert","lines":["r"]},{"start":{"row":485,"column":52},"end":{"row":485,"column":53},"action":"insert","lines":["i"]},{"start":{"row":485,"column":53},"end":{"row":485,"column":54},"action":"insert","lines":["d"]},{"start":{"row":485,"column":54},"end":{"row":485,"column":55},"action":"insert","lines":["n"]}],[{"start":{"row":485,"column":54},"end":{"row":485,"column":55},"action":"remove","lines":["n"],"id":16099},{"start":{"row":485,"column":53},"end":{"row":485,"column":54},"action":"remove","lines":["d"]},{"start":{"row":485,"column":52},"end":{"row":485,"column":53},"action":"remove","lines":["i"]},{"start":{"row":485,"column":51},"end":{"row":485,"column":52},"action":"remove","lines":["r"]},{"start":{"row":485,"column":50},"end":{"row":485,"column":51},"action":"remove","lines":["e"]}],[{"start":{"row":485,"column":50},"end":{"row":485,"column":51},"action":"insert","lines":["r"],"id":16100},{"start":{"row":485,"column":51},"end":{"row":485,"column":52},"action":"insert","lines":["e"]},{"start":{"row":485,"column":52},"end":{"row":485,"column":53},"action":"insert","lines":["d"]},{"start":{"row":485,"column":53},"end":{"row":485,"column":54},"action":"insert","lines":["i"]},{"start":{"row":485,"column":54},"end":{"row":485,"column":55},"action":"insert","lines":["e"]},{"start":{"row":485,"column":55},"end":{"row":485,"column":56},"action":"insert","lines":["n"]},{"start":{"row":485,"column":56},"end":{"row":485,"column":57},"action":"insert","lines":["t"]}],[{"start":{"row":485,"column":57},"end":{"row":485,"column":58},"action":"insert","lines":[","],"id":16101}],[{"start":{"row":485,"column":58},"end":{"row":485,"column":80},"action":"insert","lines":["mongo.db.ingredientsDB"],"id":16102}],[{"start":{"row":493,"column":36},"end":{"row":493,"column":44},"action":"remove","lines":["category"],"id":16103}],[{"start":{"row":493,"column":36},"end":{"row":493,"column":37},"action":"insert","lines":["i"],"id":16104},{"start":{"row":493,"column":37},"end":{"row":493,"column":38},"action":"insert","lines":["t"]},{"start":{"row":493,"column":38},"end":{"row":493,"column":39},"action":"insert","lines":["e"]},{"start":{"row":493,"column":39},"end":{"row":493,"column":40},"action":"insert","lines":["m"]}],[{"start":{"row":493,"column":31},"end":{"row":493,"column":36},"action":"remove","lines":["name,"],"id":16105}],[{"start":{"row":494,"column":12},"end":{"row":494,"column":35},"action":"remove","lines":["=mongo.db.ingredientsDB"],"id":16106},{"start":{"row":494,"column":12},"end":{"row":494,"column":13},"action":"insert","lines":["d"]},{"start":{"row":494,"column":13},"end":{"row":494,"column":14},"action":"insert","lines":["a"]},{"start":{"row":494,"column":14},"end":{"row":494,"column":15},"action":"insert","lines":["t"]},{"start":{"row":494,"column":15},"end":{"row":494,"column":16},"action":"insert","lines":["a"]},{"start":{"row":494,"column":16},"end":{"row":494,"column":17},"action":"insert","lines":["b"]},{"start":{"row":494,"column":17},"end":{"row":494,"column":18},"action":"insert","lines":["a"]},{"start":{"row":494,"column":18},"end":{"row":494,"column":19},"action":"insert","lines":["s"]},{"start":{"row":494,"column":19},"end":{"row":494,"column":20},"action":"insert","lines":["e"]}],[{"start":{"row":494,"column":12},"end":{"row":494,"column":13},"action":"insert","lines":["="],"id":16107}],[{"start":{"row":494,"column":41},"end":{"row":494,"column":51},"action":"remove","lines":["ingredient"],"id":16108},{"start":{"row":494,"column":41},"end":{"row":494,"column":42},"action":"insert","lines":["i"]},{"start":{"row":494,"column":42},"end":{"row":494,"column":43},"action":"insert","lines":["t"]},{"start":{"row":494,"column":43},"end":{"row":494,"column":44},"action":"insert","lines":["e"]},{"start":{"row":494,"column":44},"end":{"row":494,"column":45},"action":"insert","lines":["m"]}],[{"start":{"row":495,"column":11},"end":{"row":495,"column":25},"action":"remove","lines":["ingredient_doc"],"id":16109},{"start":{"row":495,"column":11},"end":{"row":495,"column":12},"action":"insert","lines":["d"]},{"start":{"row":495,"column":12},"end":{"row":495,"column":13},"action":"insert","lines":["o"]},{"start":{"row":495,"column":13},"end":{"row":495,"column":14},"action":"insert","lines":["c"]},{"start":{"row":495,"column":14},"end":{"row":495,"column":15},"action":"insert","lines":["u"]},{"start":{"row":495,"column":15},"end":{"row":495,"column":16},"action":"insert","lines":["m"]},{"start":{"row":495,"column":16},"end":{"row":495,"column":17},"action":"insert","lines":["e"]},{"start":{"row":495,"column":17},"end":{"row":495,"column":18},"action":"insert","lines":["n"]},{"start":{"row":495,"column":18},"end":{"row":495,"column":19},"action":"insert","lines":["t"]}],[{"start":{"row":496,"column":8},"end":{"row":496,"column":30},"action":"remove","lines":["mongo.db.ingredientsDB"],"id":16110},{"start":{"row":496,"column":8},"end":{"row":496,"column":9},"action":"insert","lines":["d"]},{"start":{"row":496,"column":9},"end":{"row":496,"column":10},"action":"insert","lines":["a"]},{"start":{"row":496,"column":10},"end":{"row":496,"column":11},"action":"insert","lines":["t"]},{"start":{"row":496,"column":11},"end":{"row":496,"column":12},"action":"insert","lines":["a"]},{"start":{"row":496,"column":12},"end":{"row":496,"column":13},"action":"insert","lines":["b"]},{"start":{"row":496,"column":13},"end":{"row":496,"column":14},"action":"insert","lines":["a"]},{"start":{"row":496,"column":14},"end":{"row":496,"column":15},"action":"insert","lines":["s"]},{"start":{"row":496,"column":15},"end":{"row":496,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":496,"column":34},"end":{"row":496,"column":44},"action":"remove","lines":["ingredient"],"id":16111},{"start":{"row":496,"column":34},"end":{"row":496,"column":35},"action":"insert","lines":["i"]},{"start":{"row":496,"column":35},"end":{"row":496,"column":36},"action":"insert","lines":["t"]},{"start":{"row":496,"column":36},"end":{"row":496,"column":37},"action":"insert","lines":["e"]},{"start":{"row":496,"column":37},"end":{"row":496,"column":38},"action":"insert","lines":["m"]}],[{"start":{"row":486,"column":20},"end":{"row":486,"column":21},"action":"insert","lines":["#"],"id":16112}],[{"start":{"row":487,"column":20},"end":{"row":487,"column":21},"action":"insert","lines":["#"],"id":16113}],[{"start":{"row":488,"column":20},"end":{"row":488,"column":21},"action":"insert","lines":["#"],"id":16114}],[{"start":{"row":477,"column":116},"end":{"row":478,"column":0},"action":"insert","lines":["",""],"id":16115},{"start":{"row":478,"column":0},"end":{"row":478,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":478,"column":0},"end":{"row":478,"column":81},"action":"insert","lines":["                    check_and_delete_empty_doc(ingredient,mongo.db.ingredientsDB)"],"id":16116}],[{"start":{"row":478,"column":16},"end":{"row":478,"column":20},"action":"remove","lines":["    "],"id":16117},{"start":{"row":478,"column":12},"end":{"row":478,"column":16},"action":"remove","lines":["    "]}],[{"start":{"row":479,"column":12},"end":{"row":479,"column":13},"action":"insert","lines":["#"],"id":16118}],[{"start":{"row":480,"column":12},"end":{"row":480,"column":13},"action":"insert","lines":["#"],"id":16119}],[{"start":{"row":478,"column":50},"end":{"row":478,"column":72},"action":"remove","lines":["mongo.db.ingredientsDB"],"id":16120},{"start":{"row":478,"column":50},"end":{"row":478,"column":67},"action":"insert","lines":["mongo.db.authorDB"]}],[{"start":{"row":478,"column":39},"end":{"row":478,"column":49},"action":"remove","lines":["ingredient"],"id":16121},{"start":{"row":478,"column":39},"end":{"row":478,"column":40},"action":"insert","lines":["a"]}],[{"start":{"row":478,"column":39},"end":{"row":478,"column":40},"action":"remove","lines":["a"],"id":16122}],[{"start":{"row":478,"column":39},"end":{"row":478,"column":58},"action":"insert","lines":["recipe[key].lower()"],"id":16123}],[{"start":{"row":470,"column":119},"end":{"row":470,"column":130},"action":"remove","lines":["           "],"id":16124},{"start":{"row":470,"column":119},"end":{"row":471,"column":0},"action":"insert","lines":["",""]},{"start":{"row":471,"column":0},"end":{"row":471,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":471,"column":12},"end":{"row":471,"column":78},"action":"insert","lines":["check_and_delete_empty_doc(recipe[key].lower(),mongo.db.authorDB) "],"id":16125}],[{"start":{"row":472,"column":12},"end":{"row":472,"column":13},"action":"insert","lines":["#"],"id":16126}],[{"start":{"row":473,"column":12},"end":{"row":473,"column":13},"action":"insert","lines":["#"],"id":16127}],[{"start":{"row":474,"column":12},"end":{"row":474,"column":13},"action":"insert","lines":["#"],"id":16128}],[{"start":{"row":471,"column":59},"end":{"row":471,"column":76},"action":"remove","lines":["mongo.db.authorDB"],"id":16129},{"start":{"row":471,"column":59},"end":{"row":471,"column":79},"action":"insert","lines":["mongo.db.countriesDB"]}],[{"start":{"row":492,"column":4},"end":{"row":492,"column":5},"action":"remove","lines":["#"],"id":16130}]]},"ace":{"folds":[{"start":{"row":36,"column":17},"end":{"row":61,"column":147},"placeholder":"..."},{"start":{"row":261,"column":13},"end":{"row":282,"column":105},"placeholder":"..."},{"start":{"row":285,"column":18},"end":{"row":404,"column":304},"placeholder":"..."},{"start":{"row":407,"column":27},"end":{"row":421,"column":102},"placeholder":"..."},{"start":{"row":424,"column":27},"end":{"row":450,"column":169},"placeholder":"..."},{"start":{"row":502,"column":21},"end":{"row":507,"column":34},"placeholder":"..."},{"start":{"row":510,"column":25},"end":{"row":550,"column":141},"placeholder":"..."}],"scrolltop":3632.46875,"scrollleft":0,"selection":{"start":{"row":492,"column":4},"end":{"row":492,"column":4},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":463,"state":"start","mode":"ace/mode/python"}},"timestamp":1564874826799,"hash":"60a6fd79fd14a18e46608625b06ea2bc8a029650"}
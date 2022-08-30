from json import load

with open("countrydata.json", encoding="UTF-8")as f:
    data=load(f)
    # print(len(data))
for c in data:
    print(c.get("name"))
all_country_names=[c.get("name") for c in data]
print(all_country_names)

def get_country_details(name):
    return [ c for c in data if c.get("name")==name][0]

details=get_country_details("India")
print(details)

def get_country_capital(name):
    c_data=get_country_details(name)
    if c_data:
        return c_data.get("capital")

print(get_country_capital("Pakistan"))

def get_country_population(name):
    c_data=get_country_details(name)
    if c_data:
        return c_data.get("population")
print(get_country_population("India"))

def get_country_currencyname(name):

    c_data=get_country_details(name)
    if c_data:
        return c_data.get("currencies")[0].get("name")
print(get_country_currencyname("India"))

def get_country_border_list_names(name):
    c_data=get_country_details(name)
    border_list=c_data.get("borders")
    b_names=[c.get("name") for c in data if c.get("alpha3code") in border_list]
    return b_names
print(get_country_border_list_names("Sri Lanka"))

# max_populated_country=max(data,key=lambda c:c.get("population"))
# print(max_populated_country)

# min_populated_country=min(data,key=lambda c:c.get("population"))
# print(min_populated_country)

def get_maxpopulated_country():
    c_data=max(data,key=lambda c:c.get("population"))
    return c_data.get("name")
print(get_maxpopulated_country())


def get_minpopulated_country():
    c_data=min(data,key=lambda c:c.get("population"))
    return c_data.get("name")
print(get_minpopulated_country())


def get_country_languages(name):
    c_data=get_country_details(name)
    return [l.get("name") for l in c_data.get("languages")]
print(get_country_languages("India"))

# movies.pgm package
# views file
# movies.json
# total number of movies
# unique genres
# movie name released in 2015
# in which year most number of movies released
















import json, random, pprint, random

x = []

CAR_MANUFACTURER = ['Audi','BMW', 'Tesla', 'Zaporojets', 'VAZ', 'Ford']
CARS_MODEL = {
    'Audi':['A8','A7','A6','A5','A4','A3','Q7','Q5','Q3'],
    'BMW':['X1','X2','X3','X5','X6','Series 5','Series 3','Series 1'],
    'Tesla':['MODEL S', 'MODEL 3', 'MODEL X', 'MODEL Y'],
    'Zaporojets':['ALL TIME BEST'],
    'VAZ':['2101', '2102', '2103', '2104', '2105', '2105', 'Chevrolet', 'Kalina', 'Granta'],
    'Ford':['Mustang', 'Focus', 'Mondeo', 'Explorer']}
GEARBOX = ['M','A','R']
COLOR = ['White','Silver','Black','Grey', 'Blue', 'Red', 'Brown', 'Green']

for i in range(len(CAR_MANUFACTURER)):
    manufacturer = {}
    manufacturer['model']='carlist.manufacturer'
    manufacturer['pk'] = i+1
    manufacturer['fields'] = {}
    manufacturer['fields']['manufacturer'] = CAR_MANUFACTURER[i]
    x.append(manufacturer)

for i in range(10):
    productionyear = {}
    productionyear['model']='carlist.productionyear'
    productionyear['pk'] = i+1
    productionyear['fields'] = {}
    productionyear['fields']['year'] = i+2010
    x.append(productionyear)

k=0
temp=[]
for i in CARS_MODEL.values():
    for j in range(len(i)):
        temp.append(i[j])
for model in temp:
    k=k+1
    model_1 = {}
    model_1['model'] = 'carlist.modeltype'
    model_1['pk'] = k
    model_1['fields'] = {}
    model_1['fields']['model_type'] = model
    x.append(model_1)
new_dict = {}
temp=[]
total = 1
for i in CARS_MODEL:
    temp1=[]
    for j in CARS_MODEL[i]:
        temp1.append(total)
        total+=1
    new_dict[i]=temp1

for i in range(1,600):
    car = {}
    car['model']='carlist.car'
    car['pk'] = i
    car['fields'] ={}
    cmanufacturer = random.randint(0,5)
    car['fields']['manufacturer'] = cmanufacturer+1
    car['fields']['models_type'] = random.choice(new_dict[CAR_MANUFACTURER[cmanufacturer]])
    car['fields']['production_year'] = random.randint(1,9)
    car['fields']['gearbox_type'] = random.choice(GEARBOX)
    car['fields']['color'] = random.choice(COLOR)
    x.append(car)

with open('data.json','w') as outfile:
    json.dump(x, outfile)

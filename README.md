# Apologies, WIP, would be completed by EOD - 7/12

``` python

nd = {x: [] for x in fake.profile().keys()}
Faker.seed(5)
for i in range(2):
     for x in fake.profile().keys():
          nd[x].append(fake.profile()[x])
print(nd)

bg = new_dict['blood_group']
max([(nd['blood_group'].count(x),x) for x in (set(nd['blood_group']))])[1]
max([(bg.count(x),x) for x in set(bg)])[1]

sum([x[0] for x in nd['current_location']])/len(nd['current_location'])
sum([x[1] for x in nd['current_location']])/len(nd['current_location'])

[(datetime.date.today()-x).days for x in nd['birthdate']]
sum([(datetime.date.today()-x).days for x in nd['birthdate']])/len(nd['birthdate'])
#------------------------------------------------------------------------
nt = namedtuple('nd',fake.profile().keys())
ndlist=[]
Faker.seed(5)
for i in range(2):
     ndlist.append(nt(**fake.profile()))
ndlist

bg = [x.blood_group for x in ndlist]
max([(bg.count(x),x) for x in set(bg)])[1]

sum([x.current_location[0] for x in ndlist])/len(ndlist)
sum([x.current_location[1] for x in ndlist])/len(ndlist)

[(datetime.date.today()-x.birthdate).days for x in ndlist]
sum([(datetime.date.today()-x.birthdate).days for x in ndlist])/len(ndlist)

```

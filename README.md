# Assignment 9 - Namedtuples
 

## Task1:  250 points (including 5 test cases)
  ### Use the Faker library to get 10000 random profiles. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age, and average age (add proper doc-strings).

- 10000 random profiles were stored in an namedtuple object.
  - ntobj = create_nt_from_fakeprofile(10000)
- The following four functions were written:
    Function            | Function name
    ------------------- | ------------
    largest blood type | **max_bloodgroup_nt(ntobj:namedtuple)**
    mean-current_location | **mean_currentlocation_nt(ntobj:namedtuple)**
    oldest_person_age (in days) | **oldest_age_nt(ntobj:namedtuple)**
    average age (in days) | **mean_age_nt(ntobj:namedtuple)**
- Doc strings were added to namedtuple class which flows downstream and also proper docstrings were written to the functions
- Following 5 test cases were written
  - test1
  - test1
  - test1
  - test1
  - test1
 - Here is the code snippet:
  ``` python
  def create_nt_from_fakeprofile(num_of_records:int):
       '''
       Create a namedtuple object with 'num_of_records' from fake.profile library.
       '''
       from faker import Faker
       fake = Faker()
       from collections import namedtuple
       nt = namedtuple('nt',fake.profile().keys())
       ntobj = nt(*[[] for x in range(len(nt._fields))])
       Faker.seed(5)
       for i in range(num_of_records):
            for x in fake.profile():
                 eval('ntobj.'+x).append(fake.profile()[x])
       return ntobj

  def max_bloodgroup_nt(nt:namedtuple):
       '''
       Return the bloodgroup with maximum count from the namedtuple
       '''
       return max([(ntobj.blood_group.count(x),x) for x in set(ntobj.blood_group)])[1]

  def mean_currentlocation_nt(nt:namedtuple):
       '''
       Return the average of current_location co-ordinates from the namedtuple
       '''
       a=sum([x[0] for x in ntobj.current_location])/len(ntobj.current_location)
       b=sum([x[1] for x in ntobj.current_location])/len(ntobj.current_location)
       return (a,b)

  def oldest_age_nt(nt:namedtuple):
       '''
       Return the oldest age from the namedtuple
       '''
       return max([(datetime.date.today()-x).days for x in ntobj.birthdate])

  def mean_age_nt(nt:namedtuple):
       '''
       Return the mean age from the namedtuple
       '''
       return sum([(datetime.date.today()-x).days for x in ntobj.birthdate])/len(ntobj.birthdate)

  ```

    
## Task 2:  250 points (including 5 test cases)
  ### Do the same thing above using a dictionary. Prove that namedtuple is faster.

- Named tuple object was converted to dictionary.
- The following four functions were written:
    Function            | Function name
    ------------------- | ------------
    largest blood type | **max_bloodgroup_dict(nd:dict)**
    mean-current_location | **mean_currentlocation_dict(nd:dict)**
    oldest_person_age (in days) | **oldest_age_dict(nd:dict)**
    average age (in days) | **mean_age_dict(nd:dict)**
- **The function was timed to compare namedtuples and dictionary and namedtuples were shown to be 1-2% faster.**
  > **Dict Time is 30.332687, Named Tuple Time is 28.117503 , Gain is 1.079%**
  ``` python
  import datetime
  from time import perf_counter

  def f(fn, args):
       fn(args)

  startd = perf_counter()
  for j in (max_bloodgroup_dict,mean_currentlocation_dict,oldest_age_dict,mean_age_dict):
       for i in range(1000):
            f(j,ntobj._asdict())
  endd = perf_counter()
  for j in (max_bloodgroup_nt,mean_currentlocation_nt,oldest_age_nt,mean_age_nt):
       for i in range(1000):
            f(j,ntobj)
  endn = perf_counter()
  print(f' Dict Time is {endd-startd:.6f}, Named Tuple Time is {endn-endd:.6f},
  Gain is {(endd-startd)/(endn-endd):.3f}%')
  ```
- Following 5 test cases were written
  - test1
  - test1
  - test1
  - test1
  - test1

- Here is the code snippet:
  ``` python
  def create_dict_from_fakeprofile(num_of_records:int):
       '''
       Create a dictionary object with 'num_of_records' from fake.profile library.
       '''
       from faker import Faker
       fake = Faker()
       nd = {x:[] for x in fake.profile().keys()}
       Faker.seed(5)
       for i in range(num_of_records):
            for x in fake.profile().keys():
                 nd[x].append(fake.profile()[x])
       return nd

  def max_bloodgroup_dict(nd:dict):
       '''
       Return the bloodgroup with maximum count from the dictionary
       '''
       bg = nd['blood_group']
       return max([(bg.count(x),x) for x in set(bg)])[1]

  def mean_currentlocation_dict(nd:dict):
       '''
       Return the average of current_location co-ordinates from the dictionary
       '''
       a=sum([x[0] for x in nd['current_location']])/len(nd['current_location'])
       b=sum([x[1] for x in nd['current_location']])/len(nd['current_location'])
       return (a,b)

  def oldest_age_dict(nd:dict):
       '''
       Return the oldest age from the dictionary
       '''
       return max([(datetime.date.today()-x).days for x in nd['birthdate']])

  def mean_age_dict(nd:dict):
       '''
       Return the mean age from the dictionary
       '''
       return sum([(datetime.date.today()-x).days for x in nd['birthdate']])/len(nd['birthdate'])
  ```



## Task 3:  500 points (including 10 test cases)
   ### Create fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value the stock market started at, what was the highest value during the day, and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple.

- namedtuple 'stockexchange' was created with the following variables - 'stockexchange(company, symbol, openn, high, close, weight, marketcap, 
trades)'
  ``` python
  from collections import namedtuple
  from faker import Faker
  fake = Faker()

  stockexchange = namedtuple('stockexchange', 'company symbol openn high close weight marketcap trades')

  mc = 5000 #marketcap
  cn = 100 #number of companies

  company = tuple([fake.company() for x in range(cn)])
  symbol = tuple([x for x in range(cn)])

  weightrandom = [random() for x in range(cn)]
  weight = tuple([round(weightrandom[x] / sum(weightrandom),4) for x in range(cn)])
  marketcap = [round(weight[x] * mc,2) for x in range(cn)]

  openn = [marketcap[x] for x in range(cn)]
  high = [marketcap[x] for x in range(cn)]
  close = [marketcap[x] for x in range(cn)]

  trades = [[] for x in range(cn)]

  initial = stockexchange(company, symbol, openn, high, close, weight, marketcap, trades)
  initial
  ```
- doc strings were added to the base class
- 100 companies data was fetched into the 'initial' stockexchange object
- company, weight, symbol were immutable
- initial marketcap was defined at 5000 Billion
- trading price was capped between 90% to 110%
- The following function takes input values for number of days and number of trades and provides the necessary output
  ``` python
  def stock_trades_days(days:int=1, trades:int=1):
      '''
      Takes the number of days and trades and prints output for each day
      with the prebuilt 'initial' stockexchange object.
      '''
      for m in range(days):
          tn = trades # number of trades

          for i in range(len(initial.company)):
              initial.trades[i].clear()

          initial.openn.clear()
          for i in range(len(initial.company)):
              initial.openn.append(initial.close[i])

          for trades in range(tn):
              for i in range(len(initial.company)):
                  initial.trades[i].append(round(randint(80,120)*.01*initial.openn[i],4))

          initial.high.clear()
          for i in range(len(initial.company)):
              initial.high.append(max(initial.trades[i]))

          initial.close.clear()
          for i in range(len(initial.company)):
              initial.close.append(initial.trades[i][-1])

          print(f'\nThe opening marketcap ws {round(sum(initial.openn),2)} Billion
                  \nThe highest marketcap is {round(sum(initial.high),2)} Billion 
                  \nThe closing marketcap is {round(sum(initial.close),2)} Billion 
                  \nTotal Trades : {tn} 
                  \nChange is {((sum(initial.close)-sum(initial.openn))/sum(initial.openn))*100:.2f} %')
  ```
- Following 5 test cases were written
- Following 5 test cases were written
  - test1
  - test1
  - test1
  - test1
  - test1

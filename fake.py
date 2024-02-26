import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

import random
from numpy import random as rd
from faker import Faker
from datetime import datetime, timedelta
from multiprocessing import Pool, cpu_count

from app.data.vars import ccaa_dict, ccaa_list, province_list
from app import models

fake = Faker()
random.seed(17)

def add_project():
    
    fake_p = fake.company()
    p = models.Project.objects.create(name = fake_p)
    
    return p

def return_random_end_date(date):
    
    num = random.randint(a = 10, b = 500)
    random_date = date + timedelta(days = num)
    
    return random_date

def return_random_costs():
    
    est_normal_dist = rd.normal(
        loc = 25000.00,
        scale = 5000.00,
        size = 250
    )
    
    est_cost = round(random.choice(est_normal_dist), 2)
    est_benefit = round(random.choice(est_normal_dist), 2)
    
    normal_dist = rd.normal(
        loc = est_cost,
        scale = 100.00,
        size = 250
    )
    
    cost = round(random.choice(normal_dist), 2)
    benefit = round(random.choice(normal_dist), 2)
    
    return est_cost, est_benefit, cost, benefit

def return_random_num(ceil, kind):
    if kind == "float":
        random_num = random.randint(a = 0, b = ceil) + round(random.random(), 2)
        return random_num
    
    else:
        random_num = random.randint(a = 0, b = ceil)
        return random_num

def add_action(_):
    
    rng1 = random.randint(a = 1, b = 10)
    project = add_project()
    
    for instance in range(rng1):
        
        name = fake.catch_phrase()
        ccaa = random.choice(ccaa_list)
        province = random.choice(ccaa_dict[ccaa])
        ccaa = ccaa
        province = province
        st_date = fake.date_between(
            start_date = datetime.fromisoformat('1997-01-01'),
            end_date = datetime.today())
        est_nd_date = return_random_end_date(st_date)
        nd_date = return_random_end_date(st_date)
        responsible = fake.first_name() + ' ' + fake.last_name()
        est_cost, est_benefit, cost, benefit = return_random_costs()

        a = models.Action.objects.create(
            project = project,
            name = name,
            ccaa = ccaa,
            province = province,
            start_date = st_date,
            est_end_date = est_nd_date,
            end_date = nd_date,
            responsible = responsible,
            est_cost = est_cost,
            est_benefit = est_benefit,
            cost = cost,
            benefit = benefit)

        rng2 = random.randint(a = 1, b = 10)

        for instance in range(rng2):

            action = a
            energy = return_random_num(ceil=500, kind='float')
            ren_energy = return_random_num(ceil=500, kind='float')
            co2 = return_random_num(ceil=100, kind='float')
            no2 = return_random_num(ceil=100, kind='float')
            so2 = return_random_num(ceil=100, kind='float')
            pm = return_random_num(ceil=100, kind='float')
            water = return_random_num(ceil=500, kind='float')
            waste = return_random_num(ceil=300, kind='float')
            hazard = return_random_num(ceil=300, kind='float')
            land = return_random_num(ceil=500, kind='float')
            train_h = return_random_num(ceil=200, kind='float')
            incidents = return_random_num(ceil=100, kind='int')
            expenditures = return_random_num(ceil=100, kind='int')

            i = models.Indicator.objects.create(
                action = action,
                energy = energy,
                ren_energy = ren_energy,
                co2 = co2,
                no2 = no2,
                so2 = so2,
                pm = pm,
                water = water,
                waste = waste,
                hazard = hazard,
                land = land,
                train_h = train_h,
                incidents = incidents,
                expenditures = expenditures,
            )
        
if __name__ == '__main__':
    
    num_cores = cpu_count()
    instances_to_add = int(input("Select number of instances to add: "))
    
    print("Populating database...")
    with(Pool(processes = num_cores)) as pool:
        [_ for _ in pool.imap(add_action, range(instances_to_add))]
    print("Population completed")
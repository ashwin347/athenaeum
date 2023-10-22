import random
import sys
import os
sys.path.append(os.path.realpath('..'))
from datetime import datetime, timedelta
from config.database_config import SessionLocal
from models import Resource


session = SessionLocal()

num_records = 100
def random_date(start, end):
    time_between_dates = end - start
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start + timedelta(days=random_number_of_days)
    return random_date
# Generate and insert random data
types=["pdf","img","article_link"]
domains = ["ui/ux","datascience","fullstack"]
current_date = datetime.now()

# Calculate the date before 100 days
date_before_100_days = current_date - timedelta(days=100)

for i in range(2,num_records):
    resource = Resource(
        resource_id = i, 
        resource_title= f"test_subtitle_{i}",
        resource_subtitle = f"test_subtitle_{i}",
        resource_link = "www.google.com",
        resource_type = random.choice(types) ,
        resource_domain = random.choice(domains),
        resource_img_path = "/static/img/test.jpg",
        is_active = True,
        creation_date = random_date(date_before_100_days, current_date)
    )
    session.add(resource)
session.commit()

print(f"Successfully inserted {num_records} random records.")
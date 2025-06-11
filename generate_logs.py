import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Create a directory if not exists
os.makedirs("data", exist_ok=True)

users = ['alice', 'bob', 'charlie', 'david', 'eve']
actions = ['login', 'logout', 'file_access', 'email_sent', 'usb_inserted', 'db_query']
departments = ['HR', 'Finance', 'Engineering', 'Legal']

def random_datetime(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

start_date = datetime(2025, 6, 1)
end_date = datetime(2025, 6, 9)

logs = []

for _ in range(1000):
    user = random.choice(users)
    action = random.choice(actions)
    time = random_datetime(start_date, end_date)
    file_accessed = f"file_{random.randint(1,20)}.pdf" if action == 'file_access' else ''
    dept = random.choice(departments)
    logs.append([user, action, time, file_accessed, dept])

df = pd.DataFrame(logs, columns=['user', 'action', 'timestamp', 'file', 'department'])
df.to_csv('data/user_logs.csv', index=False)

print("✅ Sample behavior logs generated at data/user_logs.csv")

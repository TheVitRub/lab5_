from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task11 import User, Jobs, Department


engine = create_engine('sqlite:///mars_explorer.db')
Session = sessionmaker(bind=engine)
session = Session()

query_result = session.query(User).join(Jobs, User.id == Jobs.team_leader). \
    join(Department, User.id == Department.chief). \
    filter(Jobs.work_size > 10).all()

for user in query_result:
    print(f"{user.surname} {user.name}: {user.position}")

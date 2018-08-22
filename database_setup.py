from app import db, User

db.drop_all()
db.create_all()

admin = User(username='admin', password='admin')
db.session.add(admin)
db.session.commit()

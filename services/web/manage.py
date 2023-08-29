# configure cli to run and manage the app
# created a new flask group instance to extend the normal cli
from flask.cli import FlaskGroup
from project import app,db,User

cli = FlaskGroup(app)

# register the create_db command to cli
@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
# add user
@cli.command("seed_db")
def seed_db():
    db.session.add(User(email="shrikanth@kanth.org"))
    db.session.commit()


if __name__ == "__main__":
    cli()

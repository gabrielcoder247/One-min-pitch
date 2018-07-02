from flask_script import Manager,Server
from app import create_app,db
from app.models import User,Role
from flask_migrate import Migrate, MigrateCommand

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

<<<<<<< HEAD
# migrate = Migrate(app,db)
# manager.add_command('db',MigrateCommand)

@manager.shell
 
=======
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell

>>>>>>> e093d9df398ee9518dc278a60a359257df126007
def make_shell_context():
    return dict(app = app,db = db,User = User)


if __name__ == '__main__':
    manager.run()

    
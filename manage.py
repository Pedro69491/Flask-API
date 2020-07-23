# file to run database migrations and upgrades
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_app import db, app

# creating a Manager instance,
# Manager class keeps track of all commands and handles how tey are called in the command line
manager = Manager(app)
migrate = Migrate(app, db)

# db will run on the terminal with several subcommands
manager.add_command('db', MigrateCommand) 

if __name__ == '__main__':  
    manager.run()
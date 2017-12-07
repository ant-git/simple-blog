import os
import sys
from flask.ext.script import Manager, Server
from __init__ import app

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

manager = Manager(app)
manager.add_command("runserver", Server(
    use_debugger=True,
    host=os.getenv('IP', 'localhost'),
    port=int(os.getenv('PORT', 5000))
))


if __name__ == "__main__":
    manager.run()

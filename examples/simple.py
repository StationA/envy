"""
An example of a simple configuration that can be controlled through the environment.

To try this out, run:

    python simple.py

And then compare to:

    APP_NAME=my-app APP_PORT=80 python simple.py

"""
from envy import Env


class AppEnv(Env):
    name = 'app-name'
    port = 8080


if __name__ == '__main__':
    ENV = AppEnv('APP')
    print(ENV.name)
    print(type(ENV.port))
    print(ENV.port)

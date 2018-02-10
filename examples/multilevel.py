"""
An example of a multi-level configuration that can be controlled through the environment.

To try this out, run:

    python multilevel.py

And then compare to:

    APP_DATABASE_CONNECTION_TIMEOUT=60 python multilevel.py

"""
from envy import Env


class DBEnv(Env):
    connection_string = 'postgresql://un:pw@host:port/db'
    connection_timeout = 10


class AppEnv(Env):
    database = DBEnv


if __name__ == '__main__':
    ENV = AppEnv('APP')
    print(ENV.database.connection_string)
    print(ENV.database.connection_timeout)

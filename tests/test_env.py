from envy import Env


class SingleLevelEnv(Env):
    a = 'HELLO'
    b = 123
    c = False


def test_single_level_env_defaults():
    env = SingleLevelEnv('TEST', env={})
    assert env.a == SingleLevelEnv.a
    assert env.b == SingleLevelEnv.b
    assert env.c == SingleLevelEnv.c


def test_single_level_env_overrides():
    new_a = 'GOODBYE'
    new_b = '321'
    new_c = 'True'
    env = SingleLevelEnv('TEST', env={
        'TEST_A': new_a,
        'TEST_B': new_b,
        'TEST_C': new_c,
    })
    assert env.a == new_a
    assert env.b == int(new_b)
    assert env.c == bool(new_c)


class DBEnv(Env):
    connection_string = 'postgres://un:pw@host:port/db'
    connection_timeout = 30


class AppEnv(Env):
    name = 'my-app'
    database = DBEnv


def test_multi_level_env_defaults():
    env = AppEnv('App', env={})
    assert env.name == AppEnv.name
    assert isinstance(env.database, DBEnv)
    assert env.database.connection_string == DBEnv.connection_string
    assert env.database.connection_timeout == DBEnv.connection_timeout


def test_multi_level_env_overrides():
    new_name = 'db-service'
    new_connection_string = 'mysql://un:pw@host:port/db'
    new_connection_timeout = '45'
    env = AppEnv('APP', env={
        'APP_NAME': new_name,
        'APP_DATABASE_CONNECTION_STRING': new_connection_string,
        'APP_DATABASE_CONNECTION_TIMEOUT': new_connection_timeout
    })
    assert env.name == new_name
    assert isinstance(env.database, DBEnv)
    assert env.database.connection_string == new_connection_string
    assert env.database.connection_timeout == int(new_connection_timeout)

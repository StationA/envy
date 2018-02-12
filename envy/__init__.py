import os


__version__ = '0.1.0'
DELIMITER = '_'


def _filter_and_remove_prefix(env, envvar_prefix):
    new_env = {}
    for key, val in env.items():
        if key.startswith(envvar_prefix):
            new_key = key[len(envvar_prefix + DELIMITER):]
            new_env[new_key] = val
    return new_env


class Env(object):
    """
    Base environment class that automates loading nested environment variables into
    environment objects
    """
    def __init__(self, envvar_prefix, env=None):
        env = env if env is not None else os.environ
        self._env = _filter_and_remove_prefix(env, envvar_prefix)
        self._load_from_env()

    def _load_from_env(self):
        for attr, value_spec in self.__class__.__dict__.items():
            if attr.startswith('_'):
                # Skip any private attributes
                continue

            envvar = attr.upper()
            value = None
            if isinstance(value_spec, type) and issubclass(value_spec, Env):
                value = value_spec(envvar, self._env)
            elif isinstance(value_spec, list):
                value_type = type(value_spec[0])
                idx = 0
                new_values = []
                while True:
                    listvar = envvar + DELIMITER + str(idx)
                    if listvar in self._env:
                        new_values.append(value_type(self._env[listvar]))
                        idx += 1
                    else:
                        break
                if new_values:
                    value = new_values
                else:
                    value = value_spec
            else:
                value_type = type(value_spec)
                if envvar in self._env:
                    value = value_type(self._env[envvar])
                else:
                    # TODO: Should this require a more granular way to control default values or
                    # requirements?
                    value = value_spec
            setattr(self, attr, value)

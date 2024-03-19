"""
Python decorator that will wrap the function call in snowkeet_new
and output the current DB and SCHEMA values if there is an error, then raise the error.
"""

from functools import wraps

from rich.traceback import install

install()


def sf_schema_checker(func):  # noqa
    @wraps(func)
    def wrapper(self, *args, **kwargs):  # noqa
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            default_msg = str(e)
            msg = f"{default_msg}\n\n-- ERROR CONTEXT --\n"
            f"Function: {self.__class__.__name__}.{func.__name__}"
            f"\nDatabase: {self.database}\nSchema: {self.schema}"
            raise type(e)(msg).with_traceback(e.__traceback__) from e

    return wrapper

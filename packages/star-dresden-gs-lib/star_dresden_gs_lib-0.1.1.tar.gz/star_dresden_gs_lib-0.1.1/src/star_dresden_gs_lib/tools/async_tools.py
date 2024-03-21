import asyncio


def run_async(callback):
    def inner(func):
        def wrapper(*args, **kwargs):
            def __exec():
                out = func(*args, **kwargs)
                callback(out)
                return out

            return asyncio.get_event_loop().run_in_executor(None, __exec)

        return wrapper

    return inner

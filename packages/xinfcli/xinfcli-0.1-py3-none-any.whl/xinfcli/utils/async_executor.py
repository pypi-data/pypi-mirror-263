from asyncio import AbstractEventLoop, get_event_loop
from typing import Callable


class AsyncExecutor:
    __loop: AbstractEventLoop

    def __init__(self):
        self.__loop = get_event_loop()

    async def execute(self, fn: Callable, *args, **kwargs):
        return await self.__loop.run_in_executor(None, fn, *args, **kwargs)

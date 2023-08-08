import atexit
import runpy

import exception_handling

exception_handling.hook_exception_handlers()
atexit.register(exception_handling.unhook_exception_handlers)

runpy.run_module("main", run_name="__main__")

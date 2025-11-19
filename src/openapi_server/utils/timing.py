"""
Timing decorator for async functions to measure execution time.
"""
import asyncio
import functools
import time
from typing import Callable, TypeVar, ParamSpec

P = ParamSpec('P')
R = TypeVar('R')


def measure_time(func_name: str = None, log_func: Callable = print):
    """
    Decorator to measure execution time of async functions.
    
    Args:
        func_name: Optional custom name for logging. If not provided, uses function name.
        log_func: Function to use for logging (default: print). Can be logging.info, etc.
    
    Example:
        @measure_time()
        async def my_async_function():
            await some_operation()
        
        @measure_time("Custom Operation")
        async def another_function():
            await another_operation()
    """
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        name = func_name or func.__name__
        
        if asyncio.iscoroutinefunction(func):
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                start_time = time.perf_counter()
                try:
                    result = await func(*args, **kwargs)
                    elapsed_time = time.perf_counter() - start_time
                    log_func(f"[{name}] Execution time: {elapsed_time:.4f} seconds ({elapsed_time*1000:.2f} ms)")
                    return result
                except Exception as e:
                    elapsed_time = time.perf_counter() - start_time
                    log_func(f"[{name}] Failed after {elapsed_time:.4f} seconds ({elapsed_time*1000:.2f} ms): {e}")
                    raise
            return async_wrapper
        else:
            # Support for sync functions too
            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                start_time = time.perf_counter()
                try:
                    result = func(*args, **kwargs)
                    elapsed_time = time.perf_counter() - start_time
                    log_func(f"[{name}] Execution time: {elapsed_time:.4f} seconds ({elapsed_time*1000:.2f} ms)")
                    return result
                except Exception as e:
                    elapsed_time = time.perf_counter() - start_time
                    log_func(f"[{name}] Failed after {elapsed_time:.4f} seconds ({elapsed_time*1000:.2f} ms): {e}")
                    raise
            return sync_wrapper
    
    return decorator


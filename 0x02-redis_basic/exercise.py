#!/usr/bin/env python3
""" Redis Basics"""

import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional


class Cache:
    """Cache implementation"""
    def __init__(self) -> None:
        """Initialize redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate random key"""
        key = str(uuid.uuid4())
        self._redis.set(name=key, value=data)
        return key

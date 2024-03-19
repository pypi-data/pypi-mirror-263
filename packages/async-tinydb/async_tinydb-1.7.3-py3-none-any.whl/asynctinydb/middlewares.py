"""
Contains the :class:`base class <asynctinydb.middlewares.Middleware>` for
middlewares and implementations.
"""

from __future__ import annotations
from typing import TypeVar, Type, Generic
from .storages import Storage

S = TypeVar('S', bound=Storage, covariant=True)


class Middleware(Generic[S]):
    """
    The base class for all Middlewares.

    Middlewares hook into the read/write process of TinyDB allowing you to
    extend the behaviour by adding caching, logging, ...

    Your middleware's ``__init__`` method has to call the parent class
    constructor so the middleware chain can be configured properly.
    """

    def __init__(self, storage_cls: Type[S]):
        self._storage_cls = storage_cls
        self.storage: Storage = None  # type: ignore

    @property
    def on(self):
        return self.storage.on

    @property
    def event_hook(self):
        return self.storage.event_hook

    def __call__(self, *args, **kwargs):
        """
        Create the storage instance and store it as self.storage.

        Usually a user creates a new TinyDB instance like this::

            TinyDB(storage=StorageClass)

        The storage keyword argument is used by TinyDB this way::

            self.storage = storage(*args, **kwargs)

        As we can see, ``storage(...)`` runs the constructor and returns the
        new storage instance.


        Using Middlewares, the user will call::

                                       The "real" storage class
                                       v
            TinyDB(storage=Middleware(StorageClass))
                       ^
                       Already an instance!

        So, when running ``self.storage = storage(*args, **kwargs)`` Python
        now will call ``__call__`` and TinyDB will expect the return value to
        be the storage (or Middleware) instance. Returning the instance is
        simple, but we also got the underlying (*real*) StorageClass as an
        __init__ argument that still is not an instance.
        So, we initialize it in __call__ forwarding any arguments we receive
        from TinyDB (``TinyDB(arg1, kwarg1=value, storage=...)``).

        In case of nested Middlewares, calling the instance as if it was a
        class results in calling ``__call__`` what initializes the next
        nested Middleware that itself will initialize the next Middleware and
        so on.
        """

        self.storage = self._storage_cls(*args, **kwargs)

        return self

    def __getattr__(self, name):
        """
        Forward all unknown attribute calls to the underlying storage, so we
        remain as transparent as possible.
        """

        return getattr(self.__dict__["storage"], name)


class CachingMiddleware(Middleware[S]):
    """
    Add some caching to TinyDB.

    This Middleware aims to improve the performance of TinyDB by writing only
    the last DB state every :attr:`WRITE_CACHE_SIZE` time and reading always
    from cache.
    """

    def __init__(self, storage_cls: Type[S], cache_size=1000):
        # Initialize the parent constructor
        super().__init__(storage_cls)

        # Prepare the cache
        self.cache = None
        self.cache_size = cache_size
        self._cache_modified_count = 0

    @property
    def WRITE_CACHE_SIZE(self):
        """
        Legacy property for backwards compatibility.
        """
        return self.cache_size

    @WRITE_CACHE_SIZE.setter
    def WRITE_CACHE_SIZE(self, value):
        self.cache_size = value

    async def read(self):
        if self.storage.closed:
            raise IOError('Storage is closed')

        if self.cache is None:
            # Empty cache: read from the storage
            self.cache = await self.storage.read()

        # Return the cached data
        return self.cache

    async def write(self, data):
        if self.storage.closed:
            raise IOError('Storage is closed')
        # Store data in cache
        self.cache = data
        self._cache_modified_count += 1

        # Check if we need to flush the cache
        if self._cache_modified_count >= self.cache_size:
            await self.flush()

    async def flush(self):
        """
        Flush all unwritten data to disk.
        """
        if self._cache_modified_count:
            # Force-flush the cache by writing the data to the storage
            await self.storage.write(self.cache)
            self._cache_modified_count = 0

    async def close(self):
        if self.storage.closed and self._cache_modified_count:
            raise IOError("Storage is closed before flushing the cache")

        # Flush potentially unwritten data
        await self.flush()

        # Let the storage clean up too
        await self.storage.close()

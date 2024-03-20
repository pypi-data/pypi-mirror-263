import asyncio

import redis
import redis.asyncio as aioredis
from typing import Dict, Tuple, List


class RedisWrapper(object):
    _pool_dict: Dict[Tuple[str, int, int, str, str], redis.ConnectionPool] = {}

    def __init__(
            self,
            host,
            port,
            db,
            username,
            password,
            decode_responses,
            max_connections,
            health_check_interval,
            retry_on_timeout
    ) -> None:
        pool_key = (host, port, db, username, password)
        if pool_key not in self._pool_dict:
            self._pool_dict[pool_key] = redis.ConnectionPool(
                host=host,
                port=port,
                db=db,
                username=username,
                password=password,
                decode_responses=decode_responses,
                max_connections=max_connections,
                health_check_interval=health_check_interval,
                retry_on_timeout=retry_on_timeout
            )
        self._r = redis.Redis(connection_pool=self._pool_dict[pool_key])
        self._ping()

    def get_redis(self) -> redis.Redis:
        return self._r

    def _ping(self):
        try:
            self._r.ping()
        except BaseException as e:
            # log

            #
            raise e

    def close(self) -> None:
        self._r.close()
    @staticmethod
    def new_redis_pool_connection(
            host,
            port,
            db,
            username,
            password,
            decode_responses,
            max_connections,
            health_check_interval,
            retry_on_timeout
    ):
        return RedisWrapper(host=host,
                            port=port,
                            db=db,
                            username=username,
                            password=password,
                            decode_responses=decode_responses,
                            max_connections=max_connections,
                            health_check_interval=health_check_interval,
                            retry_on_timeout=retry_on_timeout)


class AioRedisWrapper(object):
    _pool_dict: Dict[Tuple[str, int, int, str, str], redis.ConnectionPool] = {}

    def __init__(
            self,
            host,
            port,
            db,
            username,
            password,
            decode_responses,
            max_connections,
            health_check_interval,
            retry_on_timeout
    ) -> None:
        pool_key = (host, port, db, username, password)
        if pool_key not in self._pool_dict:
            self._pool_dict[pool_key] = aioredis.ConnectionPool(
                host=host,
                port=port,
                db=db,
                username=username,
                password=password,
                decode_responses=decode_responses,
                max_connections=max_connections,
                health_check_interval=health_check_interval,
                retry_on_timeout=retry_on_timeout
            )
        self._r = aioredis.Redis(connection_pool=self._pool_dict[pool_key])
        #asyncio.create_task(self._ping_async())

    def get_redis(self) -> aioredis.Redis:
        return self._r

    async def _ping_async(self):
        try:
            await self._r.ping()
        except Exception as e:
            # log
            #
            raise e

    async def close(self):
        await self._r.close()

    @staticmethod
    def new_redis_pool_connection(
            host,
            port,
            db,
            username,
            password,
            decode_responses,
            max_connections,
            health_check_interval,
            retry_on_timeout
    ):
        return AioRedisWrapper(host=host,
                                     port=port,
                                     db=db,
                                     username=username,
                                     password=password,
                                     decode_responses=decode_responses,
                                     max_connections=max_connections,
                                     health_check_interval=health_check_interval,
                                     retry_on_timeout=retry_on_timeout)

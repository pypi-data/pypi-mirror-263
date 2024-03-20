import redis

from model_infer_utils.infer_task_mgr import InferTaskBaseMgr, ParamConfig, AsyncioInferTaskBaseMgr
from model_infer_utils.redis_warper import RedisWrapper, AioRedisWrapper
from model_infer_utils.task_proto import TaskProto, RedisTaskProto, TaskResultProto


class RedisParamConfig(ParamConfig):

    def __init__(self, host='localhost', port=6379, username='default', password='', db=0,
                 queue_key_name="", health_check_interval=0, max_connections=None,
                 retry_on_timeout=True, decode_responses=True) -> None:
        """
            Args:
                host: redis连接url
                port: redis连接端口
                username: redis连接用户名
                password: redis连接密码
                queue_key_name: 提取待使用任务的key名称
                health_check_interval: 健康检查间隔，发送命令前判断如大于间隔时间则pingpong一次，超时自捕异常重连，如成功执行命令，不成功异常向外传递。默认为0，不做检查。建议开启retry_on_timeout，不使用检查
                max_connections: 默认None,不设置时max_connections为2 ** 31，如设置有限数值，获取池中con对象超过最大连接数时会抛异常，不建议设置
                retry_on_timeout: 在设置命令实现函数中execute_command，抛出超时会有一次因超时而重试conn.send_command的机会，虽然因网络问题很可能也失败，但也值得一次重试
                decode_responses: redis 取出的结果默认是字节，decode_responses=True 改成字符串
            Return:
                None
        """
        # connect config
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.db = db
        self.health_check_interval = health_check_interval
        self.max_connections = max_connections
        self.retry_on_timeout = retry_on_timeout
        self.decode_responses = decode_responses
        # task config
        self.queue_key_name = queue_key_name


class RedisInferTaskMgr(InferTaskBaseMgr):
    """
            推理任务获取和结果上传的封装基类
    """

    def __init__(self, param: RedisParamConfig) -> None:
        self.redis_wrapper = RedisWrapper.new_redis_pool_connection(
            host=param.host,
            port=param.port,
            db=param.db,
            username=param.username,
            password=param.password,
            decode_responses=param.decode_responses,
            max_connections=param.max_connections,
            health_check_interval=param.health_check_interval,
            retry_on_timeout=param.retry_on_timeout
        )
        self.param = param

    @property
    def redis(self):
        return self.redis_wrapper.get_redis()

    @staticmethod
    def from_redis_config_param(dict_param: dict) -> object:
        try:
            config = RedisParamConfig(
                host=dict_param["host"], port=dict_param["port"], db=dict_param["db"], username=dict_param["username"],
                password=dict_param["password"],
                queue_key_name=dict_param["QueuePackStreaming"]
            )
            return RedisInferTaskMgr(config)
        except Exception as ex:
            print("except:" + str(ex))
        return None

    def get_task(self) -> (bool, TaskProto, str):
        """
            同步方法
            Return:
                bool: 成功返回true，和TaskProto解析后对象，失败返回false和为未解析TaskProto对象
                TaskProto:成功返回任务Task Proto object，失败返回None
                str: 失败时返回错误信息，成功则为空字符串
        """
        try:
            task_val = self.redis.lpop(self.param.queue_key_name)
        except redis.exceptions.ConnectionError as ex:
            # alarm

            #
            return False, None, str(ex)
        except redis.exceptions.TimeoutError as ex:
            # alarm
            #
            return False, None, str(ex)
        except Exception as ex:
            # alarm
            #
            return False, None, str(ex)

        if task_val is None:
            return False, None, "not found job"
        # parse task
        try:
            redis_task_obj = RedisTaskProto()
            redis_task_obj.parse_task(task_val)
        except Exception as ex:
            return False, None, str(ex)

        return True, redis_task_obj, ""

    def add_task(self, stream_result: TaskResultProto) -> None:
        """
            Args:
                stream_result: 流式结果包装
            Return:
                None
        """
        try:
            flag = self.redis.zadd(stream_result.model_key, {stream_result.to_json(): stream_result.order})
            if stream_result.order == 0:
                self.redis.expire(stream_result.model_key, 600)
        except Exception as ex:
            # log error

            #
            pass

    def ping(self):
        try:
            self.redis.ping()
        except BaseException as e:
            # log

            #
            raise e

    def close(self):
        self.redis_wrapper.close()

    def __del__(self):
        self.close()


class AsyncRedisInferTaskMgr(AsyncioInferTaskBaseMgr):
    """
            推理任务获取和结果上传的封装基类,异步版本
    """

    def __init__(self, param: RedisParamConfig) -> None:
        self.redis_wrapper = AioRedisWrapper.new_redis_pool_connection(
            host=param.host,
            port=param.port,
            db=param.db,
            username=param.username,
            password=param.password,
            decode_responses=param.decode_responses,
            max_connections=param.max_connections,
            health_check_interval=param.health_check_interval,
            retry_on_timeout=param.retry_on_timeout
        )
        self.param = param

    @property
    def redis(self):
        return self.redis_wrapper.get_redis()

    async def close(self):
        self.redis_wrapper.aclose()

    async def ping(self):
        try:
            await self.redis.ping()
        except BaseException as e:
            # log

            #
            raise e

    @staticmethod
    def from_redis_config_param(dict_param: dict) -> object:
        try:
            config = RedisParamConfig(
                host=dict_param["host"], port=dict_param["port"], db=dict_param["db"], username=dict_param["username"],
                password=dict_param["password"],
                queue_key_name=dict_param["QueuePackStreaming"]
            )
            return AsyncRedisInferTaskMgr(config)
        except Exception as ex:
            print("except:" + str(ex))
        return None

    async def get_task(self, timeout: int = 1) -> (bool, TaskProto, str):
        """
            异步方法
            Args:
                timeout:设置超时时间，单位秒,当为0时阻塞直到有结果.
            Return:
                bool: 成功返回true，和TaskProto解析后对象，失败返回false和为未解析TaskProto对象
                TaskProto:成功返回任务Task Proto object，失败返回None
                str: 失败时返回错误信息，成功则为空字符串
        """
        try:
            task_tuple = await self.redis.blpop(self.param.queue_key_name, timeout=timeout)
        except redis.exceptions.ConnectionError as ex:
            # alarm

            #
            return False, None, str(ex)
        except redis.exceptions.TimeoutError as ex:
            # alarm
            #
            return False, None, str(ex)
        except Exception as ex:
            # alarm
            #
            return False, None, str(ex)

        if task_tuple is None:
            return False, None, "not found job"
        # parse task
        try:
            redis_task_obj = RedisTaskProto()
            redis_task_obj.parse_task(task_tuple[1])
        except Exception as ex:
            return False, None, str(ex)

        return True, redis_task_obj, ""

    async def add_task(self, stream_result: TaskResultProto) -> None:
        """
            Args:
                stream_result: 流式结果包装
            Return:
                None
        """
        try:
            flag = await self.redis.zadd(stream_result.model_key, {stream_result.to_json(): stream_result.order})
            if stream_result.order == 0:
                await self.redis.expire(stream_result.model_key, 600)
        except Exception as ex:
            # log error

            #
            pass
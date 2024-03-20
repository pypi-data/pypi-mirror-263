from model_infer_utils.task_proto import TaskProto, TaskResultProto


class ParamConfig(object):
    def __init__(self):
        pass


class InferTaskBaseMgr(object):
    """
        推理任务获取和结果上传的封装基类
    """
    def __init__(self, param: ParamConfig) -> None:
        pass

    def get_task(self) -> (bool, TaskProto, str):
        """
            同步方法
            Return:
                bool: 成功返回true，和TaskProto解析后对象，失败返回false和为未解析TaskProto对象
                TaskProto:返回任务Task Proto object
                str: 失败时返回错误信息，成功则为空字符串
        """
        return False, None, ""

    def add_task(self, stream_result: TaskResultProto) -> None:
        """
            Args:
                stream_result: 流式结果包装
            Return:
                None
        """
        pass

    def ping(self):
        pass

    def close(self):
        pass


class AsyncioInferTaskBaseMgr(object):
    """
        推理任务获取和结果上传的封装基类
    """

    def __init__(self, param: ParamConfig) -> None:
        pass

    async def get_task(self, timeout: int = 1) -> (bool, TaskProto, str):
        """
            异步方法
            Return:
                bool: 成功返回true，和TaskProto解析后对象，失败返回false和为未解析TaskProto对象
                TaskProto:返回任务Task Proto object
                str: 失败时返回错误信息，成功则为空字符串
        """
        return False, None, ""

    async def add_task(self, stream_result: TaskResultProto) -> None:
        """
            异步方法
            Args:
                stream_result: 流式结果包装
            Return:
                None
        """
        pass

    async def ping(self):
        pass

    async def close(self):
        pass

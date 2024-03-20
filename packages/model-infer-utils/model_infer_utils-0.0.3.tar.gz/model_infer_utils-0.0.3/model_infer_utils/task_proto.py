import json
from typing import Any

class ModelParam(object):
    def __init__(self):
        self.generate_length = 1024
        self.top_p = 1.0
        self.top_k = 3.0
        self.repetition_penalty = 1.05
        self.length_penalty = 1.0
        self.frequency_penalty = 0.0
        self.no_repeat_ngram_size = 5
        self.min_len = 2
        self.temperature = 0.66
        self.end_words = []
        self.bad_words = []

    def parse(self, dict):
        self.generate_length = dict["generate_length"]
        self.top_p = dict["top_p"]
        self.top_k = dict["top_k"]
        self.repetition_penalty = dict["repetition_penalty"]
        self.length_penalty = dict["length_penalty"]
        self.frequency_penalty = dict["frequency_penalty"]
        self.no_repeat_ngram_size = dict["no_repeat_ngram_size"]
        self.min_len = dict["min_len"]
        self.temperature = dict["temperature"]
        if "end_words" in dict:
            for word in dict["end_words"]:
                self.end_words.append(word)
        if "bad_words" in dict:
            for word in dict["bad_words"]:
                self.bad_words.append(word)


class EmbeddingData(object):
    def __init__(self):
        self.oss_sign_url_list = []
        self.embedding_list = []

    def parse(self, dict):
        if "oss_sign_url_list" in dict:
            for oss_sign_url in dict["oss_sign_url_list"]:
                self.oss_sign_url_list.append(oss_sign_url)

        if "embedding_list" in dict:
            for embedding_url in dict["embedding_list"]:
                self.embedding_list.append(embedding_url)


class GenerateJob(object):
    def __init__(self):
        self.total_length = 0
        self.prompt = ""
        self.param = []
        self.model_version = ""
        self.job_key = ""
        self.job_type = ""
        self.job_result_key = ""
        self.time_stamp = 0
        # self.do_sensitive = True
        self.embedding_data = EmbeddingData()  # for mutltimodel

    def parse(self, dict):
        self.total_length = dict['total_length']
        if 'model_version' in dict:
            self.model_version = dict['model_version']
        if 'job_key' in dict:
            self.job_key = dict['job_key']
        if 'job_type' in dict:
            self.job_type = dict['job_type']
        self.job_result_key = dict['result_key']
        self.time_stamp = dict['timestamp']
        #   self.do_sensitive = task_param_dict['timestamp']
        if "embedding_data" in dict:
            self.embedding_data.parse(dict['embedding_data'])


class TaskProto(object):
    def __init__(self):
        self.job_result_key = ""
        self.param = ModelParam()
        self.generate_jobs = []

    def parse_task(self, task_str) -> (bool, str):
        """
            封装json结构解析到对象成员
            Args:
                task_str: 任务的json字符串
            Return:
                bool: 成功返回true，失败返回false
                str: 失败时返回错误信息，成功则为空字符串
        """
        pass


class RedisTaskProto(TaskProto):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "task result key:" + self.job_result_key

    def parse_task(self, task_str) -> (bool, str):
        """
            封装json结构解析到对象成员
            Args:
                task_str: 任务的json字符串
            Return:
                bool: 成功返回true，失败返回false
                str: 失败时返回错误信息，成功则为空字符串
        """
        try:
            task_param_dict = json.loads(task_str)
            self.job_result_key = task_param_dict['result_key']

            if "param" not in task_param_dict:
                return False, Exception("param node can't be non-existent!")
            self.param.parse(task_param_dict['param'])

            if "generate_jobs" not in task_param_dict:
                return False, Exception("generate_jobs node can't be non-existent!")

            for i in range(len(task_param_dict['generate_jobs'])):
                job = GenerateJob()
                job.parse(task_param_dict['generate_jobs'][i])
                self.generate_jobs.append(job)

        except Exception as ex:
            # log, or alarm

            #
            return False, str(ex)
        return True


class TaskResultProtoEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, TaskResultProto):
            return {
                "request_id": o.request_id,
                "model_key": o.model_key,
                "start_time": o.start_time,
                "finish_time": o.finish_time,
                "reply": o.reply,
                "finish_reason": o.finish_reason,
                "order": o.order,
                "finish": o.finish,
                "llm_engine_running_num": o.llm_engine_running_num
            }
        return super().default(o)


class TaskResultProto(object):
    def __init__(self):
        self.request_id = ""
        self.model_key = ""
        self.start_time = 0
        self.finish_time = 0
        self.reply = ""
        self.finish_reason = 1
        self.order = 0
        self.finish = False
        self.llm_engine_running_num = 0
        self.max_running_limit = 0

    def jsonformat(self) -> Any:
        return {
            "request_id": self.request_id,
            "model_key": self.model_key,
            "start_time": self.start_time,
            "finish_time": self.finish_time,
            "reply": self.reply,
            "finish_reason": self.finish_reason,
            "order": self.order,
            "finish": self.finish,
            "llm_engine_running_num": self.llm_engine_running_num
        }

    def to_json(self):
        return json.dumps(self, cls=TaskResultProtoEncoder)


class RedisTaskResultProto(TaskResultProto):
    def __init__(self, request_id: str, model_key: str, start_time: int, finish_time: int, reply: str,
                 finish_reason: int, order: int, finish: bool, llm_engine_running_num: int, max_running_limit: int):
        super().__init__()
        self.request_id = request_id
        self.model_key = model_key
        self.start_time = start_time
        self.finish_time = finish_time
        self.reply = reply
        self.finish_reason = finish_reason
        self.order = order
        self.finish = finish
        self.max_running_limit = max_running_limit
        self.llm_engine_running_num = llm_engine_running_num

import types

import model_infer_utils
import json
import enum

DEFAULTS = {
    "MODEL_PROJECT_NAME": "model_project_name",
    "MODEL_NAME_NODE": "model_name",
    "MODEL_RUN_ENV_NODE": "model_run_env",
    "MODEL_RUN_TYPE_NODE": "model_run_type",
    "LLM_CONFIG_NODE": "llm_config",
    "APP_LAUNCH_PARAM_NODE": "app_launch_param",
    "MODEL_RELATED_UPLOAD_PARAM_NODE": "model_related_upload_param",
    "MODEL_INFERENCE_COMPONENT_PARAM_NODE": "model_inference_component_param",
    "MODEL_REDIS":"model_redis"
}

Model_run_env = enum.Enum('MODEL_RUN_ENV', ('PAI_HK', 'PAI_WLCB', 'HUOSHAN_SHANGHAI'))  #枚举类型存储在json的value中时都是用大写,和普通配置参数区别开来
Model_run_type = enum.Enum('MODEL_RUN_TYPE', ('PROD', 'TEST', 'TO_BUSINESS', 'TO_EVALUATE'))

class ParamParseHelper(object):
    """
            帮助模型推理服务解析配置文件

            json结构基于已约定key名称提取不同部分子节点
    """
    def __init__(self, content: str) -> None:
        """
            Args:
                content:获取得到的配置json string
            Return:
                json.loads异常时需捕获
        """
        self.param_dict = json.loads(content)

        self.model_project_name = self.param_dict[DEFAULTS["MODEL_PROJECT_NAME"]]
        if len(self.model_project_name) == 0:
            raise Exception("node %s can't empty" % DEFAULTS["MODEL_PROJECT_NAME"])

        self.model_name = self.param_dict[DEFAULTS["MODEL_NAME_NODE"]]
        if len(self.model_name) == 0:
            raise Exception("node %s can't empty" % DEFAULTS["MODEL_NAME_NODE"])

        self.model_run_env = self.param_dict[DEFAULTS["MODEL_RUN_ENV_NODE"]].upper()
        if self.model_run_env not in Model_run_env.__members__:
            raise Exception("node %s value:%s, must in %s" % (DEFAULTS["MODEL_RUN_ENV_NODE"], self.model_run_env, ','.join(Model_run_env.__members__.keys())))

        self.model_run_type = self.param_dict[DEFAULTS["MODEL_RUN_TYPE_NODE"]].upper()
        if self.model_run_type not in Model_run_type.__members__:
            raise Exception("node %s value:%s, must in %s" % (DEFAULTS["MODEL_RUN_TYPE_NODE"], self.model_run_type, ','.join(Model_run_type.__members__.keys())))

        if DEFAULTS["LLM_CONFIG_NODE"] not in self.param_dict: #模型相关节点必须存在
            raise Exception("node %s isn't exist" % DEFAULTS["LLM_CONFIG_NODE"])

        if DEFAULTS["APP_LAUNCH_PARAM_NODE"] not in self.param_dict[DEFAULTS["LLM_CONFIG_NODE"]]:  # 模型推理程序启动参数节点必须存在
            raise Exception("node %s isn't exist in node %s" % (DEFAULTS["APP_LAUNCH_PARAM_NODE"], DEFAULTS["LLM_CONFIG_NODE"]))

        if DEFAULTS["MODEL_RELATED_UPLOAD_PARAM_NODE"] not in self.param_dict[DEFAULTS["LLM_CONFIG_NODE"]]:  # 模型工具包用于上传节点必须存在
            raise Exception("node %s isn't exist in node %s" % (DEFAULTS["MODEL_RELATED_UPLOAD_PARAM_NODE"], DEFAULTS["LLM_CONFIG_NODE"]))

        if DEFAULTS["MODEL_INFERENCE_COMPONENT_PARAM_NODE"] not in self.param_dict[DEFAULTS["LLM_CONFIG_NODE"]]:  # 模型工具包用于报警或存储log配置节点必须存在
            raise Exception("node %s isn't exist in node %s" % (DEFAULTS["MODEL_INFERENCE_COMPONENT_PARAM_NODE"], DEFAULTS["LLM_CONFIG_NODE"]))

        if DEFAULTS["MODEL_REDIS"] not in self.param_dict[DEFAULTS["LLM_CONFIG_NODE"]]:  # 模型推理用redis参数节点必须存在
            raise Exception(
                "node %s isn't exist in node %s" % (DEFAULTS["MODEL_REDIS"], DEFAULTS["LLM_CONFIG_NODE"]))

    def parse_app_launch_param(self, callback_func):
        """
            Args:
                callback_func:回调函数传入节点

        """
        if callback_func is not None:
            return callback_func(self.param_dict[DEFAULTS["LLM_CONFIG_NODE"]][DEFAULTS["APP_LAUNCH_PARAM_NODE"]])

    def get_app_launch_param(self):
        """
           Return:
               返回模型启动相关参数节点供解析
        """
        return self.param_dict[DEFAULTS["LLM_CONFIG_NODE"]][DEFAULTS["APP_LAUNCH_PARAM_NODE"]]

    def get_node_param_from_model_related_param(self, node_name:str):
        """
            Args:
               node_name:节点名称
            Return:
               返回模型启动相关参数节点供解析
        """
        return self.param_dict[DEFAULTS["LLM_CONFIG_NODE"]][node_name]

    def parse_node_from_llm_config_node(self, node_name:str, callback_func):
        """
            Args:
                callback_func:回调函数传入节点

        """
        if callback_func is not None:
            return callback_func(self.param_dict[DEFAULTS["LLM_CONFIG_NODE"]][node_name])

    def get_redis_config(self):
        """
           Return:
               返回模型启动相关参数节点供解析
        """
        return self.param_dict[DEFAULTS["LLM_CONFIG_NODE"]][DEFAULTS["MODEL_REDIS"]]

    def parse_redis_node(self, callback_func):
        """
            Args:
                callback_func:回调函数传入节点

        """
        if callback_func is not None:
            return callback_func(self.param_dict[DEFAULTS["LLM_CONFIG_NODE"]][DEFAULTS["MODEL_REDIS"]])
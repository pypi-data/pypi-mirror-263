import model_infer_utils


import nacos


class ModelConfig(object):
    """
        帮助模型推理服务拉取配置参数进行的封装

        这个版本封装的是nacos 客户端
    """
    def __init__(self) -> None:
        self.client = None

    def new_client(self, server_address: str, namespace: str, ak: str = None, sk: str = None, username: str = None, password: str = None) -> (bool, str):
        """
            Args:
                server_address:服务地址，格式参考https://xxx:8848，必填.可指定前缀https://或http://,默认不传使用http://,不传端口默认使用8848
                namespace: 命名空间，必填
                ak: 选填
                sk: 选填
                username: 选填,username + password或ak + sk必须传入一组才能鉴权成功
                password: 选填
            Return:
                如果成功返回True，参数二为空字符串。如果失败返回False，参数二为错误信息，可输出使用
        """
        try:
            self.client = nacos.NacosClient(server_address, namespace=namespace, ak=ak, sk=sk, username=username, password=password)
        except Exception as ex:
            return False, str(ex)
        return True, ""

    def load_model_config(self, group: str, data_id: str) ->(bool, str):
        """
            Args:
                group:组名，必填
                data_id: 配置的名称，必填
            Return:
                如果成功返回True，参数二为配置内容。如果失败返回False，参数二为错误信息，可输出使用
        """
        if self.client is None:
            return False, "client needs to be initialized, please call new_client()"
        try:
            content = self.client.get_config(data_id, group)
        except Exception as ex:
            return False, str(ex)
        if content is None:
            return False, "[load_model_config] config not found for data_id:%s, group:%s, namespace:%s"% (
                        data_id, group, self.client.namespace)
        else:
            return True, content
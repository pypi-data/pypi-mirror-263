from zhipuai import ZhipuAI
from zhipuai.core._base_type import NotGiven, NOT_GIVEN

_system_info = """
API Gateway or Initialization Prompt:

Attention, Model. You are about to receive an input query. It is crucial that you thoroughly analyze and comprehend the content before formulating a response. 
Your objective is to provide a thoughtful, precise, and enlightening answer that addresses the user's needs. 
Take into account the nuances of the query and utilize your robust processing capabilities to ensure a high-quality and relevant response.
Other than code and specific names and citations, your answer must be written in the same language as the question.
"""
from lmchain.config import  Config
class AgentZhipuAI:
    def __init__(self, api_key = "", client =ZhipuAI(api_key=Config.api_key), system_info =_system_info,
                 chat_model = "glm-4",image_model =  "cogview",embedding_model = "embedding-2",read_pic_model = "glm-4v"):
        if api_key == "":
            self.client = client  # 可以使用你自己key定义的chient
        else:
            self.client = ZhipuAI(api_key=api_key)

        if system_info == "":
            self.history = []
        else:
            self.history = [{"role": "system", "content": system_info}]

        self.model_name = chat_model
        self.image_model = image_model

        "下面是要处理embedding的集成"
        from lmchain.vectorstores import embeddings
        self.embedding_tool = embeddings.GLMEmbedding(client=self.client,model=embedding_model)
        "上面是要处理embedding的集成"

    def __call__(self, prompt="", role="user") -> str:
        """_call"""
        # construct query
        prompt_json = {
            "role": role,
            "content": prompt
        }
        self.history.append(prompt_json)
        response = self.client.chat.completions.create(
            model="glm-4",  # 填写需要调用的模型名称
            messages=self.history,
        )
        # 直接获取 message 字段，这里假设它是一个 CompletionMessage 实例
        choices = response.choices[0].message

        # 直接访问属性而不是作为字典键
        response_content = choices.content
        response_role = choices.role
        tool_calls = choices.tool_calls

        response_json = {
            "role": response_role,
            "content": response_content
        }
        self.history.append(response_json)

        return response_content

    "------------------------------------------下面是作图器部分--------------------------------------------------------------------"
    #显式图像
    def image_show(self,query):
        assert len(query) != 0, print("请输入作画要求")
        image = self.image_generator(query=query)
        image.show()

    #从做好的图像url地址将图像下载到本地
    def image_generator(self,query,return_np_image = False):
        assert  len(query) != 0,print("请输入作画要求")
        url = self.image_generator_get_url(query)

        import requests
        from PIL import Image
        from io import BytesIO

        # 发送HTTP请求获取图像数据
        response = requests.get(url)
        response.raise_for_status()  # 确保请求成功

        image = Image.open(BytesIO(response.content))

        if return_np_image:
            import  numpy as np
            import numpy as np
            _image = np.array(image)
            return image,_image #这里image的大小为[1024,1024],经过numpy则变为(1024, 1024, 3)
        return image

    #这力是使用作图器创作一个图像，并返回图像的URL地址
    def image_generator_get_url(self,query,
            quality = NOT_GIVEN,
            response_format  = NOT_GIVEN,
            size = NOT_GIVEN,
            style = NOT_GIVEN,
            user = NOT_GIVEN,
            extra_headers = None,
            disable_strict_validation = None):
        response = self.client.images.generations(
            model=self.image_model,  # 填写需要调用的模型名称
            prompt= query,
        )
        return (response.data[0].url)
    "------------------------------------------上面是作图器部分--------------------------------------------------------------------"

    "------------------------------------------下面是读图器，url输入可以为http://XXX.jpg--------------------------------------------------------------------"
    def read_pic_and_talk(self,query,url):
        response = self.client.chat.completions.create(
            model="glm-4v",  # 填写需要调用的模型名称
            messages=[                {                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": query
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": url
                            }                        }                    ]                }            ]        )
        return (response.choices[0].message.content)


if __name__ == '__main__':
    llm = AgentZhipuAI(system_info="你现在是一名相声演员，有非常丰富的讲笑话能力。")

    print(llm("你是谁"))

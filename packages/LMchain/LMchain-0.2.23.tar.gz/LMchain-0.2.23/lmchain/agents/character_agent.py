from zhipuai import ZhipuAI
from zhipuai.core._base_type import NotGiven, NOT_GIVEN

_system_info = """
API Gateway or Initialization Prompt:

Attention, Model. You are about to receive an input query. It is crucial that you thoroughly analyze and comprehend the content before formulating a response. 
Your objective is to provide a thoughtful, precise, and enlightening answer that addresses the user's needs. 
Take into account the nuances of the query and utilize your robust processing capabilities to ensure a high-quality and relevant response.
Other than code and specific names and citations, your answer must be written in the same language as the question.
\n\n
"""
from lmchain.config import  Config

class CharacterAgentZhipuAI:
    def __init__(self, api_key = "", client =ZhipuAI(api_key=Config.api_key), system_info ="",chat_model = "glm-4"):
        if api_key == "":
            self.client = client  # 可以使用你自己key定义的chient
        else:
            self.client = ZhipuAI(api_key=api_key)

        if system_info == "":
            self.history = [{"role": "system", "content": _system_info}]
        else:
            self.history = [{"role": "system", "content": _system_info + system_info}]

        self.model_name = chat_model

    def __call__(self, prompt="", role="user") -> str:
        """_call"""
        # construct query
        prompt_json = {
            "role": role,
            "content": prompt
        }
        self.history.append(prompt_json)
        response = self.client.chat.completions.create(
            model=self.model_name,  # 填写需要调用的模型名称
            messages=self.history,
        )
        # 直接获取 message 字段，这里假设它是一个 CompletionMessage 实例
        choices = response.choices[0].message

        # 直接访问属性而不是作为字典键
        response_content = choices.content
        response_role = choices.role

        response_json = {
            "role": response_role,
            "content": response_content
        }
        self.history.append(response_json)

        return response_content

if __name__ == '__main__':
    llm = CharacterAgentZhipuAI()

    response = llm("你好")
    print(response)

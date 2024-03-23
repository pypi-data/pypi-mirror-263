from lmchain.agents.character_agent import CharacterAgentZhipuAI

class Agent:
    def __init__(self,name,role,capabilities:list = []):
        #这里的agent只需要它的角色定义，以及传送来的记忆就可以了
        self.name = name
        self.role = str({"role":role,"name":name})
        self.capabilities = capabilities
        self.memories = []  # Each agent has its own memory

    def remember(self,message):
        self.memories.append(message)

    def add_capabilities(self,capabily):
            if  isinstance(capabily,list):
                self.capabilities.extend(capabily)
            else:
                self.capabilities.extend([capabily])

class GroundManager:
    def __init__(self,ground_info,model = CharacterAgentZhipuAI):
        self.ground_info = ground_info
        self.ground_messages = []
        self.agents = []
        self.model = model

    def add_ground_messages(self,name,role,content):
        self.ground_messages.append({"name":name,"role":role,"content":content})

    def get_message(self):
        return self.messages

    def broadcast(self,message):
        for agent in self.agents:
            agent.remember(message)

    def generate_agent_response(self,agent):
        agent_role = agent.role
        ground_agent_prompt = self.ground_info + agent_role + "\n\n" + str(agent.capabilities)

        character_model = self.model(system_info = ground_agent_prompt)
        response = character_model(prompt = str(agent.memories))
        self.add_ground_messages(name=agent.name,role=agent_role,content=response)

        self.broadcast(self.ground_messages)
        return response

    def ground_run(self,epoch = 10):
        flag = True
        for _ in range(epoch):
            for agent in self.agents:
                response = self.generate_agent_response(agent)
                print(agent.name, " : ", response)
                print("----------------------------------------------------------------")
                if "问题已经解决" in response:
                    flag = False
                    break
            if flag == False:
                print("问题已经解决，场景结束！")
                break



if __name__ == '__main__':

    ground_info = "\n\n这里是一个专业的骨科医院，有专业骨科大夫，病人，还有一个观察者。你需要扮演其中一个角色，而且仅仅扮演一个角色。\n\n无论扮演谁你都会认真对待你的角色设定，你都会仔细思考你的角色定义，准确的用中文，按照你的角色定义，认真描述和回答你自己的问题，不要设想别的角色。\n\n"
    conversation_manager = GroundManager(ground_info=ground_info)

    agent1 = Agent(name="Doctor Tony",role="我是一名等待病人问询的骨科医生",capabilities=["作为医生如果你认为已经做出完整的回答，直接回答 '我的回答已经完毕~' 不要回答其他内容。\n\n","作为医生如果看到观察者回答 '你的回答有违设定' ，你需要重新思考并回答问题。\n\n"])
    agent2 = Agent(name="Xiaohua",role="我是一名感觉跑步时右腿膝盖痛的患者",capabilities=["作为患者如果认为自己的问题已经解决，要先阐述获得的解决问题的方法，然后回答 '问题已经解决！' 不要回答其他内容。\n\n","作为患者如果看到观察者回答 '你的回答有违设定' ，你需要重新思考并阐述问题。\n\n"])
    observers = Agent(name="OBSERVERS",role="我是一名观察者，在当前场景下知晓所有的内容，你的作用是判断所有的问题与回复是否有违场景设定。",capabilities=["作为观察者，经过你的认真思考，如果认为所有的问题已经解决，对整个对话场景做出一个总结，然后做出决定，只回答 \n'问题已经解决！' 不要回答其他内容。\n\n","作为观察者，经过你的认真思考，如果问题与回复有违角色设定，回答 '你的回答有违设定！' 不要回答其他内容。\n\n","作为观察者，经过你的认真思考，如果问题与回复符合场景需求，回答 '请继续~' 不要回答其他内容。\n\n"])
    conversation_manager.agents.extend([agent1,agent2,observers])

    conversation_manager.ground_run()


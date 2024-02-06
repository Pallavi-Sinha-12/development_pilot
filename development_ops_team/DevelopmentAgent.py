from langchain.agents.openai_assistant import OpenAIAssistantRunnable

class DevelopmentAgent:

    def __init__(self, agent_role, agent_backstory, tools = [], model_name = "gpt-4-1106-preview"):
        self.agent_role = agent_role
        self.agent_backstory = agent_backstory
        self.tools = tools
        self.model_name = model_name

    def create_assistant(self) -> OpenAIAssistantRunnable:
        return OpenAIAssistantRunnable.create_assistant(
            name= self.agent_role,
            instructions= self.agent_backstory,
            tools= self.tools,
            model= self.model_name,
        )
    
    def extract_value(self, assistant_output : list ) -> str:
        raw_output = str(assistant_output)
        start_index = raw_output.find("value=") + len("value=")
        end_index = raw_output.find(", type='text')")
        extracted_value = raw_output[start_index:end_index].strip().lstrip('"').rstrip('"').strip(")")
        return extracted_value
            
    def invoke(self, assistant : OpenAIAssistantRunnable , query : str) -> str:
        assistant_output =  assistant.invoke({"content": query})
        extracted_value = self.extract_value(assistant_output)
        return extracted_value
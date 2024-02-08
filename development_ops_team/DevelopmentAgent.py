from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from typing import Any


class DevelopmentAgent:
    """
    Represents a development agent that interacts with an OpenAI assistant.

    Attributes:
        agent_role (str): The role of the agent.
        agent_backstory (str): The backstory of the agent.
        tools (list): The tools used by the agent (default to an empty list).
        model_name (str): The name of the model used by the agent (default to "gpt-4-1106-preview").


    Methods:
        create_assistant(self): Creates an OpenAI assistant using the specified parameters.
        extract_value(self, assistant_output): Extracts the reply from the OpenAI assistant's output.
        invoke(self, assistant, query): Invokes the OpenAI assistant with the specified query and returns the extracted reply.
    """

    def __init__(
        self,
        agent_role: str,
        agent_backstory: str,
        tools: list = [],
        model_name: str = "gpt-4-1106-preview",
    ):
        """
        Initializes a new instance of the DevelopmentAgent class.

        Args:
            agent_role (str): The role of the agent.
            agent_backstory (str): The backstory of the agent.
            tools (list, optional): The tools used by the agent (default to an empty list).
            model_name (str, optional): The name of the model used by the agent (default to "gpt-4-1106-preview").
        """
        self.agent_role = agent_role
        self.agent_backstory = agent_backstory
        self.tools = tools
        self.model_name = model_name

    def create_assistant(self) -> OpenAIAssistantRunnable:
        """
        Creates an OpenAI assistant using the specified parameters.

        Returns:
            OpenAIAssistantRunnable: The created OpenAI assistant.
        """
        return OpenAIAssistantRunnable.create_assistant(
            name=self.agent_role,
            instructions=self.agent_backstory,
            tools=self.tools,
            model=self.model_name,
        )

    def extract_value(self, assistant_output: list) -> str:
        """
        Extracts the reply from the OpenAI assistant's output.

        Args:
            assistant_output (list): The output from the OpenAI assistant.

        Returns:
            str: The extracted reply from the assistant's output.
        """
        raw_output = str(assistant_output)
        start_index = raw_output.find("value=") + len("value=")
        end_index = raw_output.find(", type='text')")
        extracted_value = (
            raw_output[start_index:end_index].strip().lstrip('"').rstrip('"').strip(")")
        )
        return extracted_value

    def invoke(self, assistant: OpenAIAssistantRunnable, query: str) -> str:
        """
        Invokes the OpenAI assistant with the specified query and returns the extracted value.

        Args:
            assistant (OpenAIAssistantRunnable): The OpenAI assistant to invoke.
            query (str): The query to send to the assistant.

        Returns:
            str: The extracted value from the assistant's response.
        """
        assistant_output = assistant.invoke({"content": query})
        extracted_value = self.extract_value(assistant_output)
        return extracted_value

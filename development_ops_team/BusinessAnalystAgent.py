from development_ops_team.DevelopmentAgent import DevelopmentAgent

class BusinessAnalystAgent(DevelopmentAgent):
    """
    Represents a Business Analyst Agent responsible for translating business needs into precise requirement questions.

    Attributes:
        domain (str): The domain in which the Business Analyst specializes.
        model_name (str): The name of the model used by the agent.

    Methods:
        ask(self, query: str) -> str: Asks a question to the assistant and returns the extracted value.
    """

    def __init__(self, domain: str, model_name: str = "gpt-4-1106-preview"):
        """
        Initializes a BusinessAnalystAgent object.

        Args:
            domain (str): The domain in which the Business Analyst specializes.
            model_name (str, optional): The name of the model used by the agent. Defaults to "gpt-4-1106-preview".
        """
        self.domain = domain
        agent_role = "Business Analyst"
        agent_backstory = f"""
            As a highly dedicated and seasoned Business Analyst with over 20 years of expertise in the dynamic {self.domain} domain, you play a pivotal role in translating business aspirations into precise technical solutions. 
            Renowned for your proactive approach and sharp analytical skills, you meticulously dissect the provided business context, ensuring a comprehensive understanding.
            Your task is to craft incisive requirement questions that delve deep into specific facets of the feature, reflecting your commitment to clarity and precision. 
            Every question you pose is aimed at extracting valuable insights, and you exhibit a keen ability to bridge the gap between intricate business needs and streamlined technical solutions.
            Your extensive experience has honed your knack for formulating questions that are not only clear and concise but also considerate of diverse audiences, avoiding assumptions about prior knowledge. Embrace the inherent nuances of the {self.domain} domain, showcasing your domain-specific acumen.
            Present your requirement questions in a structured format, leveraging your expertise to drive effective communication. 
            Your active engagement and meticulous questioning set the stage for insightful responses from the Subject Matter Expert, contributing significantly to the project's success.
            Your aspiration for continuous improvement and your natural curiosity form the cornerstone of your proactive approach, ensuring that no stone is left unturned in the pursuit of comprehensive project insights.
        """
        tools = []
        self.model_name = model_name

        super().__init__(agent_role, agent_backstory, tools, self.model_name)

    def ask(self, query: str) -> str:
        """
        Asks a question to the Business Analyst Agent and returns the reply.

        Args:
            query (str): The question to ask the assistant.

        Returns:
            str: The reply for the specified query.
        """
        assistant = self.create_assistant()
        extracted_value = self.invoke(assistant, query)
        return extracted_value
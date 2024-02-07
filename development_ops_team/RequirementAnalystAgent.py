from development_ops_team.DevelopmentAgent import DevelopmentAgent

class RequirementAnalystAgent(DevelopmentAgent):
    """
    Represents a Requirement Analyst Agent responsible for translating business needs into requirement rules, acceptance criteria, and user flows.

    Attributes:
        domain (str): The domain in which the Requirement Analyst specializes.
        model_name (str): The name of the language model to be used by the agent.

    Methods:
        ask(self, query: str) -> str: Asks a question to the assistant and returns the extracted value.
    """

    def __init__(self, domain : str, model_name : str = "gpt-4-1106-preview"):
        """
        Initializes a RequirementAnalystAgent object.

        Args:
            domain (str): The domain in which the Requirement Analyst specializes.
            model_name (str, optional): The name of the language model to be used by the agent. Defaults to "gpt-4-1106-preview".
        """
        self.domain = domain
        agent_role = "Requirement Analyst"
        agent_backstory = f"""
        As a seasoned Requirement Analyst with over 25 years of expertise in the {self.domain} domain, you play a pivotal role in translating business needs into technical solutions. 
        Working closely with the Subject Matter Expert, who provides detailed insights into the business context, your responsibility is to synthesize the final requirement rules and acceptance criteria for the upcoming business feature.
        In this critical task, leverage your extensive domain knowledge to bridge the gap between the provided business context and technical implementation. 
        Define the requirement rules , acceptance criteria and user flow with utmost clarity and conciseness, ensuring a comprehensive understanding by all stakeholders that align with the domain, business context, and the requirements furnished by the Subject Matter Expert. 
        Execute this responsibility with diligence, drawing upon your analytical skills, attention to detail, and collaborative approach. 
        Your role significantly contributes to the success of the project by providing a robust foundation for the development and testing phases.
        """
        tools = []
        self.model_name = model_name

        super().__init__(agent_role, agent_backstory, tools, self.model_name)

    def ask(self, query: str) -> str:
        """
        Asks a question to the Requirement Analyst Agent and returns the reply.

        Args:
            query (str): The question to ask the Requirement Analyst Agent.

        Returns:
            str: The reply for the specified query from the assistant.
        """
        assistant = self.create_assistant()
        extracted_value = self.invoke(assistant, query)
        return extracted_value


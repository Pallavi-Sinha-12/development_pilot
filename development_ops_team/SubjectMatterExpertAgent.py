from development_ops_team.DevelopmentAgent import DevelopmentAgent


class SubjectMatterExpertAgent(DevelopmentAgent):
    """
    Represents a Subject Matter Expert agent that provides comprehensive answers to requirement questions specific to a domain of expertise.

    Args:
        domain (str): The domain of expertise for the agent.
        model_name (str, optional): The name of the model to be used by the agent. Defaults to "gpt-4-1106-preview".

    Attributes:
        domain (str): The domain of expertise for the agent.
        model_name (str): The name of the model used by the agent.

    Methods:
        ask(self, query): Asks the agent a question and returns the reply.
    """

    def __init__(self, domain: str, model_name: str = "gpt-4-1106-preview"):
        """
        Initializes a new instance of the SubjectMatterExpertAgent class.

        Args:
            domain (str): The domain of expertise for the agent.
            model_name (str, optional): The name of the model to be used by the agent. Defaults to "gpt-4-1106-preview".
        """
        self.domain = domain
        self.model_name = model_name

        agent_role = "Subject Matter Expert"
        agent_backstory = f"""
        As a distinguished Subject Matter Expert with over 30 years of unwavering expertise in the {self.domain} domain, you stand as the epitome of domain mastery within our esteemed organization. 
        Renowned for your profound understanding of the intricate business context, you bring a wealth of knowledge that is unparalleled.
        Your role is to address the requirement questions posed by the Business Analyst, leveraging your extensive domain knowledge and business acumen to provide comprehensive answers.
        Embrace the role of a guide and informant, offering insights that go beyond the surface, reflecting your commitment to excellence. 
        Your responses should showcase the clarity of thought and a keen awareness of the nuanced requirements, ensuring that the information provided is not only precise but also aligns seamlessly with the overarching goals of the business feature.
        Tap into your vast knowledge base to provide specific and actionable details, elevating the collaborative effort with the Business Analyst. 
        Your dedication to clarity, precision, and depth in your responses sets the stage for a seamless transition from requirements to implementation. 
        As a respected SME, your contribution plays a pivotal role in shaping the success of the project."
        """
        tools = []

        super().__init__(agent_role, agent_backstory, tools, self.model_name)

    def ask(self, query: str) -> str:
        """
        Asks the Subject Matter Expert agent a question and returns the reply.

        Args:
            query (str): The question to ask the agent.

        Returns:
            str: The reply for the specified query from the agent.
        """
        assistant = self.create_assistant()
        extracted_value = self.invoke(assistant, query)
        return extracted_value

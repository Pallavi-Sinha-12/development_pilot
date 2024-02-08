from development_ops_team.DevelopmentAgent import DevelopmentAgent


class QualityAssuranceAgent(DevelopmentAgent):
    """
    Represents a Quality Assurance Agent responsible for generating rigorous test scenarios and crafting comprehensive test cases.

    Attributes:
        domain (str): The domain of expertise for the Quality Assurance Agent.
        model_name (str): The name of the model used by the Quality Assurance Agent.

    Methods:
        ask(self, query): Asks a question to the Quality Assurance Agent's assistant and returns the extracted value.
    """

    def __init__(self, domain: str, model_name: str = "gpt-4-1106-preview"):
        """
        Initializes a QualityAssuranceAgent object.

        Args:
            domain (str): The domain of expertise for the Quality Assurance Agent.
            model_name (str): The name of the model used by the Quality Assurance Agent.
        """

        self.domain = domain
        self.model_name = model_name

        agent_role = "Quality Assurance Engineer"
        agent_backstory = f"""
        As a highly seasoned Quality Assurance Engineer with an illustrious 30-year career in the {self.domain} domain, you bring a wealth of expertise to the testing phase. 
        Renowned for your meticulous approach, you are committed to upholding the highest standards of quality in software development.

        In your role, you are tasked with generating rigorous test scenarios for the upcoming business feature. 
        Given the requirement rules and acceptance criteria provided by the Requirement Analyst, your mission is to craft comprehensive test cases that leave no room for ambiguity or oversight.        Your keen eye for detail ensures that each test case includes vital components:

        1. Test Case Name
        2. Test Case Description (Given, When, Then)
        3. Test Case Expected Result

        Striving for perfection, you aim to cover every nuance of the requirement rules and acceptance criteria. 
        Your test cases not only validate the functional aspects but also encompass various scenarios, ensuring the robustness and reliability of the business feature.
        Known for your strict adherence to quality, you harbor an unwavering commitment to identifying and rectifying any potential flaws. 
        Your relentless pursuit of perfection aligns with your aspirations for continuous career growth and excellence in the dynamic landscape of software testing.
        Execute your QA role with unwavering dedication, contributing to the project's success by fortifying it against potential defects and delivering a product of the highest caliber.

        """
        tools = []

        super().__init__(agent_role, agent_backstory, tools, self.model_name)

    def ask(self, query: str) -> str:
        """
        Asks a question to the Quality Assurance Agent and returns the reply from the assistant.

        Args:
            query (str): The question to ask the assistant.

        Returns:
            str: The reply for the specified query from the assistant.
        """

        assistant = self.create_assistant()
        extracted_value = self.invoke(assistant, query)
        return extracted_value

import streamlit as st
import os
from development_ops_team.BusinessAnalystAgent import BusinessAnalystAgent
from development_ops_team.SubjectMatterExpertAgent import SubjectMatterExpertAgent
from development_ops_team.RequirementAnalystAgent import RequirementAnalystAgent
from development_ops_team.QualityAssuranceAgent import QualityAssuranceAgent

domains = ["Agriculture & Mining", "Automotive", "Business Services", "Computers & Electronics", "Consumer Services", "Education", "Energy & Utilities", "Engineering, Research & Development", "Financial Services", "Government", "Healthcare, Pharmaceuticals & Biotechnology", "Insurance", "Manufacturing", "Media, Publishing & Entertainment", "Non-Profit", "Payments Systems", "Real Estate & Construction", "Retail", "Software & Internet", "Telecommunications", "Transportation & Storage", "Travel, Recreation & Leisure", "Wholesale & Distribution"]
if "business_domain" not in st.session_state:
    st.session_state.business_domain_index = 0
st.sidebar.title("Development Pilot 🚀")

st.sidebar.markdown("""
    Welcome to Development Pilot, your AI-powered team for step by step business feature development.
""")


if "is_openai_api_key_set" not in st.session_state:
    st.session_state.is_openai_api_key_set = False

openai_api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
if st.sidebar.button("Set OpenAI API Key"):

    st.session_state.openai_api_key = openai_api_key
    os.environ["OPENAI_API_KEY"] = st.session_state.openai_api_key
    st.sidebar.success("OpenAI API Key successfully set!")
    st.session_state.is_openai_api_key_set = True


if st.session_state.is_openai_api_key_set:

    st.sidebar.markdown("---")

    st.sidebar.subheader("Project Overview")

    st.sidebar.markdown(
        """
        Development Pilot is a comprehensive AI-powered assistant designed to assist you throughout the project development lifecycle.
        
        **Tabs:**
        - **Business Analyst (BA) 📈:** Analyze and generate requirement questions based on the provided business context.
        - **Subject Matter Expert (SME) 🧠:** Answer the generated requirement questions from BA based on domain knowledge.
        - **Requirement Analyst (RA) 📝:**  Synthesizes the information gathered from SME and defines detailed requirement rules.
        - **Quality Assurance (QA) 🕵️‍♂️:** Generate test cases from the requirement rules to ensure comprehensive testing.

        Use these assistants to enhance collaboration and streamline your project workflow. Happy coding! 🚀
        """
    )

    st.sidebar.markdown("© 2024 Development Pilot. All rights reserved.")

    tab1, tab2, tab3, tab4 = st.tabs(["Business Analyst (BA) 📈", "Subject Matter Expert (SME) 🧠", "Requirement Analyst (RA) 📝", "Quality Assurance (QA) 🕵️‍♂️"])


    with tab1:
        st.header("Business Analyst (BA) 📈")
        business_context = st.text_area("Enter Business Context for the new feature:", height=300)
        business_domain = st.selectbox("Select Business Domain:", domains, index=st.session_state.business_domain_index, key='business_domain_tab1')
        st.session_state.business_context = business_context
        st.session_state.business_domain = business_domain
        st.session_state.business_domain_index = domains.index(business_domain)
        if st.button("Generate Requirement Questions"):
            businessAnalystAgent = BusinessAnalystAgent(st.session_state.business_domain)
            question_to_BA = fr""" The following is the business context for the new feature: {st.session_state.business_context}.
            Please generate requirement questions for the given business context by considering the domain of the business you are working in.
            """
            with st.spinner("Generating requirement questions..."):
                requirement_questions = businessAnalystAgent.ask(question_to_BA)
            st.session_state.requirement_questions = requirement_questions.replace("\\n", "\n")
            st.success("Requirement questions generated successfully! ✔️")

        if "requirement_questions" in st.session_state:
            st.markdown(f"**Requirement Questions 🤔:** {st.session_state.requirement_questions}", unsafe_allow_html=True)

            st.download_button(
                label="Download Requirement Questions",
                data= st.session_state.requirement_questions,
                file_name="requirement_questions.txt",
                mime="text/markdown",
            )

            st.info("To interact with the Subject Matter Expert, click on the next tab.")
    
    with tab2:
        st.header("Subject Matter Expert (SME) 🧠")
        requirement_questions_to_SME = st.text_area("Enter Requirement Questions from the BA:", value=st.session_state.requirement_questions if "requirement_questions" in st.session_state else '', height=300)
        if "requirement_questions" in st.session_state:
            st.info("The requirement questions generated by the Business Analyst are pasted here. Feel free to edit the questions if needed.")
        business_domain = st.selectbox("Select Business Domain:", domains, index=st.session_state.business_domain_index, key='business_domain_tab2' )
        st.session_state.business_domain = business_domain
        st.session_state.business_domain_index = domains.index(business_domain)
        st.session_state.requirement_questions_to_SME = requirement_questions_to_SME
        if st.button("Answer Requirement Questions"):
            subjectMatterExpertAgent = SubjectMatterExpertAgent(st.session_state.business_domain)
            question_to_SME = f""" The following are the requirement questions asked by the Business Analyst: {st.session_state.requirement_questions_to_SME}. For each question, try to be informative and clear in your answers. 
            For your reference, the new business feature context is as follows: {st.session_state.business_context}. Your answers should contain only the information that is relevant to the questions asked.
            """
            with st.spinner("Answering requirement questions..."):
                sme_reqirements_response = subjectMatterExpertAgent.ask(question_to_SME)
            st.session_state.sme_reqirements_response = sme_reqirements_response.replace("\\n", "\n")
            st.success("Requirement questions answered successfully by SME! ✔️ ")

        if "sme_reqirements_response" in st.session_state:
            st.markdown(f"**SME Requirement Responses 💡:** {st.session_state.sme_reqirements_response}", unsafe_allow_html=True)

            st.download_button(
                label="Download SME Requirement Responses",
                data=st.session_state.sme_reqirements_response,
                file_name="sme_reqirements_response.txt",
                mime="text/markdown",
            )

            st.info("To interact with the Requirement Analyst, click on the next tab.")

    with tab3:
        st.header("Requirement Analyst (RA) 📝")
        sme_reqirements_response_to_RA = st.text_area("Enter Requirement Responses from the SME:", value=st.session_state.sme_reqirements_response if "sme_reqirements_response" in st.session_state else '', height=300)
        if "sme_reqirements_response" in st.session_state:
            st.info("The requirement responses from the Subject Matter Expert are pasted here. Feel free to edit the responses if needed.")
        st.session_state.sme_reqirements_response_to_RA = sme_reqirements_response_to_RA
        business_domain = st.selectbox("Select Business Domain:", domains, index=st.session_state.business_domain_index, key='business_domain_tab3')
        st.session_state.business_domain = business_domain
        st.session_state.business_domain_index = domains.index(business_domain)
        if st.button("Generate Requirement Rules"):
            requirementAnalystAgent = RequirementAnalystAgent(st.session_state.business_domain)
            question_to_RA = f""" The following are the requirement responses from the Subject Matter Expert: {st.session_state.sme_reqirements_response_to_RA}.
            Based on the requirement responses, define detailed requirement rules, acceptance criteria and user flows for the new business feature.
            """
            with st.spinner("Generating requirement rules..."):
                requirement_rules = requirementAnalystAgent.ask(question_to_RA)
            st.session_state.requirement_rules = requirement_rules.replace("\\n", "\n")
            st.success("Requirement rules generated successfully by RA! ✔️")

        if "requirement_rules" in st.session_state:
            st.markdown(f"**Requirement Rules 📝:** {st.session_state.requirement_rules}", unsafe_allow_html=True)
            
            st.download_button(
                label="Download Requirement Rules",
                data=st.session_state.requirement_rules,
                file_name="requirement_rules.txt",
                mime="text/markdown",
            )

            st.info("To interact with the Quality Assurance, click on the next tab.")
    with tab4:
        st.header("Quality Assurance (QA) 🕵️‍♂️")
        requirement_rules_to_QA = st.text_area("Enter Requirement rules, acceptance criteria and user flows from the RA:", value=st.session_state.requirement_rules if "requirement_rules" in st.session_state else '', height=300)
        if "requirement_rules" in st.session_state:
            st.info("The requirement rules, acceptance criteria and user flows from the Requirement Analyst are pasted here. Feel free to edit the requirement rules if needed.")
        st.session_state.requirement_rules_to_QA = requirement_rules_to_QA
        business_domain = st.selectbox("Select Business Domain:", domains, index=st.session_state.business_domain_index, key='business_domain_tab4')
        st.session_state.business_domain = business_domain
        st.session_state.business_domain_index = domains.index(business_domain)
        if st.button("Generate Test Cases"):
            qualityAssuranceAgent = QualityAssuranceAgent(st.session_state.business_domain)
            question_to_QA = f""" The following are the requirement rules, acceptance criteria and user flows for the new business feature from Requirement Analyst: {st.session_state.requirement_rules_to_QA}.
            The business feature context is as follows: {st.session_state.business_context}.
            Generate test scenarios for the given business feature and given requirement rules and acceptance criteria.
            """
            with st.spinner("Generating test cases..."):
                test_cases = qualityAssuranceAgent.ask(question_to_QA)
            st.session_state.test_cases = test_cases.replace("\\n", "\n")
            st.success("Test cases generated successfully by QA! ✔️")

        if "test_cases" in st.session_state:
            st.markdown(f"**Test Cases 🧪:** {st.session_state.test_cases}", unsafe_allow_html=True)
            
            st.download_button(
                label="Download Test Cases",
                data=st.session_state.test_cases,
                file_name="test_cases.txt",
                mime="text/markdown",
            )
            
            st.info("Feel free to copy the generated test cases and use them for your development of the business feature. Happy coding! 🚀")

else:
    st.warning("Please enter your OpenAI API key to get started.")
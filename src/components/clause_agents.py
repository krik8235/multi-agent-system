import os

from crewai import Agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from components.tools import rag_query_tools, rag_tools

load_dotenv(override=True)

# AI ML API - https://aimlapi.com/app/
AI_API_KEY_AIMLAPI = os.environ.get("AI_API_KEY_AIMLAPI")
AI_API_BASE_AIMLAPI = os.environ.get("AI_API_BASE_AIMLAPI")
AI_MODEL_NAME_AIMLAPI = os.environ.get("AI_MODEL_NAME_AIMLAPI")


# LiteLLM - https://docs.litellm.ai/docs/providers
AI_API_KEY_LITELLM = os.environ.get("AI_API_KEY_LITELLM")
AI_API_BASE_LITELLM = os.environ.get("AI_API_BASE_LITELLM")
AI_MODEL_NAME_LITELLM = os.environ.get("AI_MODEL_NAME_LITELLM")

llm = ChatOpenAI(
    openai_api_key=AI_API_KEY_LITELLM,
    openai_api_base=AI_API_BASE_LITELLM,
    model_name=AI_MODEL_NAME_LITELLM,
    temperature=0.1,
)
# llm = LLM(
#     model=OPENAI_MODEL_NAME,
#     base_url=OPENAI_API_BASE,
#     api_key=OPENAI_API_KEY
# )


corporate_lawyer_agent = Agent(
    role="Corporate Lawyer",
    goal="Use the documents you're given and the tools you have to build a knowledge base of NDAs that you can refer later. First, check if the documents have already been added.",
    backstory="""You are a corporate lawyer who has vast knowledge of NDAs, different sections within them, and how they are supposed to work.
    You also have the ability to call the RAG tool to ingest new documents that using the paths of files given to you and building a knowledge base of NDAs.""",
    # tools=rag_tools,
    verbose=True,
    llm=llm,
)
corporate_lawyer_agent.tools = rag_tools


### Clause agents and tasks here - try to check if one agent can be used for multiple clauses, since handoff between agents takes time
parties_corporate_lawyer = Agent(
    role="Parties Corporate Lawyer",
    goal="To compare the current NDA parties clause to the ones in our RAG database and identify how good it is.",
    backstory="""You are a corporate lawyer who specialises in identifying who the parties in a certain NDA are.
    There's no one who does it as well as you do. Things that others miss, you don't.""",
    # tools=rag_query_tools,
    verbose=True,
    llm=llm,
)
parties_corporate_lawyer.tools = rag_query_tools

# obligations of receiving party
obligation_information_lawyer = Agent(
    role="Obligations of Receiving Party Lawyer",
    goal="To compare the current NDA obligations of receiving party clause to the ones in our RAG database and identify how good it is.",
    backstory="""You are an obligations of receiving party lawyer who is an expert in identifying what the obligations of receiving party is in a certain NDA.
    You have never failed to identify obligations of receiving party in an NDA. You are a lawyer with many years of experience and know how to identify obligations of receiving party.
    """,
    # tools=rag_query_tools,
    verbose=True,
    llm=llm,
)
obligation_information_lawyer.tools = rag_query_tools


# terms and termination
terms_and_termination_lawyer = Agent(
    role="Terms and Termination Lawyer",
    goal="To compare the current NDA terms and termination clause to the ones in our RAG database and identify how good it is.",
    backstory="""You are a terms and termination lawyer who is an expert in identifying what the terms and termination is in a certain NDA.
    Terms and terminatioin are in your DNA. When given an NDA, you're eyes first go to terms and termination clause and you can identify fallacies well.
    """,
    # tools=rag_query_tools,
    verbose=True,
    llm=llm,
)
terms_and_termination_lawyer.tools = rag_query_tools

# remedies
remedies_lawyer = Agent(
    role="Remedies Lawyer",
    goal="To compare the current NDA remedies clause to the ones in our RAG database and identify how good it is.",
    backstory="""You are a remedies lawyer who is an expert in identifying what the remedies is in a certain NDA.
    You craft perfect remedies in an NDA in the case of breach or conflict. You are the go to person for remedies in an NDA.
    """,
    # tools=rag_query_tools,
    verbose=True,
    llm=llm,
)
remedies_lawyer.tools = rag_query_tools

# additional important information
additional_information_lawyer = Agent(
    role="Additional Important Information Lawyer",
    goal="To compare the current NDA additional important information clause to the ones in our RAG database and identify how good it is.",
    backstory="""You are an additional important information lawyer who is an expert in identifying what the additional important information is in a certain NDA.
    You identify up all the missing information in an NDA. You carefully craft perfect additional important information in an NDA.
    """,
    # tools=rag_query_tools,
    verbose=True,
    llm=llm,
)
additional_information_lawyer.tools = rag_query_tools

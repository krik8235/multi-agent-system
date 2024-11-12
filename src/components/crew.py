from typing import Dict
from crewai import Crew, Process
from dotenv import load_dotenv
from components.clause_agents import (
    additional_information_lawyer,
    corporate_lawyer_agent,
    obligation_information_lawyer,
    remedies_lawyer,
    terms_and_termination_lawyer,
)
from components.clause_tasks import get_tasks
load_dotenv(override=True)


def get_crew(input_doc):
    crew = Crew(
        agents=[
            corporate_lawyer_agent,
            obligation_information_lawyer,
            terms_and_termination_lawyer,
            remedies_lawyer,
            additional_information_lawyer,
        ],
        tasks=get_tasks(input_doc),
        process=Process.sequential,
        verbose=True
    )
    return crew


def get_agent_output(document_from_frontend):
    crew = get_crew(document_from_frontend)
    result = crew.kickoff()

    if isinstance(result, dict) and "accumulated_results" in result:
        return result["accumulated_results"]
    else:
        # Fallback in case the modification didn't work as expected
        return {"final_recommendation": result}

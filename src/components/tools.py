import os
from composio_crewai import Action, App, ComposioToolSet
from dotenv import load_dotenv
load_dotenv(override=True)


composio_toolset = ComposioToolSet(api_key=os.environ.get("COMPOSIO_API_KEY"))

rag_tools = composio_toolset.get_tools(
    apps=[App.RAGTOOL],
    actions=[
        Action.FILETOOL_LIST_FILES,
        Action.FILETOOL_CHANGE_WORKING_DIRECTORY,
        Action.FILETOOL_FIND_FILE,
    ],
)

rag_query_tools = composio_toolset.get_tools(
    apps=[App.RAGTOOL],
)
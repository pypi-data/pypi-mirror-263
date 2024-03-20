from .pydantic_utils import json_schema_to_model
from langchain_core.tools import StructuredTool 
from composio.sdk import ComposioCore, App, Action
from typing import List
    
def ComposioTool(client : ComposioCore, action_schema: dict[str, any]) ->  StructuredTool:
    name = action_schema["name"]
    description = action_schema["description"]
    parameters = json_schema_to_model(action_schema["parameters"])
    appName = action_schema["appName"]
    print(parameters.schema())
    return StructuredTool.from_function(
        name=name,
        description=description,
        args_schema=parameters,
        return_schema=True,
        # TODO use execute action here
        func = lambda **kwargs: client.execute_action(client.get_action_enum(name, appName), kwargs)
    )

def ComposioToolset(tools: List[App] = [], actions: List[Action] = []) -> List[StructuredTool]:
    client = ComposioCore()
    actions_list = client.sdk.get_list_of_actions(tools, actions)
    return [ComposioTool(client, action) for action in actions_list]


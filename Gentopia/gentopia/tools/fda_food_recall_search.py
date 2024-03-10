from typing import AnyStr
from gentopia.tools.basetool import *
import requests
import json


class FDAFoodRecallArgs(BaseModel):
    query: str = Field(..., description="the state to search for recalls in. The format of the state must be in the two letter format. For example, MD for Maryland")


class FDAFoodRecallSearch(BaseTool):
    """Tool that adds the capability to search for food recalls from the FDA's database"""

    name = "fda_food_recall_search"
    description = ("Find information about food recalls in a particular US state"
                   "Input should be the state you would like to search in.")

    args_schema: Optional[Type[BaseModel]] = FDAFoodRecallArgs

    def _run(self, query: AnyStr) -> str:
        response = requests.get(f"https://api.fda.gov/food/enforcement.json?search=state:{query}&limit=5")
        return json.dumps(response.json())

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError


if __name__ == "__main__":
    ans = FDAFoodRecallSearch()._run("VA")
    print(ans)

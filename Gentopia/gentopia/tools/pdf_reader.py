from typing import AnyStr
from gentopia.tools.basetool import *
import requests
import io
import PyPDF2


class PdfReaderArgs(BaseModel):
    query: str = Field(..., description="the URL of the PDF")


class PdfReader(BaseTool):
    """Tool that adds the capability to read PDFs from the given URL"""

    name = "pdf_read"
    description = ("Read the information contained within a PDF by providing the URL that it is hosted at."
                   "Input should be the URL of the PDF you want to read.")

    args_schema: Optional[Type[BaseModel]] = PdfReaderArgs

    def _run(self, query: AnyStr) -> str:
        response = requests.get(query)
        f = io.BytesIO(response.content)
        reader = PyPDF2.PdfReader(f)
        return "".join([page.extract_text() for page in reader.pages[:3]])

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError


if __name__ == "__main__":
    ans = PdfReader()._run("https://openreview.net/pdf?id=h1nUUpmvpf")
    print(ans)

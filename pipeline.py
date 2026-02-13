from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import PydanticOutputParser

from schemas import SupportTicket
from prompts import template

from dotenv import load_dotenv

load_dotenv()


parser = PydanticOutputParser(pydantic_object=SupportTicket)

llm = HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.2',
    temperature=0.0,
    max_new_tokens=256,
)

model = ChatHuggingFace(llm=llm)

template = template.partial(
    format_instructions=parser.get_format_instructions()
)

# print(template)

chain = template | model | parser

def output(email: str) -> SupportTicket:
    return chain.invoke({'email': email})

# print(output('Hi, I was charged twice for my last invoice. Please help to fix this.'))

'''

ticket = output('Hi, I was charged twice for my last invoice. Please help to fix this.')
print(ticket.dict())
print(ticket.json())

'''
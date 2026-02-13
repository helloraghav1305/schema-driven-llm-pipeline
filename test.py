from schemas import SupportTicket
from prompts import template
from langchain_core.messages import HumanMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# Testing schemas.py
data = {
    'issue_type': 'billing',
    'summary': 'Customer was charged twice',
    'priority': 'urgent', # try an invalid case like 'urgent'
    'action_required': True,
    'confidence': 0.95
}

ticket = SupportTicket(**data)
# print(ticket)


# Testing prompts.py
prompt = template.invoke({'email': 'Hi, my account is locked after I tried to reset my password. Please help.'})


model = ChatHuggingFace(
    llm=HuggingFaceEndpoint(
        repo_id='mistralai/Mistral-7B-Instruct-v0.2',
        temperature=0.0
    )
)

response = model.invoke(prompt)

print(response.content)




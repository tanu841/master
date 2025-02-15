import openai
from fastapi import FastAPI,Form,Request
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app=FastAPI()
templates = Jinja2Templates(directory="templates")
openai=OpenAI(
    api_key="sk-xxxxxx", # get your own key form the openai website and don't share it
)

@app.get("/",response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("chat.html",{"request":request})

chat_log=[{
    'role': 'system',
    'content': 'You are a python tutor AI,completely dedicated to teach users how to learn \
               Python from scratch. Please provide clear instructions on the Python concepts,\
               best practices, and coding examples to help users learn Python effectively.'
}]
chat_responses=[]

@app.post("/",response_class=HTMLResponse)
async def chat(request:Request,user_input:Annotated[str,Form()]):
    chat_log.append({'role':'user','content':user_input})
    chat_responses.append(user_input)

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=chat_log,
    temperature=0.6
    )
    bot_response = response['choices'][0]['message']['content']
    chat_log.append({'role':'assistant','content':bot_response})
    chat_responses.append(bot_response)
    return templates.TemplateResponse("home.html",{"request":request, " chat_responses":chat_responses})

# Output
#% python3 main.py
#ChatCompletion (id='chatcmpl-9gF15VWOLOzf00RsfNxTaMNkuOLCO',
# choices=[Choice (finish_reason='stop', index=0, Logprob s=None,
# message=ChatCompletionMessage (content='How can I assist you today?', role='assistant', function_call=None, tool_calls=None))],
# created=1719854527, model='gpt-3.5-turbo-0125', object='chat.completion', service_tier=None, system_fingerprint=None,
# usage=CompletionUsage (completion_tokens=7, prompt_tokens=13, total_tokens=20))

#Output1
#% pythons main.py
#ChatCompletion(id='chatcmpl-9gF2gVNx7u6C21Mu@Rx5HGLpFf0sd',
# choices=[Choice (finish_reason='stop', index=0, logprob s=None,
# message=ChatCompletionMessage (content='The San Antonio Spurs won the NBA championship in 2005.', role='assistant', function_call=None, tool_calls=None))],
# created=1719854626, model='gpt-3.5-turbo-0125', object='chat.comp letion', service_tier=None, system_fingerprint=None,
# usage=CompletionUsage (completion_tokens=13, prompt_tokens=27,

#Output2
#content": "The 2005 San Antonio Spurs team that won the NBA championship consisted of the following players: \n\n1. Tim Duncan\n2. M anu Ginobili\n3. Tony Parker\n4. Bruce Bowen\n5. Robert Horry\n6. Mikael Finley\n7. Devin Brown\n8. Brent Barry \n9. Nazr Mohammed\n10. Rash Nesterovi\u0107\n11. Hedo T\u00fcrko\u011flu\n12. Beno Udrih\n13. Melvin Ely\n14. Charles Smith\n15. Sean Marks\n\n The team was coached by Gregg Popovich."

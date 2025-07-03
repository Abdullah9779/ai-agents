from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wikipedia_tool

load_dotenv()

llm = ChatGroq(model="deepseek-r1-distill-llama-70b", )

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are helpfull ai agent assistant."),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}")
])

chat_history = []

tools = [search_tool, wikipedia_tool]

agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=False, # If want to check thinking/backend processing make it verbose=True.
)

if __name__ == "__main__":
    while True:
        user_input = input("You : ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        if user_input:
            chat_history.append({"role": "user", "content": user_input})
            ai_response = agent_executor.invoke({
                "query": user_input,
                "chat_history": chat_history
            })
            chat_history.append({"role": "assistant", "content": ai_response['output']})
            print(f"\n\n--------------------\n\nBot : {ai_response['output']}\n\n--------------------\n\n")

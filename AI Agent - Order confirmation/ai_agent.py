from mytools import get_order_status
from groq import Groq
import json
import re

client = Groq(api_key="your_api_key_here")

system_command = """
You are an AI chating agent with access to tools. Always reply in valid JSON format as described below.

Your task:
- Help the user confirm their order using a 6-digit order number.
- If the user gives anything other than a 6-digit number, reply: "Invalid or missing order number. Please provide a 6-digit order number."
- If the user gives a 6-digit number (e.g. 298383), immediately call the tool `get_order_status` with that number. Do NOT assume whether the number is valid or not — let the tool decide.
- If the user says "order is complete", "thank you", or "bye", you may call `end_chat`.
- If the user asks questions NOT related to an order number, say: "I can only help you with order confirmation. Please provide your 6-digit order number."

Tool Functions:
1. get_order_status(order_number:int) --> get_order_status
2. end_chat() --> end_chat — use it to end chat once order is complete or user says goodbye.

Output format (ALWAYS use this JSON format):

{
  "ai_response": "Your response to user here",
  "tool": "tool name here if any (get_order_status or end_chat), otherwise null",
  "order_number": 6-digit number if provided, otherwise null
}

If you are responding to a tool output, you will receive the following input:
{
  "user_response": "null",
  "tool": "tool name",
  "tool_output": "tool result string"
}

In that case, reply with the status or summary from the tool output, still using the same JSON output format above.
"""

messages = [{"role": "system", "content": system_command}]

def clean_response(text):
    return re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.MULTILINE).strip()

def get_ai_response():
    try:
        completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=messages,
            temperature=0.7,
            max_completion_tokens=1024,
            top_p=1
        )
        response_text = completion.choices[0].message.content
        print(f"[DEBUG] Raw AI Response:\n{response_text}")

        cleaned = clean_response(response_text)
        return json.loads(cleaned)

    except json.JSONDecodeError:
        return {
            "ai_response": "Sorry, I received an invalid response format.",
            "tool": None,
            "order_number": None
        }
    except Exception as e:
        return {
            "ai_response": f"An error occurred: {e}",
            "tool": None,
            "order_number": None
        }

def inject_tool_output(tool_name, output):
    formatted = json.dumps({
        "user_response": "null",
        "tool": tool_name,
        "tool_output": output
    })
    messages.append({"role": "user", "content": formatted})

def chat():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chat ended.")
            break

        messages.append({"role": "user", "content": user_input})
        ai_response = get_ai_response()
        messages.append({"role": "assistant", "content": json.dumps(ai_response)})

        print(f"AI: {ai_response['ai_response']}")

        if ai_response["tool"] == "get_order_status" and ai_response["order_number"]:
            try:
                tool_result = get_order_status(ai_response["order_number"])
            except Exception as e:
                tool_result = f"Error: {e}"

            inject_tool_output("get_order_status", tool_result)
            tool_ai_response = get_ai_response()
            messages.append({"role": "assistant", "content": json.dumps(tool_ai_response)})
            print(f"AI: {tool_ai_response['ai_response']}")

        elif ai_response["tool"] == "end_chat":
            print("The chat has been closed.")
            break

if __name__ == "__main__":
    chat()

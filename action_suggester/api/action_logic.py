import google.generativeai as genai
import json

API_KEY = "AIzaSyCWyFSIjDbGjF3dJC-bk1ZkOYL3gCd-G0c"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

def analyze_message(query):
    prompt = (
        f'Analyze the following user message: "{query}".\n'
        'Return ONLY a valid JSON object like this:\n'
        '{"tone": "Happy", "intent": "Order Food"}\n'
        'Do not include any explanation, markdown, or extra text.'
    )

    try:
        response = model.generate_content(prompt)
        content = response.text.strip()

        # Clean Gemini markdown formatting if present
        if content.startswith("```json"):
            content = content.replace("```json", "").replace("```", "").strip()

        print("=== Gemini Raw Response ===")
        print(content)

        data = json.loads(content)
        return {
            "tone": data.get("tone", "Unknown"),
            "intent": data.get("intent", "Unknown")
        }
    except Exception as e:
        print("Error parsing Gemini response:", e)
        return {"tone": "Unknown", "intent": "Unknown"}


 # def suggest_actions(tone, intent):
 #    actions = {
 #        "ORDER_FOOD": "Order Food Online",
 #        "FIND_RECIPE": "Find Pizza Recipes",
 #        "ASK_HELP": "Ask for Help",
 #        "SHARE_NEWS": "Share Latest News"
 #    }

 #    suggestions = []
 #    if intent == "Order Food":
 #        suggestions.append({"action_code": "ORDER_FOOD", "display_text": actions["ORDER_FOOD"]})
 #    if "recipe" in tone.lower() or intent == "Find Recipe":
 #        suggestions.append({"action_code": "FIND_RECIPE", "display_text": actions["FIND_RECIPE"]})
 #    if tone == "Urgent":
 #        suggestions.append({"action_code": "ASK_HELP", "display_text": actions["ASK_HELP"]})
 #    if tone == "Happy":
 #        suggestions.append({"action_code": "SHARE_NEWS", "display_text": actions["SHARE_NEWS"]})

 #    return suggestions[:3]

def suggest_actions(tone, intent):
    actions = {
        "ORDER_FOOD": "Order Food Online",
        "FIND_RECIPE": "Find Pizza Recipes",
        "ASK_HELP": "Ask for Help",
        "SHARE_NEWS": "Share Latest News"
    }

    suggestions = []
    intent = intent.lower()
    tone = tone.lower()

    if "order" in intent or "food" in intent:
        suggestions.append({"action_code": "ORDER_FOOD", "display_text": actions["ORDER_FOOD"]})
    
    if "recipe" in intent or "cook" in intent:
        suggestions.append({"action_code": "FIND_RECIPE", "display_text": actions["FIND_RECIPE"]})
    
    if "help" in intent or tone == "urgent":
        suggestions.append({"action_code": "ASK_HELP", "display_text": actions["ASK_HELP"]})
    
    if "news" in intent or "information" in intent or "share" in intent or tone == "happy":
        suggestions.append({"action_code": "SHARE_NEWS", "display_text": actions["SHARE_NEWS"]})

    return suggestions[:3]

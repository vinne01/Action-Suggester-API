Here's the README content formatted in proper markdown:

```markdown
# Action Suggester API

This project is a simple Django-based API that uses an external AI (LLM, such as Gemini API) to analyze the tone and intent of a user's message and suggests relevant actions. The results, including the query, tone, intent, and suggested actions, are logged to a PostgreSQL database.

## 🚀 Features
- **POST /api/analyze/**: Accepts a user message and returns an analysis of the tone and intent along with suggested actions
- **LLM Integration**: Uses Gemini (or another LLM) API to identify tone and intent
- **Database Logging**: Logs each request's details to a PostgreSQL database
- **Action Suggestions**: Based on the tone and intent, the API suggests up to 3 predefined actions

## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/your-repository-name/action-suggester-api.git
cd action-suggester-api
```
     **Architecture of Projects **
  graph TD
    A[User Query] --> B[/api/analyze POST]
    B --> C[Gemini API<br><i>Prompted for tone & intent</i>]
    C --> D[Tone & Intent Identified]
    D --> E[suggest_actions(tone, intent)]
    E --> F[Suggested Actions]
    F --> G[QueryLog Model<br><i>Log to DB</i>]
    G --> H[JSON Response to User]
2. **Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure PostgreSQL Database**  
Make sure you have PostgreSQL installed and a database created. Update your `settings.py` in the project with the database credentials:

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

5. **Configure LLM API Key**  
To connect to the Gemini API (or any other LLM), add the API key in `action_logic.py`:

```python
# action_logic.py
import google.generativeai as genai

API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")
```

6. **Run Migrations**  
Create the necessary database tables:
```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Start the Django Development Server**
```bash
python manage.py runserver
```
Now your API is accessible at `http://localhost:8000/`

## 📡 API Endpoint

**POST /api/analyze/**  
Request:
```json
{
    "query": "Your message here"
}
```

Example:
```json
{
    "query": "I want to order pizza tonight!"
}
```

Response:
```json
{
    "id": 1,
    "query": "I want to order pizza tonight!",
    "tone": "Happy",
    "intent": "Order Food",
    "suggested_actions": [
        {
            "action_code": "ORDER_FOOD",
            "display_text": "Order Food Online"
        },
        {
            "action_code": "SHARE_NEWS",
            "display_text": "Share Latest News"
        }
    ],
    "created_at": "2025-04-18T10:43:33.123Z"
}
```

Error Response (if no query is provided):
```json
{
    "error": "Query field is required"
}
```

## 🧪 Testing with Postman
1. Open Postman
2. Set the method to **POST**
3. Set the URL to `http://localhost:8000/api/analyze/`
4. In the Body tab, choose `raw` and select JSON format
5. Enter a query in the JSON format:
```json
{
    "query": "I want to order pizza tonight!"
}
```
6. Send the request and check the response in the body section

## 📚 Code Structure
- **action_logic.py**: Contains functions for analyzing the message, identifying tone and intent, and suggesting actions
- **models.py**: Defines the database model for logging queries and actions
- **serializers.py**: Contains the serializer for the QueryLog model, ensuring the correct output structure
- **views.py**: Defines the APIView that handles the /api/analyze/ endpoint
- **urls.py**: Routes the /api/analyze/ request to the correct view
- **settings.py**: Django project configuration, including database and installed apps

## 🛠️ Dependencies
- Django: Web framework
- Django REST Framework (DRF): For creating REST APIs
- google-generativeai: For interacting with the Gemini API
- psycopg2: PostgreSQL database adapter for Python
- python-dotenv (optional, for API key management via .env)

## 🎉 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## 🚀 Troubleshooting
- Make sure your PostgreSQL database is running and correctly configured in `settings.py`
- If you're having issues with the Gemini API, check if your API key is valid and the rate limits are not exceeded
```

This formatting uses proper markdown syntax with:
- Headers using `#` symbols
- Code blocks wrapped in triple backticks with language specifications
- Organized sections with clear hierarchy
- Proper list formatting
- JSON examples with syntax highlighting
- Consistent spacing and indentation
- Emoji decorations for visual clarity

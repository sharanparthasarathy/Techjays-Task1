# 🤖 Django Groq AI Chat

A ChatGPT-style AI chat application built with **Django** and the **Groq API**.
The application supports user authentication, multiple chat threads, persistent conversation history, and AI-generated responses using Groq's LLMs.

## 🚀 Features

* 🔐 User Signup & Login
* 🚪 Logout functionality
* 💬 ChatGPT-style chat interface
* 🧵 Multiple chat threads
* 💾 Persistent chat history
* 🔄 Continue previous conversations
* 🤖 AI responses powered by Groq
* 📝 Markdown-formatted AI responses
* 📊 Markdown tables
* 💻 Code block formatting
* 📱 Responsive chat interface
* 👤 User-specific chat history
* 🔒 Users can only access their own conversations
* ⚙️ Environment variable support for API keys

## 🛠️ Tech Stack

### Backend

* Python
* Django
* Django Authentication
* SQLite

### AI

* Groq API
* OpenAI GPT-OSS model through Groq

### Frontend

* HTML5
* CSS3
* JavaScript
* Django Templates
* Markdown

### Development Tools

* Python Virtual Environment
* Git & GitHub
* python-dotenv

## 📂 Project Structure

```text
django-groq-chat/
│
├── chat/
│   ├── migrations/
│   ├── templates/
│   │   └── chat/
│   │       ├── signup.html
│   │       ├── login.html
│   │       ├── chat.html
│   │       └── chat_thread.html
│   │
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   └── urls.py
│
├── .env
├── .gitignore
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

> `.env`, `db.sqlite3`, and the virtual environment should not be committed to GitHub.

## 🗄️ Database Models

The application uses two main models.

### ChatThread

Stores individual conversations.

```text
ChatThread
├── user
├── title
├── created_at
└── updated_at
```

### Message

Stores individual messages inside a conversation.

```text
Message
├── thread
├── role
├── content
└── created_at
```

The `role` field identifies whether a message was sent by:

```text
user
assistant
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-120b
```

**Never upload your actual API key to GitHub.**

Make sure `.env` is included in `.gitignore`:

```gitignore
venv/
.env
__pycache__/
*.pyc
db.sqlite3
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/django-groq-chat.git
```

Move into the project:

```bash
cd django-groq-chat
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create `.env`

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-120b
```

### 6. Run migrations

```bash
python manage.py migrate
```

### 7. Create an admin account

```bash
python manage.py createsuperuser
```

### 8. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## 💬 How It Works

The application follows this flow:

```text
User
 │
 ▼
Login / Signup
 │
 ▼
Create Chat Thread
 │
 ▼
Send Message
 │
 ▼
Save User Message
 │
 ▼
Retrieve Previous Messages
 │
 ▼
Send Conversation to Groq API
 │
 ▼
Receive AI Response
 │
 ▼
Save AI Response
 │
 ▼
Display Formatted Response
```

This allows the AI to maintain context within each conversation.

## 🔐 Authentication

Django's built-in authentication system is used for:

* User registration
* Login
* Logout
* Session management
* Protecting chat pages

Users can only access conversations belonging to their own account.

## 🧠 Conversation Memory

Each conversation is stored as a separate `ChatThread`.

Messages are stored in the `Message` table and sent to the Groq API as conversation context.

Example:

```text
System
  ↓
You are a helpful AI assistant.

User
  ↓
What is Django?

Assistant
  ↓
Django is a Python web framework...

User
  ↓
What are its advantages?

Assistant
  ↓
Django provides...
```

This enables follow-up questions without losing the conversation context.

## 📝 Markdown Support

AI responses can contain Markdown such as:

```markdown
# Django

**Django** is a Python web framework.

### Features

- Authentication
- ORM
- Admin panel
- URL routing
```

The application converts Markdown into HTML before displaying the response.

It also supports:

* Headings
* Bold and italic text
* Lists
* Tables
* Code blocks
* Line breaks
* Blockquotes

## 🔮 Future Improvements

Planned improvements include:

* [ ] Automatic chat title generation
* [ ] Delete conversations
* [ ] Rename conversations
* [ ] Search chat history
* [ ] Loading animation
* [ ] Stop generating button
* [ ] Streaming AI responses
* [ ] Message regeneration
* [ ] Copy response button
* [ ] Code syntax highlighting
* [ ] Dark/Light mode
* [ ] PostgreSQL database
* [ ] Docker support
* [ ] Production deployment
* [ ] AI conversation summarization
* [ ] File upload support
* [ ] Image understanding
* [ ] Voice input

## 🎯 Learning Objectives

This project was developed to practice:

* Django fundamentals
* Django authentication
* Django ORM
* Database relationships
* CRUD operations
* REST/API integration
* Environment variables
* LLM API integration
* Prompt and conversation management
* Server-side rendering
* Markdown rendering
* Git & GitHub

## 📸 Screenshots

Add screenshots of your application here after uploading them to your repository.

Example:

```markdown
![Login Page](screenshots/login.png)

![Chat Interface](screenshots/chat.png)

![Chat History](screenshots/history.png)
```

## 👨‍💻 Author

**Sharan Parthasarathy**

AI & Data Science Graduate | Python | Django | Machine Learning | AI

GitHub:
`https://github.com/YOUR_USERNAME`

Portfolio:
`https://sharan-codes.vercel.app/`

## 📄 License

This project is created for educational and development purposes.

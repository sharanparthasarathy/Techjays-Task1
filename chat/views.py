from django.shortcuts import render

import markdown

from .models import ChatThread, Message
from django.contrib.auth.decorators import login_required

from groq import Groq
from django.conf import settings

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

groq_client = Groq(
    api_key=settings.GROQ_API_KEY
)

@login_required
def chat_view(request):

    threads = request.user.chat_threads.all()

    return render(
        request,
        "chat/chat.html",
        {
            "threads": threads
        }
    )

@login_required
def new_chat(request):
    thread = ChatThread.objects.create(
        user=request.user,
        title="New Chat"
    )

    return redirect("chat_thread", thread_id=thread.id)

@login_required
def chat_thread(request, thread_id):

    thread = ChatThread.objects.get(
        id=thread_id,
        user=request.user
    )

    if request.method == "POST":

        user_message = request.POST.get("message", "").strip()

        if user_message:

            # 1. Save user's message
            Message.objects.create(
                thread=thread,
                role="user",
                content=user_message
            )

            # 2. Get previous conversation
            previous_messages = thread.messages.all().order_by(
                "created_at"
            )

            # 3. Convert database messages to Groq format
            groq_messages = [
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant."
                }
            ]

            for message in previous_messages:

                groq_messages.append({
                    "role": message.role,
                    "content": message.content
                })

            # 4. Send conversation to Groq
            response = groq_client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=groq_messages
            )

            # 5. Get AI response
            ai_response = response.choices[0].message.content

            # 6. Save AI response
            Message.objects.create(
                thread=thread,
                role="assistant",
                content=ai_response
            )

        return redirect(
            "chat_thread",
            thread_id=thread.id
        )

    chat_messages = thread.messages.all().order_by(
        "created_at"
    )

    for message in chat_messages:

        if message.role == "assistant":

            message.formatted_content = markdown.markdown(
                message.content,
                extensions=[
                    "tables",
                    "fenced_code",
                    "nl2br",
                ]
            )

        else:

            message.formatted_content = message.content

    return render(
        request,
        "chat/chat_thread.html",
        {
            "thread": thread,
            "messages": chat_messages
        }
    )

def signup_view(request):

    if request.user.is_authenticated:
        return redirect("chat")


    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)

        return redirect("chat")

    return render(request, "chat/signup.html")


def login_view(request):

    if request.user.is_authenticated:
        return redirect("chat")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("chat")

        else:

            messages.error(
                request,
                "Invalid username or password"
            )

    return render(request, "chat/login.html")

def logout_view(request):

    logout(request)

    return redirect("login")
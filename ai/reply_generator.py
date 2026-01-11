import random
import json

def generate_reply(comment_text):
    responses = [
        f"Thank you for your question! We would be happy to assist you regarding: {comment_text}",
        f"We appreciate your interest. Regarding '{comment_text}', our team will guide you shortly.",
        f"Thanks for reaching out! Here's some information related to your comment: {comment_text}"
    ]
    return random.choice(responses)

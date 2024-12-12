from collections import Counter
import matplotlib.pyplot as plt
import re
import json
from datetime import datetime


class conversation:
    def __init__(self, title, userMessages, GPTMessages, timestamp, totalConversation):
        self.title = title
        self.userMessages = userMessages
        self.GPTMessages = GPTMessages
        self.timestamp = timestamp
        self.totalConversation = totalConversation


with open("ChatGPT Data\conversations.json", "r") as file:
    dataFile = json.load(file)

conversations = []

for obj in dataFile:

    # Get the title of the conversation

    conversationTime = obj.get("create_time")
    conversationTitle = obj.get("title")
    conversationUserMessages = []
    conversationGPTMessages = []
    totalConversation = []

    mappings = obj.get("mapping", {})
    for mapping_id, mapping_obj in mappings.items():
        # Check if "message" exists and is not None
        message_obj = mapping_obj.get("message")
        if message_obj and "content" in message_obj:
            message_author = message_obj["author"].get("role")
            message_parts = message_obj["content"].get("parts", [])
            if message_parts:
                content = message_parts[-1]
                totalConversation.append(content)
                if message_author == "assistant":
                    conversationGPTMessages.append(content)
                elif message_author == "user":
                    conversationUserMessages.append(content)  # Add content to myMessages
            # else:
            # myMessages.append("No content in parts.")
        # else:

        # myMessages.append(f"No message content for mapping_id: {mapping_id}")
    conversations.append(conversation(conversationTitle, conversationUserMessages, conversationGPTMessages, datetime.fromtimestamp(conversationTime), totalConversation))

# Print the messages to verify
for i in conversations:
    print(i.userMessages)

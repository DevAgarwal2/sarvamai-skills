# Sarvam AI Chat Completion Skill Template

## Overview
This template helps you create skills that use Sarvam AI's chat completion API for conversational AI, text generation, and intelligent responses.

## API Information

**Endpoint:** `https://api.sarvam.ai/v1/chat/completions`  
**Method:** POST  
**Authentication:** Bearer token in Authorization header

## Available Models

| Model | Parameters | Description | Use Case |
|-------|-----------|-------------|----------|
| sarvam-m | 24B | Production-ready chat model | General conversation, Q&A, content generation, reasoning tasks |

**Note:** sarvam-m is currently the only available chat model in the API.

## Request Parameters

| Parameter | Type | Required | Default | Range | Description |
|-----------|------|----------|---------|-------|-------------|
| messages | Array | Yes | - | - | List of conversation messages |
| model | String | No | sarvam-m | - | Model to use (only sarvam-m available) |
| temperature | Float | No | 0.7 | 0.0-2.0 | Sampling temperature |
| max_tokens | Integer | No | 1024 | 1-4096 | Maximum tokens to generate |
| top_p | Float | No | 0.9 | 0.0-1.0 | Nucleus sampling parameter |
| frequency_penalty | Float | No | 0.0 | -2.0-2.0 | Penalty for token frequency |
| presence_penalty | Float | No | 0.0 | -2.0-2.0 | Penalty for token presence |
| stream | Boolean | No | false | - | Enable streaming responses |

## Message Format

```json
{
  "messages": [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Hello!"},
    {"role": "assistant", "content": "Hi! How can I help you?"},
    {"role": "user", "content": "What is AI?"}
  ]
}
```

## Response Format

```json
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "sarvam-m",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "AI stands for Artificial Intelligence..."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 20,
    "completion_tokens": 50,
    "total_tokens": 70
  }
}
```

## Python Example

```python
from sarvamai import SarvamAI
import os

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)

response = client.chat.completions(
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "What is the capital of India?"}
    ],
    model="sarvam-m",
    temperature=0.7,
    max_tokens=512
)

print(response.choices[0].message.content)
```

## cURL Example

```bash
curl -X POST https://api.sarvam.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_SARVAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sarvam-m",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ]
  }'
```

## Message Roles

### System
Sets the behavior and context for the assistant:
```python
{"role": "system", "content": "You are an expert in Indian history"}
```

### User
Represents user input:
```python
{"role": "user", "content": "Tell me about the Mughal Empire"}
```

### Assistant
Represents AI responses (for conversation history):
```python
{"role": "assistant", "content": "The Mughal Empire was..."}
```

## Use Cases

1. **Chatbots**: Customer support, virtual assistants
2. **Content Generation**: Articles, summaries, descriptions
3. **Question Answering**: Knowledge bases, FAQs
4. **Code Assistance**: Programming help, code generation
5. **Creative Writing**: Stories, poems, scripts
6. **Analysis**: Text analysis, sentiment analysis
7. **Education**: Tutoring, explanations, learning aids
8. **Translation Support**: Language understanding and translation

## Temperature Guide

| Temperature | Behavior | Use Case |
|-------------|----------|----------|
| 0.0-0.3 | Focused, deterministic | Facts, code, structured data |
| 0.4-0.7 | Balanced | General conversation, Q&A |
| 0.8-1.2 | Creative, diverse | Creative writing, brainstorming |
| 1.3-2.0 | Very random | Experimental, highly creative |

## Model Information

**sarvam-m** is a 24B parameter model optimized for:
- General conversation and dialogue
- Question answering and information retrieval
- Content generation (articles, summaries, descriptions)
- Code assistance and programming help
- Creative writing and brainstorming
- Text analysis and reasoning tasks

The model supports both English and multiple Indian languages, making it ideal for building multilingual applications.

## Best Practices

1. **System Prompts**: Always use system messages to set context
2. **Conversation History**: Include relevant previous messages
3. **Token Management**: Monitor token usage to control costs
4. **Temperature Tuning**: Adjust based on desired output style
5. **Error Handling**: Implement retry logic and fallbacks
6. **Prompt Engineering**: Craft clear, specific prompts
7. **Streaming**: Use streaming for real-time applications

## Prompt Engineering Tips

### Be Specific
```python
# Bad
{"role": "user", "content": "Tell me about India"}

# Good
{"role": "user", "content": "List the top 5 tourist destinations in India with brief descriptions"}
```

### Provide Context
```python
messages = [
    {"role": "system", "content": "You are a travel expert specializing in India"},
    {"role": "user", "content": "Recommend a 3-day itinerary for Delhi"}
]
```

### Use Examples
```python
{"role": "user", "content": """
Translate these phrases to Hindi:
Example: Hello -> नमस्ते
Your turn: Good morning
"""}
```

## Common Patterns

### Simple Q&A
```python
response = client.chat.completions(
    messages=[
        {"role": "user", "content": "What is 2+2?"}
    ],
    model="sarvam-m",
    temperature=0.2  # Low temp for factual
)
```

### Multi-turn Conversation
```python
conversation = []

# First exchange
conversation.append({"role": "user", "content": "Hi!"})
response = client.chat.completions(messages=conversation)
conversation.append({"role": "assistant", "content": response.choices[0].message.content})

# Second exchange
conversation.append({"role": "user", "content": "Tell me a joke"})
response = client.chat.completions(messages=conversation)
```

### Creative Writing
```python
response = client.chat.completions(
    messages=[
        {"role": "system", "content": "You are a creative writer"},
        {"role": "user", "content": "Write a short story about AI"}
    ],
    model="sarvam-m",
    temperature=0.9,  # High temp for creativity
    max_tokens=1024
)
```

## Common Errors

| Error | Solution |
|-------|----------|
| 401 Unauthorized | Check API key in Authorization header |
| 400 Bad Request | Verify message format and parameters |
| 429 Too Many Requests | Implement rate limiting |
| 500 Server Error | Retry with exponential backoff |

## Skill Template Structure

When creating a chat completion skill:

1. Define the assistant's role (system prompt)
2. Design the conversation flow
3. Handle multi-turn conversations
4. Manage conversation history
5. Implement token limits
6. Add error handling and retries
7. Include user feedback mechanisms

## Advanced Features

### Streaming Responses
```python
response = client.chat.completions(
    messages=[
        {"role": "user", "content": "Write a long essay"}
    ],
    stream=True
)

for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end='')
```

### Token Counting
```python
response = client.chat.completions(
    messages=messages,
    model="sarvam-m"
)

print(f"Tokens used: {response.usage.total_tokens}")
print(f"Prompt: {response.usage.prompt_tokens}")
print(f"Completion: {response.usage.completion_tokens}")
```

### Conversation Management
```python
class ConversationManager:
    def __init__(self, max_history=10):
        self.messages = []
        self.max_history = max_history
    
    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})
        # Keep only recent messages
        if len(self.messages) > self.max_history:
            self.messages = self.messages[-self.max_history:]
    
    def get_response(self, user_input):
        self.add_message("user", user_input)
        response = client.chat.completions(messages=self.messages)
        assistant_message = response.choices[0].message.content
        self.add_message("assistant", assistant_message)
        return assistant_message
```

## Integration with Other APIs

### Multilingual Chatbot
```python
# 1. Translate user input to English
translation = client.text.translate(
    input=user_input_hindi,
    source_language_code="hi-IN",
    target_language_code="en-IN"
)

# 2. Get chat response
chat_response = client.chat.completions(
    messages=[{"role": "user", "content": translation.translated_text}]
)

# 3. Translate back to Hindi
final_response = client.text.translate(
    input=chat_response.choices[0].message.content,
    source_language_code="en-IN",
    target_language_code="hi-IN"
)
```

## Related APIs

- **Text Translation**: Create multilingual chatbots
- **Text to Speech**: Convert responses to audio
- **Speech to Text**: Voice-based chat interfaces

## Resources

- [API Documentation](https://docs.sarvam.ai/api-reference-docs/endpoints/chat)
- [Prompt Engineering Guide](https://docs.sarvam.ai/prompting)
- [Python SDK](https://pypi.org/project/sarvamai/)
- [Dashboard](https://dashboard.sarvam.ai)

"""
Sarvam AI - Chat Completion
----------------------------
This example demonstrates how to use Sarvam AI's chat completion API
for conversational AI and text generation tasks.

Uses the default sarvam-m model (24B parameter production-ready chat model)
"""

import os
from sarvamai import SarvamAI

def chat_completion(
    messages: list,
    temperature: float = 0.7,
    max_tokens: int = 1024,
    top_p: float = 0.9,
    frequency_penalty: float = 0.0,
    presence_penalty: float = 0.0,
    stream: bool = False
):
    """
    Generate chat completions using Sarvam AI.
    
    Args:
        messages: List of message dictionaries with 'role' and 'content'
        temperature: Sampling temperature (0.0 to 2.0)
        max_tokens: Maximum tokens to generate
        top_p: Nucleus sampling parameter
        frequency_penalty: Penalty for token frequency
        presence_penalty: Penalty for token presence
        stream: Enable streaming responses
    
    Returns:
        Chat completion response object
    """
    # Initialize the client with API key from environment
    client = SarvamAI(
        api_subscription_key=os.getenv("SARVAM_API_KEY")
    )
    
    # Generate chat completion
    response = client.chat.completions(
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stream=stream
    )
    
    return response


def main():
    """Example usage of chat completion API."""
    
    # Example 1: Simple question answering
    print("=" * 50)
    print("Example 1: Simple Q&A")
    print("=" * 50)
    
    messages = [
        {"role": "user", "content": "What is the capital of India?"}
    ]
    
    try:
        response = chat_completion(messages)
        print(f"User: {messages[0]['content']}")
        print(f"Assistant: {response.choices[0].message.content}")
        print(f"\nTokens used: {response.usage.total_tokens}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: Multi-turn conversation
    print("\n" + "=" * 50)
    print("Example 2: Multi-turn Conversation")
    print("=" * 50)
    
    conversation = [
        {"role": "user", "content": "Can you explain what AI is?"},
        {"role": "assistant", "content": "AI (Artificial Intelligence) refers to computer systems that can perform tasks that typically require human intelligence, such as learning, reasoning, problem-solving, and understanding language."},
        {"role": "user", "content": "What are some common applications of AI?"}
    ]
    
    try:
        response = chat_completion(conversation)
        print("Conversation history:")
        for msg in conversation[:-1]:
            print(f"{msg['role'].capitalize()}: {msg['content']}\n")
        print(f"User: {conversation[-1]['content']}")
        print(f"Assistant: {response.choices[0].message.content}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 3: Creative writing with high temperature
    print("\n" + "=" * 50)
    print("Example 3: Creative Writing")
    print("=" * 50)
    
    messages = [
        {
            "role": "user",
            "content": "Write a short poem about artificial intelligence and the future of India"
        }
    ]
    
    try:
        response = chat_completion(
            messages,
            temperature=0.9,  # Higher temperature for creativity
            max_tokens=256
        )
        print(f"User: {messages[0]['content']}\n")
        print(f"Assistant:\n{response.choices[0].message.content}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 4: Factual responses with low temperature
    print("\n" + "=" * 50)
    print("Example 4: Factual Information")
    print("=" * 50)
    
    messages = [
        {
            "role": "user",
            "content": "List the top 5 programming languages used in India in 2024"
        }
    ]
    
    try:
        response = chat_completion(
            messages,
            temperature=0.2,  # Lower temperature for factual responses
            max_tokens=512
        )
        print(f"User: {messages[0]['content']}\n")
        print(f"Assistant:\n{response.choices[0].message.content}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 5: System prompt with role guidance
    print("\n" + "=" * 50)
    print("Example 5: With System Prompt")
    print("=" * 50)
    
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant specializing in Indian languages and culture. Respond concisely and accurately."
        },
        {
            "role": "user",
            "content": "What are the official languages of India?"
        }
    ]
    
    try:
        response = chat_completion(
            messages,
            temperature=0.5
        )
        print(f"System: {messages[0]['content']}\n")
        print(f"User: {messages[1]['content']}\n")
        print(f"Assistant: {response.choices[0].message.content}")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

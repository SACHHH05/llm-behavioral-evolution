import ollama

MODEL_NAME = "qwen3:8b"

def main():
    print(f"Running model: {MODEL_NAME}")

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": (
                    "Explain what an AI language model is "
                    "in simple terms."
                ),
            }
        ],
        options={
            "temperature": 0.0,
            "num_predict": 128,
        },
    )

    print("\nMODEL RESPONSE")
    print("=" * 40)
    print(response["message"]["content"])


if __name__ == "__main__":
    main()

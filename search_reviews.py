import json
from vector import retriever

while True:
    question = input("\nAsk your question (q to quit): ")

    if question.lower() == "q":
        print("👋 Bye!")
        break

    print(f"\n🔍 Searching reviews for: '{question}'")
    reviews = retriever.invoke(question)
    print(f"📚 Found {len(reviews)} relevant reviews")

    review_data = []
    for review in reviews:
        review_data.append(
            {
                "review_id": review.id,
                "content": review.page_content,
                "rating": review.metadata.get("rating", "N/A"),
                "date": review.metadata.get("date", "N/A"),
            }
        )

    # Print results
    print(review_data)

    # Save to JSON
    output = {
        "question": question,
        "results_count": len(review_data),
        "reviews": review_data
    }

    with open("search_results.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print("✅ Results saved to search_results.json")

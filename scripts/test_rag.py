from app.services.recommendation_service import recommend

def main():

    while True:
        query = input(
            "Ask Weeber: "
        )

        if query.strip().lower() == "exit":
            print("Sayōnara. Goodbye!")
            break

        result = recommend(query)

        print("\n\nANSWER:")
        print(
            result["answer"]
        )

        print("\n\nSOURCES:")

        for anime in result["sources"]:
            print(
                "-",
                anime["title"]
            )

if __name__ == "__main__":
    main()
from dotenv import load_dotenv
from talk_to_google_sheets import TalkToGoogleSheets
from talk_to_openai import fetch_openai_response


def run():
    load_dotenv()
    sheet_client = TalkToGoogleSheets()
    data = sheet_client.get_all_data()

    print("Welcome to Money Boy!")
    print("Type your queries below (type 'exit' to quit).")

    while True:
        user_query = input("\nYour query: ")
        if user_query.strip().lower() == "exit":
            print("Goodbye!")
            break

        try:
            response = fetch_openai_response(data, user_query)
            print("\nAssistant Response:")
            print(response)
        except Exception as e:
            print(f"An error occurred: {e}")



if __name__ == "__main__":
    run()

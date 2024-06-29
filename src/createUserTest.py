from pprint import pprint
import random, requests


def createUserID():
    # Generate a random number for the userID
    random_number = random.randint(10000000, 99999999)
    userID = str(random_number)

    # Prepare the data payload for creating a record
    # data_payload = {"records": [{"fields": {"UserID": userID}}]}

    # url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{TABLE_NAME_USERINFO}"
    # headers = {
    #     "Authorization": f"Bearer {AIRTABLE_API_KEY}",
    #     "Content-Type": "application/json"
    # }

    from lib.supabase_client import SupabaseClient
    from repositories import UserRepository

    # supabase = SupabaseClient(url=os.environ[SUPABASE_URL], key=os.environ[SUPABASE_KEY])
    supabase = SupabaseClient(
        url="https://tomwaurajyktcauvdyvc.supabase.co",
        key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRvbXdhdXJhanlrdGNhdXZkeXZjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTcxNDQzMzQsImV4cCI6MjAzMjcyMDMzNH0.i1DGhf5zI6XmMefERJ8V9pmC_r9jMNd6l5VvYixgLDo",
    )
    user_repository = UserRepository(supabase)
    try:
        user = user_repository.create_user(user_data={"user_id"})
        # Sending the POST request to Airtable
        # response = requests.post(url, headers=headers, json=data_payload)
        # response.raise_for_status()  # Raises an exception for 4XX/5XX errors
        # data = response.json()
        # userID = data['records'][0]['fields']['UserID']
        userID_status = "New"
        # On success, parse and return the response
        return {
            "message": "Record created successfully.",
            "details": user,
            "userID": userID,
            "userID_status": userID_status,
        }
    except Exception as e:
        # Return detailed error information in case of failure
        return {
            "error": f"Airtable API request failed: {str(e)}",
            # "details": response.text if response else "No response"
        }


if __name__ == "__main__":
    pprint(createUserID(), indent=4)

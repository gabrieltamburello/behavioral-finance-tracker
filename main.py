import sqlite3

# functions to add daily entries
def add_daily_entries():
    connect_DB_DE = sqlite3.connect("tracker.db")
    cursor_DE = connect_DB_DE.cursor()
    
    # date input
    date_DE = input("Enter the date (YYYY-MM-DD): ")
    
    # input validation for date input
    


    allowed_market_moods = ["Bullish", "Bearish", "Neutral"]
    
    # This variable will store the final, validated mood or indicate an exit
    overall_market_mood_DE = "" # Initialize it
    
    # input validation for overall market mood input
    while True:
        # overall market mood input
        user_input_mood = input("Enter the market mood (Bullish/Bearish/Neutral) or type 'exit' to cancel: ")
        
        # check if user wants to exit
        if user_input_mood.lower() == "exit":
            print("Cancelling market mood entry.")
            break   # exits the while True loop
        
        # convert to title case
        normalized_market_moods = user_input_mood.title()
        if normalized_market_moods in allowed_market_moods:
            overall_market_mood_DE = normalized_market_moods    # store valid market mood
            break
        else:
            print("Must enter the market mood (Bullish/Bearish/Neutral). Please try again: ")   # loop will repeat until exited or proper input
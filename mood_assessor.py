import datetime
from pathlib import Path

def read_mood_data(file_path):
    """
    Read mood data from the specified file.
    """
    if not file_path.is_file():
        return []

    with open(file_path, 'r') as file:
        data = file.readlines()
    
    return [line.strip() for line in data]

def write_mood_data(file_path, mood_value):
    """
    Write mood data to the specified file.
    """
    with open(file_path, 'a') as file:
        file.write(f"{mood_value}\n")

def get_today_date():
    """
    Get today's date in YYYY-MM-DD format.
    """
    return datetime.date.today().strftime("%Y-%m-%d")

def assess_mood():
    """
    Assess the mood based on user input and store the result.
    """
    mood_mapping = {
        "happy": 2,
        "relaxed": 1,
        "apathetic": 0,
        "sad": -1,
        "angry": -2
    }
    
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    file_path = data_dir / "mood_diary.txt"
    
    today_date = get_today_date()
    mood_data = read_mood_data(file_path)
    
    # Check if today's mood is already recorded
    if any(today_date in entry for entry in mood_data):
        print("Sorry, you have already entered your mood today.")
        return
    
    # Get valid mood input from the user
    while True:
        user_mood = input("Enter your current mood (happy, relaxed, apathetic, sad, angry): ").strip().lower()
        if user_mood in mood_mapping:
            break
        print("Invalid mood. Please enter a valid mood.")
    
    mood_value = mood_mapping[user_mood]
    write_mood_data(file_path, f"{today_date}: {mood_value}")
    print("Mood recorded successfully.")
    
    # Analyze the mood data for diagnosis
    if len(mood_data) < 6:
        print("Not enough data for diagnosis.")
        return

    # Only consider the last 7 days of mood entries
    recent_moods = [line.split(": ")[1] for line in mood_data[-6:]] + [str(mood_value)]
    recent_mood_values = [int(mood) for mood in recent_moods]

    # Diagnosis logic
    happy_count = recent_mood_values.count(2)
    sad_count = recent_mood_values.count(-1)
    apathetic_count = recent_mood_values.count(0)
    
    diagnosis = None

    if happy_count >= 5:
        diagnosis = "manic"
    elif sad_count >= 4:
        diagnosis = "depressive"
    elif apathetic_count >= 6:
        diagnosis = "schizoid"
    else:
        average_mood = sum(recent_mood_values) / len(recent_mood_values)
        if average_mood > 0:
            diagnosis = "relaxed"
        elif average_mood == 0:
            diagnosis = "apathetic"
        else:
            diagnosis = "sad"
    
    print(f"The mood assessment diagnosis is: {diagnosis}")

if __name__ == "__main__":
    assess_mood()
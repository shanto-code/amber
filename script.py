import os
import random

def get_assets():
    # বর্তমান ফাইলের লোকেশন অনুযায়ী পাথ সেট করা
    base_dir = os.path.dirname(os.path.abspath(__file__))
    music_dir = os.path.join(base_dir, "music")
    image_dir = os.path.join(base_dir, "images")

    # ফাইল লিস্ট চেক করা
    try:
        music_files = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]
        image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
    except FileNotFoundError:
        return "Error: music or images folder not found!"

    if not music_files or not image_files:
        return "Error: Folders are empty!"

    # লটারি করে ফাইল বাছাই
    selected_music = os.path.join(music_dir, random.choice(music_files))
    selected_image = os.path.join(image_dir, random.choice(image_files))

    # আপনার চ্যানেলের জন্য স্পেশাল ডার্ক সাইকোলজি টেক্সট
    facts = [
        "Silence is the best revenge.",
        "The eyes never lie, even when the lips do.",
        "Stay private, stay lowkey, stay happy.",
        "To gain power, learn to be unpredictable.",
        "Your biggest enemy is your own overthinking."
    ]
    
    selected_facts = random.sample(facts, 5)
    
    # সবগুলো তথ্যকে পাইপ (|) দিয়ে আলাদা করে পাঠানো
    return f"{selected_music}|{selected_image}|{'|'.join(selected_facts)}"

if __name__ == "__main__":
    print(get_assets())

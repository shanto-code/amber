import os
import random

def get_assets():
    # গান এবং ছবির ফোল্ডার পাথ (আপনার গিটহাব রেপো অনুযায়ী চেক করুন)
    music_dir = "music"
    image_dir = "images"

    # ফোল্ডার থেকে ফাইল লিস্ট করা
    music_files = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]
    image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]

    if not music_files or not image_files:
        return "Error: No music or images found"

    # র‍্যান্ডম একটি গান এবং একটি ছবি বেছে নেওয়া
    selected_music = os.path.join(music_dir, random.choice(music_files))
    selected_image = os.path.join(image_dir, random.choice(image_files))

    # স্ক্রিনে দেখানোর জন্য ৫টি র‍্যান্ডম ফ্যাক্টস বা টেক্সট
    facts = [
        "Silence is the best revenge.",
        "The eyes never lie, even when the lips do.",
        "Stay private, stay lowkey, stay happy.",
        "Focus on yourself, the world will follow.",
        "Darkness is just the absence of light.",
        "Music heals what words cannot.",
        "Consistency is more important than perfection.",
        "The best is yet to come.",
        "Your only limit is your mind.",
        "Success is the loudest noise."
    ]
    
    selected_facts = random.sample(facts, 5)

    # সব তথ্যকে একটি স্ট্রিং হিসেবে রিটার্ন করা (live.yml এ ব্যবহারের জন্য)
    return f"{selected_music}|{selected_image}|{'|'.join(selected_facts)}"

if __name__ == "__main__":
    print(get_assets())

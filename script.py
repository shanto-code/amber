import os
import random

def get_assets():
    # আপনার গিটহাবের ফোল্ডার নাম অনুযায়ী (বড় হাতের অক্ষর খেয়াল করুন)
    music_dir = "Lo-Fi"
    image_dir = "Images"

    # ফোল্ডারগুলো আছে কি না নিশ্চিত করা
    if not os.path.exists(music_dir) or not os.path.exists(image_dir):
        # যদি উপরের নামে না থাকে তবে ছোট হাতের নামে চেক করবে
        music_dir, image_dir = "music", "images"

    try:
        # শুধু mp3 এবং ছবিগুলো লিস্ট করা
        music_files = [f for f in os.listdir(music_dir) if f.lower().endswith('.mp3')]
        image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    except Exception:
        return "Error|Error|Error|Error|Error|Error|Error"

    if not music_files or not image_files:
        return "Empty|Empty|Error|Error|Error|Error|Error"

    # র‍্যান্ডম ফাইল সিলেক্ট করা
    selected_music = os.path.join(music_dir, random.choice(music_files))
    selected_image = os.path.join(image_dir, random.choice(image_files))

    # আপনার চ্যানেলের জন্য ৫টি টেক্সট
    facts = [
        "Silence is the best revenge.",
        "The eyes never lie, even when the lips do.",
        "Stay private, stay lowkey, stay happy.",
        "To gain power, learn to be unpredictable.",
        "Your biggest enemy is your own overthinking."
    ]
    
    selected_facts = random.sample(facts, 5)
    
    # সবগুলো ডাটা একসাথে পাঠানো
    return f"{selected_music}|{selected_image}|{'|'.join(selected_facts)}"

if __name__ == "__main__":
    print(get_assets())

import random

# Articles of the Code of Conduct
articles = {
    "Article 1": "I am an American fighting in the forces which guard my country and our way of life. I am prepared to give my life in their defense.",
    "Article 2": "I will never surrender of my own free will. If in command, I will never surrender the members of my command while they still have the means to resist.",
    "Article 3": "If I am captured, I will continue to resist by all means available. I will make every effort to escape and aid others to escape. I will accept neither parole nor special favors from the enemy.",
    "Article 4": "If I become a prisoner of war, I will keep faith with my fellow prisoners. I will give no information or take part in any action which might be harmful to my comrades. If I am senior I will take command. If not I will obey the lawful orders of those appointed over me and back them up in every way.",
    "Article 5": "When questioned, should I become a prisoner of war, I am required to give name, rank, service number, and date of birth. I will evade answering further questions to the utmost of my ability. I will make no oral or written statements disloyal to my country and its allies or harmful to their cause.",
    "Article 6": "I will never forget that I am an American, fighting for freedom, responsible for my actions, and dedicated to the principles which made my country free. I will trust in my God and in the United States of America."
}

# MAJCOMS terms and definitions
majcoms = {
    "Air Combat Command (ACC)": "Joint Base Langley-Eustis, Virginia",
    "Air Education Training Command (AETC)": "Joint Base San Antonio-Randolph AFB, Texas",
    "Air Force Materiel Command (AFMC)": "Wright-Patterson AFB, Ohio",
    "Air Force Reserve Command (AFRC)": "Robins AFB, Georgia",
    "Air Force Special Operations Command (AFSOC)": "Hurlburt Field, Florida",
    "Air Mobility Command (AMC)": "Scott AFB, Illinois",
    "Air Force Global Strike Command (AFGSC)": "Barksdale AFB, Louisiana",
    "Pacific Air Forces (PACAF)": "Joint Base Pearl Harbor-Hickam, Hawaii",
    "US Air Forces in Europe - Air Forces Africa (USAFE)": "Ramstein AB, Germany",
    "Space Operations Command (SOC)": "Peterson SFB, Colorado",
    "Space Training & Readiness Command (STARCOM)": "Peterson SFB, Colorado",
    "Space Systems Command (SSC)": "Los Angeles SFB, California"
}

chain_of_command = {
    "AFROTC Detachment 340 Commander" : "Lt. Col. Adam J. Messer",
    "AFROTC North East Region Commander" : "Col. Shannon E. Moore",
    "AFROTC Commander" : "Col. Eugene A. Moore III",
    "Holm Center Commander" : "Brigadier Gen. Joseph L. Sheffield",
    "Air University Commander" : "Lt. Gen. Andrea D. Tullos",
    "Air Education and Training Command Commander" : "Lt. Gen. Brian S. Robinson",
    "Chief of Space Operations" : "Gen. B. Chance Saltzman",
    "Chief of Staff of the Air Force" : "Gen. David W. Allvin",
    "Chairman of the Joint Chief of Staff" : "Gen. Charles Q. Brown Jr.",
    "Secretary of the Air Force" : "The Honorable Frank Kendall III",
    "Secretary of Defense" : "The Honorable Lloyd J. Austin III",
    "President of the United States" : "The Honorable Joseph R. Biden Jr."
}

# Allow the user to pick a study set (input should be an integer only)
study_sets = [articles, majcoms, chain_of_command]
print("Choose a study set:")
print("1) Articles of the Code of Conduct")
print("2) MAJCOMS")
print("3) Chain of Command")

while True:
    try:
        choice_set = int(input("Enter 1, 2, or 3: "))
        if choice_set in {1, 2, 3}:
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Decrement the choice by 1 to align with the list index
choice_set -= 1

# Shuffle terms
terms = list(study_sets[choice_set].keys())
random.shuffle(terms)

# Quiz loop
score = 0
for term in terms:
    correct_definition = study_sets[choice_set][term]
    incorrect_flag = False
    while True:
        print(f"\nDefine {term}:")
        answer = input("Your answer: ").strip()

        # Check if the answer is correct
        if answer == correct_definition:
            print("Correct!")
            if not incorrect_flag:
              score += 1
            break
        else:
            print("Incorrect. Try again.")
            incorrect_flag = True

# Final score
total_questions = len(terms)
print(f"\nYour final score is {score}/{total_questions}.")
if score == total_questions:
    print("Excellent work! You've mastered this material.")
elif score >= total_questions * 0.7:
    print("Good job! Keep practicing to perfect your knowledge.")
else:
    print("Keep studying! You'll get better with practice.")
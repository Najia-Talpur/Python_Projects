import random

print("======================================")
print("      FAKE NEWS HEADLINE GENERATOR    ")
print("======================================")
print("Generate random and fun news headlines!")
print("Choose a category or create your own.")
print()

categories = {
    "Technology": [
        "A tech billionaire",
        "A startup founder",
        "A software engineer",
        "A robotics company",
        "A group of scientists",
        "An AI robot",
        "A cybersecurity expert"
    ],

    "Sports": [
        "A professional football player",
        "A tennis champion",
        "An Olympic athlete",
        "A basketball coach",
        "A young rising athlete",
        "A sports commentator"
    ],

    "Movies": [
        "A famous actor",
        "A Hollywood director",
        "A movie producer",
        "A rising film star",
        "A streaming platform",
        "A film critic"
    ],

    "Education": [
        "A university professor",
        "A college student",
        "A school principal",
        "A group of researchers",
        "An education minister",
        "A scholarship program"
    ],

    "Animals": [
        "A curious cat",
        "A clever dog",
        "A group of monkeys",
        "A wild elephant",
        "A zoo keeper",
        "A rare panda"
    ],

    "Business": [
        "A startup company",
        "A multinational corporation",
        "A young entrepreneur",
        "A financial expert",
        "A business consultant",
        "A venture capitalist"
    ]
}

actions = [
    "announces",
    "launches",
    "cancels",
    "celebrates",
    "investigates",
    "reveals",
    "discovers",
    "organizes",
    "supports",
    "criticizes",
    "apologizes for",
    "invests in",
    "creates",
    "tests",
    "builds",
    "promotes",
    "debates",
    "plans",
    "introduces",
    "demonstrates"
]

objects = [
    "a new technology platform",
    "a groundbreaking research project",
    "a global charity campaign",
    "a controversial policy",
    "a revolutionary smartphone",
    "a viral social media trend",
    "a new online business",
    "a space exploration mission",
    "an artificial intelligence system",
    "a new electric vehicle",
    "a record-breaking sports event",
    "a secret startup idea",
    "a documentary film",
    "a digital education program",
    "a sustainable energy solution",
    "a new mobile application",
    "a major investment deal",
    "a public awareness campaign",
    "a creative art exhibition",
    "an international conference"
]

locations = [
    "during a live interview",
    "at a global technology conference",
    "inside a government building",
    "during a press conference",
    "at a university campus",
    "during a late night broadcast",
    "in the middle of a busy city",
    "at an international summit",
    "during a major sporting event",
    "inside a research laboratory",
    "at a public event",
    "during an online livestream",
    "at a startup conference",
    "during a community gathering",
    "at an awards ceremony",
    "inside a corporate headquarters",
    "at a business meeting",
    "during a charity event",
    "at a global forum",
    "during a social media livestream"
]

while True:
    print("Choose a category:")

    for category in categories:
        print("-", category)

    print("- Custom")
    choice = input("Enter category: ").title().strip()

    if choice == "Custom":
        subject = input("Enter your own subject: ")

    elif choice in categories:
        subject = random.choice(categories[choice])

    else:
        print("Invalid category")
        exit()

    def generate_headline():
        action = random.choice(actions)
        object = random.choice(objects)
        location = random.choice(locations)
        return f"🚨 BREAKING NEWS: {subject} {action} {object} {location}"

    print(generate_headline())

    user_input = input("Do you wnat another headline? (yes/no) ").strip().title()
    if user_input == "No":
        break

print("Thanks for using Fake Headline Generator. Have a fun day")

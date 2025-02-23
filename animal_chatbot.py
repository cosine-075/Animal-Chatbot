import random

animal_data = {
    "dog": {
        "facts": ["Dogs have an amazing sense of smell.", "They can hear sounds four times farther away than humans.", "Different breeds have different jobs, like herding or rescuing."],
        "responses": ["Dogs are loyal companions!", "Woof woof!", "They love to play fetch."],
        "questions": {
            "what do dogs eat": ["Dogs eat special dog food, but also some human foods in moderation.", "They need a balanced diet of protein, carbs, and fats."],
            "how do dogs help people": ["Dogs can help people by guiding the blind, helping in rescues, and being emotional support animals.", "They also keep us company!"],
        }
    },
    "cat": {
        "facts": ["Cats can jump up to six times their height.", "They have flexible bodies and can squeeze through tight spaces.", "Cats use their whiskers to sense their surroundings."],
        "responses": ["Meow! Cats are mysterious.", "Purr...", "They love to nap in sunny spots."],
        "questions": {
            "why do cats purr": ["Cats purr when they're happy, but sometimes when they're scared or in pain.", "Scientists think it might help them heal."],
            "how do cats clean themselves": ["Cats clean themselves by licking their fur.", "Their tongues have tiny barbs that help remove dirt."],
        }
    },
    "elephant": {
        "facts": ["Elephants have the largest brains of any land animal.", "They use their trunks to communicate and grab things.", "Elephants live in family groups called herds."],
        "responses": ["Elephants are very intelligent!", "They are huge and gentle.", "They love to take mud baths."],
        "questions": {
            "how long do elephants live": ["Elephants can live for about 60 to 70 years in the wild.", "That's a very long life!"],
            "why do elephants have trunks": ["Elephants use their trunks for many things, like breathing, smelling, drinking, and grabbing food.", "It's like a multi-tool!"],
        }
    },
    "bird": {
        "facts": ["Birds have hollow bones, which makes them light for flying.", "Many birds can sing beautiful songs.", "Some birds migrate thousands of miles each year."],
        "responses": ["Chirp chirp!", "Birds are free spirits.", "They love to build nests."],
        "questions": {
            "why do birds sing": ["Birds sing to attract mates and to mark their territory.", "It's like their way of talking."],
            "how do birds fly": ["Birds fly by flapping their wings, which creates lift.", "Their feathers help them stay in the air."],
        }
    },
    "penguin": {
        "facts": ["Penguins are birds that can't fly, but they are excellent swimmers.", "They live in very cold places, like Antarctica.", "Penguins huddle together to stay warm."],
        "responses": ["Waddle waddle!", "They are very good at diving.", "They love to eat fish."],
        "questions": {
            "how do penguins stay warm": ["Penguins have thick layers of fat and feathers to keep them warm.", "They also huddle together in groups."],
            "what do penguins eat": ["Penguins eat fish, krill, and squid.", "They dive deep into the ocean to find food."],
        }
    },
    "lion": {
        "facts": ["Lions are known as the king of the jungle, even though they live in grasslands.", "Female lions do most of the hunting.", "Lions live in groups called prides."],
        "responses": ["Roar!", "They are very powerful.", "They love to sleep in the shade."],
        "questions": {
            "why do lions have manes": ["Male lions have manes to make them look bigger and more intimidating.", "It also protects their necks during fights."],
            "where do lions live": ["Lions live in grasslands and savannas in Africa.", "They need lots of space to roam."],
        }
    }
}

def chatbot():
    print("Hello! I'm your animal expert chatbot.")
    print("Ask me about dogs, cats, elephants, birds, penguins, or lions!")

    while True:
        user_input = input("You: ").lower().strip()

        if "bye" in user_input or "goodbye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break

        if not user_input:
            print("Chatbot: Please ask me a question!")
            continue

        animal_found = False
        for animal, data in animal_data.items():
            if animal in user_input:
                animal_found = True
                if "fact" in user_input:
                    fact = random.choice(data["facts"])
                    print(f"Chatbot: Here's a fact about {animal}s: {fact}")
                elif any(question in user_input for question in data["questions"]):
                    for question, answers in data["questions"].items():
                        if question in user_input:
                            answer = random.choice(answers)
                            print(f"Chatbot: {answer}")
                            break
                else:
                    response = random.choice(data["responses"])
                    print(f"Chatbot: {response}")
                break
        if not animal_found:
            print("Chatbot: I'm sorry, I don't know about that animal. Try asking about dogs, cats, elephants, birds, penguins, or lions.")

chatbot()
# Additional greetings for the chatbot
additional_greetings = [
    "Hello!",
    "Hi there!",
    "Greetings!",
    "Howdy!",
    "Good day!"
]

# Information related to classrooms
classroom_info = [
    "Where is Room 101?",
    "Room 101 is located on the first floor of the main building.",
    "Which room is the Computer Lab?",
    "The Computer Lab is in Room 202 on the second floor.",
    "Where can I find the library?",
    "The library is on the ground floor, next to the main entrance."
]

# Example function (you can modify as per your needs)
def get_classroom_info(room_number):
    classroom_dict = {
        "101": "Room 101 is on the first floor.",
        "202": "Room 202 is the Computer Lab on the second floor.",
        "Library": "The library is on the ground floor."
    }
    return classroom_dict.get(room_number, "I don't have information on that room.")

import random

sample_recommendations = {
    "user1": ["tshirt_red.jpg", "jeans_blue.jpg"],
    "user2": ["jacket_black.jpg", "sneakers_white.jpg"]
}

def get_recommendations(user_id):
    return sample_recommendations.get(user_id, random.sample(list(sample_recommendations["user1"]), 2))
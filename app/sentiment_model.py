sample_reviews = {
    "tshirt_red.jpg": ["Great quality for the price!", "Loved the color and fit."],
    "jeans_blue.jpg": ["Comfortable and durable.", "Fabric feels cheap."]
}

def get_sentiment_tags(product_id):
    reviews = sample_reviews.get(product_id, [])
    tags = []
    for review in reviews:
        if "great" in review.lower():
            tags.append("Great Value")
        if "cheap" in review.lower():
            tags.append("Low Quality")
    return list(set(tags))
scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = "white yellow orange green blue brown black paneled red".split()


def get_belt(user_score, scores=scores, belts=belts):
    match user_score:
        case user_score if user_score >= 1000:
            return "red"

        case user_score if user_score >= 800:
            return "paneled"

        case user_score if user_score >= 600:
            return "black"

        case user_score if user_score >= 400:
            return "brown"

        case user_score if user_score >= 250:
            return "blue"
        
        case user_score if user_score >= 249:
            return "green"

        case user_score if user_score >= 101:
            return "orange"

        case user_score if user_score >= 50:
            return "yellow"

        case user_score if user_score >= 10:
            return "white"

        case user_score if user_score < 10:
            return None

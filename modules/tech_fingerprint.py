import builtwith

def detect_technologies(url):

    try:
        technologies = builtwith.parse(url)

        return technologies

    except Exception as e:

        return {"error": str(e)}

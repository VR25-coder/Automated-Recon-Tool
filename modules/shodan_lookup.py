import shodan

API_KEY = "M5Bw2WiiM7LYhJmUUr72cLyUtKR8sOpx"

def lookup_ip(ip):

    api = shodan.Shodan(API_KEY)

    try:
        host = api.host(ip)

        return {
            "ip": host["ip_str"],
            "organization": host.get("org", "N/A"),
            "os": host.get("os", "Unknown"),
            "ports": host.get("ports", [])
        }

    except Exception as e:

        return {"error": str(e)}

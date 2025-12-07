def handler(request):
    import os

    here = os.path.dirname(__file__)
    tarinat_path = os.path.join(here, "..", "tarinat.txt")

    with open(tarinat_path, "r", encoding="utf-8") as f:
        tarinat = f.read()

    # Palaa JSON-vastauksella
    return {
        "status": 200,
        "body": tarinat
    }

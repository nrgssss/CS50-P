def main():
    spacecraft ={"name": "james webb space telescope"}
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    
    ========================REOPRT=======================

    Name:{spacecraft["name"]}
    Distance:{spacecraft.get("distance", "Unknown")} AU

    =====================================================
    """
main()
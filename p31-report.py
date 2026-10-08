def main():
    spacecraft={"name":"James webb space Telescope"}
    spacecraft.update({"distance" : 0.01,"orbit":"Sun"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""

=============================REPORT============================

    Name:{spacecraft.get("name","Unknown")}
    Distance:{spacecraft.get("distance","Unknown")} AU
    orbit:{spacecraft.get("orbit", "Unknown")}

===============================================================
"""
main()

def main():
    spacecraft = {"name":"james webb spase telescope"}
    spacecraft["distance"]=0.01
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ================REPORT================

    Name:{spacecraft["name"]}
    Distance:{spacecraft["distance"]} AU
    
    ======================================
    """
main()
couple_quantities = {
    "AA-AA":0,
    "AA-Aa":0,
    "AA-aa":0,
    "Aa-Aa":0,
    "Aa-aa":0,
    "aa-aa":0
}

couple_quantities["AA-AA"] = int(raw_input("Insert number of AA-AA couples:"))
couple_quantities["AA-Aa"] = int(raw_input("Insert number of AA-Aa couples:"))
couple_quantities["AA-aa"] = int(raw_input("Insert number of AA-aa couples:"))
couple_quantities["Aa-Aa"] = int(raw_input("Insert number of Aa-Aa couples:"))
couple_quantities["Aa-aa"] = int(raw_input("Insert number of Aa-aa couples:"))
couple_quantities["aa-aa"] = int(raw_input("Insert number of aa-aa couples:"))

def dominantProb():
    AAAA_prob = 1
    AAAa_prob = 1
    AAaa_prob = 1
    AaAa_prob = float(0.75)
    Aaaa_prob = float(0.5)
    aaaa_prob = 0
    
    return 2*(
        couple_quantities["AA-AA"] * AAAA_prob +
        couple_quantities["AA-Aa"] * AAAa_prob +
        couple_quantities["AA-aa"] * AAaa_prob +
        couple_quantities["Aa-Aa"] * AaAa_prob +
        couple_quantities["Aa-aa"] * Aaaa_prob +
        couple_quantities["aa-aa"] * aaaa_prob
        )

print dominantProb()

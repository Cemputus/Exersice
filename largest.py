def is_uganda_martyr(name):
    uganda_martyrs = [
        "Achilleus Kewanuka",
        "Adolphus Ludigo-Mukasa",
        "Ambrosius Kibuuka",
        "Anatoli Kiriggwajjo",
        "Andrew Kaggwa",
        "Antanansio Bazzekuketta",
        "Bruno Sserunkuuma",
        "Charles Lwanga",
        "Denis Ssebuggwawo Wasswa",
        "Gonzaga Gonza",
        "Gyavira Musoke",
        "James Buuzaabalyaawo",
        "John Maria Muzeeyi",
        "Joseph Mukasa",
        "Kizito",
        "Lukka Baanabakintu",
        "Matiya Mulumba",
        "Mbaga Tuzinde",
        "Mugagga Lubowa",
        "Mukasa Kiriwawanvu",
        "Nowa Mawaggali",
        "Ponsiano Ngondwe"
    ] 

    return name in uganda_martyrs

input_name = "Joseph Mukasa"
result = is_uganda_martyr(input_name)
if result:
    print(f"{input_name} is a Uganda Martyr.")
else:
    print(f"{input_name} is not a Uganda Martyr.")






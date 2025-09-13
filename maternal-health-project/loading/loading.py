#===================== 3. Function to store data in data storage path ===========================
# step1: Data extraction and  loading using telecharger_fichier() function (EL)
telechargements_reussis = True
i=1 # Delimitted phase 
for nom, url in datasets.items():
    base_path = base_path_st1
    sheet_name = "child_section"
    if i < 7:
        i+=1
    else:
        base_path = base_path_st2
        sheet_name = "child_form"
    if nom == "newbornData" or nom.endswith(("N")):
        # Pour newbornData, on télécharge la feuille "Newborn"
            dest = os.path.join(base_path,"LABELLED/", f"{nom}Labelled.xlsx")
            if not telecharger_fichier(url, dest, sheet_name=sheet_name):
                telechargements_reussis = False
    else:
            dest = os.path.join(base_path,"LABELLED/", f"{nom}Labelled.xlsx")
            if not telecharger_fichier(url, dest):
                telechargements_reussis = False

import os
import requests
from plyer import notification
import pandas as pd

# Path for data storage avec loading from server 
base_path = "/your-current-staging-areas/path"

#===================== 1. define data api ===========================
# Api definition for our database
datasets = {
    "dataset1": "https://kf.kobotoolbox.org/api/.../data.xlsx",
        ...                                                        ,
    "datasetn": "https://kf.kobotoolbox.org/api/.../data.xlsx"
}

#===================== 2. Function to download dataset ===========================
# Function load data with Excel API's URL 
# Param 1: API's url
# Param 2: Dataset path including the file name and extention
# Param 3: sheet_name
def telecharger_fichier(url, destination, sheet_name=None):
    try:
        response = requests.get(url) # Get excel file from API url
        response.raise_for_status() # Check getting statu
        if sheet_name is not None:
            excel_file = pd.ExcelFile(BytesIO(response.content)) # Create Excel Empty file
            # Look for the our specified excel sheet
            if sheet_name in excel_file.sheet_names:
                df = pd.read_excel(excel_file, sheet_name=sheet_name)
            else:
                # Let us take first sheet when our sheet is not available 
                # Assume we know, if there are not repeat in our form, excel file is not named
                df = pd.read_excel(excel_file)
            df.to_excel(destination, index=False)
        else:
            # Write excel content in our destination file
            with open(destination, "wb") as f:
                f.write(response.content)
        print(f"✅ Téléchargement réussi : {os.path.basename(destination)}")
        return True
    except Exception as e:
        print(f"❌ Échec : {os.path.basename(destination)} — {e}")
        return False

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
     

#===================== 3. Function to store data in data storage path ===========================
# step2: Transform data first row to variable name code (T)
data_finale = {}
i=1 # Delimitted phase 
for nom in datasets:
    base_path = base_path_st1
    if i < 7:
        i+=1
    else:
        base_path = base_path_st2
    try:       
        df_nolabel = pd.read_excel(os.path.join(base_path, f"{nom}.xlsx"))
        df_labelled = pd.read_excel(os.path.join(base_path, "LABELLED/", f"{nom}Labelled.xlsx"))
        
        
        if not df_nolabel.empty and not df_labelled.empty:
            # Si les deux fichiers ont du contenu, on remplace les colonnes normalement
            df_labelled.columns = df_nolabel.columns
            df_labelled.to_excel(os.path.join(base_path,"LABELLED/", f"{nom}Labelled.xlsx"), index=False)
            data_finale[nom] = df_labelled
            print(f"🔄 Colonnes remplacées pour : {nom}")
        else:
            # Si un des fichiers est vide, on crée un fichier avec juste les colonnes
            df_vide_colonnes = pd.DataFrame(columns=df_nolabel.columns)
            df_vide_colonnes.to_excel(os.path.join(base_path,"LABELLED/", f"{nom}Labelled.xlsx"), index=False)
            data_finale[nom] = df_vide_colonnes
            print(f"⚠️ Fichier vide, colonnes ajoutées pour : {nom}")
    except Exception as e:
        print(f"⚠️ Erreur traitement {nom} : {e}")
        telechargements_reussis = False


# 1.
# With API : we extract raw data labelled and we transform first row to got labelled data
#


# Notification de fin
notification.notify(
    title="Téléchargements terminés",
    message="Tous les téléchargements ont réussi !" if telechargements_reussis else "Certains téléchargements ont échoué.",
    timeout=10
)

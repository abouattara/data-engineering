import os
import requests
from plyer import notification
import pandas as pd

# Path for data storage avec loading from server 
base_path = "/your-current-staging-areas/path"

# Api definition for our database
datasets = {
    "preInclusionData": "https://kf.kobotoolbox.org/api/.../data.xlsx",
    "depistageData":    "https://kf.kobotoolbox.org/api/.../data.xlsx",
    "inclusionData":    "https://kf.kobotoolbox.org/api/.../data.xlsx",
    "suiviData":        "https://kf.kobotoolbox.org/api/.../data.xlsx",
    "accouchementData": "https://kf.kobotoolbox.org/api/.../data.xlsx"
}

# Function to download data files 
def download_files(url, destination):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(destination, "wb") as f:
            f.write(response.content)
        print(f"✅ data loaded Successfully ! : {os.path.basename(destination)}")
        return True
    except Exception as e:
        print(f"❌ Error : {os.path.basename(destination)} — {e}")
        return False


# Download_files() use to download data files
success_downloading = True
for name, url in datasets.items():
    # File name and stagging areas path definition
    dest = os.path.join(base_path, f"{name}Labelled.xlsx")
    if not download_files(url, dest):
        success_downloading = False


# data loading and column names management
data_finale = {}
for name in datasets:
    try:
        # Load two fomat of our database
        df_nolabel = pd.read_excel(os.path.join(base_path, f"{name}.xlsx"))
        df_labelled = pd.read_excel(os.path.join(base_path, f"{name}Labelled.xlsx"))
        
        if not df_nolabel.empty and not df_labelled.empty:
            # if there data in theses two files renames column names normally
            df_labelled.columns = df_nolabel.columns
            df_labelled.to_excel(os.path.join(base_path, f"{name}Labelled.xlsx"), index=False)
            data_finale[name] = df_labelled
            print(f"🔄 Column names are renamed for : {name}")
        else:
            # If there are empty file, define it column names
            df_vide_colonnes = pd.DataFrame(columns=df_nolabel.columns)
            df_vide_colonnes.to_excel(os.path.join(base_path, f"{name}Labelled.xlsx"), index=False)
            data_finale[name] = df_vide_colonnes
            print(f"⚠️ Empty file, column names are defined for : {name}")
    except Exception as e:
        print(f"⚠️ Error file column names definition for {name} : {e}")
        success_downloading = False




# Notified 
notification.notify(
    title="End of downloading",
    message="All files are successfully downloaded !" if success_downloading else "Error occurs for certain files !",
    timeout=10
)
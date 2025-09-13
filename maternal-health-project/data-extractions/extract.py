# Path for data storage avec loading from server 
base_path = "/your-current-staging-areas/path"

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

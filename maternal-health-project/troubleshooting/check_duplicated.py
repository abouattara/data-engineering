def find_duplicates(df, col_name, label):
    duplicated_ids = df[df.duplicated(subset=[col_name], keep=False)][col_name]
    if not duplicated_ids.empty:
        message = f"🔴 Doublons dans {label} ({col_name}) :\n" + ", ".join(map(str, duplicated_ids.unique()))
        return message
    return None

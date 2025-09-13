def check_tracability(child_df, child_col, parent_df, parent_col, child_label, parent_label):
    """Retourne les identifiants du child_df qui ne sont pas dans le parent_df."""
    invalid_ids = child_df[~child_df[child_col].isin(parent_df[parent_col])][child_col].unique()
    if invalid_ids.size > 0:
        return f"⛔ {child_label} non trouvées {parent_label} :\n" + ", ".join(map(str, invalid_ids))
    return Non

import emoji


def add_char_count(df):
    df["char_count"] = df["text"].str.len()
    return df

def add_has_tsla(df):
    pattern = r"\b(tsla|\$tsla|tesla)\b"
    df["has_tsla"] = df["text"].str.contains(pattern, case=False, regex=True).astype(int)
    return df

def add_has_emoji(df):
    df["has_emoji"] = df["text"].apply(lambda x: int(any(char in emoji.EMOJI_DATA for char in x)))
    return df

def add_exclam_count(df):
    df["exclam_count"] = df["text"].str.count("!")
    return df

def add_is_reply(df):
    df["is_reply"] = df["text"].str.startswith("@").astype(int)
    return df
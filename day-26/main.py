from pathlib import Path
import pandas as pd

BASE_DIR: Path = Path(__file__).parent
DATA_PATH: Path = BASE_DIR / "unesco_nato_alphabet.csv"

def run_alphabet_encoder() -> None:
    if not DATA_PATH.exists():
        print(f"[FATAL] Critical registry file is missing at: {DATA_PATH.name}")
        return

    data_frame: pd.DataFrame = pd.read_csv(DATA_PATH)

    data_frame.columns = data_frame.columns.str.strip().str.lower()
    print(f"[DEBUG] Validated dataset columns in memory: {list(data_frame.columns)}")

    nato_dict: dict[str, str] = {row["letter"]: row["code"] for (index, row) in data_frame.iterrows()}
    print("[SUCCESS] NATO phonetic dictionary database generated and loaded into memory.")

    user_input: str = input("Enter a word to encode into aviation phonetic matrix: ").upper()

    try:
        encoded_result: list[str] = [nato_dict[letter] for letter in user_input if letter in nato_dict]
        print(f"[RESULT] Phonetic vector output: {encoded_result}")
    except KeyError as error:
        print(f"[ERROR] Character translation sequence failed. Invalid identifier: {error}")

if __name__ == "__main__":
    run_alphabet_encoder()
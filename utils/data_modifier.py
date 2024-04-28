import pandas as pd

class DataModifier:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path

    def handle(self):
        try:
            df = pd.read_csv(self.csv_file_path, encoding="unicode_escape")
            return df
        except FileNotFoundError:
            print(f"Error: CSV file '{self.csv_file_path}' not found.")
            return None

    def change_col_name(self, old_col_name, new_col_name):
        df = self.handle()
        if df is not None:
            try:
                df.rename(columns={old_col_name: new_col_name}, inplace=True)
                df.to_csv(self.csv_file_path, index=False)
            except KeyError:
                print(f"Error: Column '{old_col_name}' not found in the CSV file.")

    def change_value(self, col_name, old_val, new_val):
        df = self.handle()
        if df is not None:
            if col_name in df.columns:
                df[col_name] = df[col_name].astype(str)
                df[col_name] = df[col_name].replace(old_val, new_val)
                df.to_csv(self.csv_file_path, index=False)
            else:
                print(f"Error: Column '{col_name}' not found in the CSV file.")

if __name__ == "__main__":
    dataModifier = DataModifier("data\\responses\\all_labeled_gpt-3.5-turbo.csv")
    dataModifier.change_col_name("Label", "is harmful?")
    dataModifier.change_col_name("Response", "response")
    dataModifier.change_value("is harmful?", "0", "No")
    dataModifier.change_value("is harmful?", "1", "Yes")

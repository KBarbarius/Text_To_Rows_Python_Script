import pandas as pd
from tqdm import tqdm

# Loading the excel file into a DataFrame
excel_file_path = 'D:/wewe655.xlsx'
df = pd.read_excel(excel_file_path)

# Function to split values in 'Category_ID' column into individual rows
def split_categories(df, output_excel='D:/accessd.xlsx'):
    result = pd.DataFrame(columns=['Track_ID', 'Category_ID'])
    
    total_rows = len(df)
    with tqdm(total=total_rows, desc="Processing Rows") as pbar:
        for _, row in df.iterrows():
            track_id = row['Track_ID']
            categories = list(map(int, str(row['Category_ID']).split(',')))

            result = pd.concat([result, pd.DataFrame({'Track_ID': [track_id]*len(categories), 'Category_ID': categories})])
            pbar.update(1)

    # Save the result to an Excel file
    result.to_excel(output_excel, index=False)
    print(f"Output saved to {output_excel}")

    return result

# Split the 'Category_ID' column into individual rows
result_df = split_categories(df, output_excel='D:/converted.xlsx')

print(result_df)

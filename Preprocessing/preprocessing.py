
from operator import index


class PreprocessingClass:

    # def change_dtype_utility(df, name, current_param, replaced_param):
    #     return df[name].astype(str).str.replace(current_param,replaced_param, regex=True)

    def delete_unnecessary_rows(df):
        real_columns = df.loc[0]
        df.columns = real_columns
        df.drop(labels=0, axis=0, inplace=True)
        df.columns=df.columns.astype(str)
        df.rename(columns={'NaT':'Date'}, inplace=True)

    
    def change_data_type(df):
        params = df.columns
        parameters = params[1:]
    
        for param in parameters:
            df[param] = df[param].astype(str).str.replace('-','0', regex=True)
            df[param] = df[param].astype(str).str.replace('.', '', regex=True)
            df[param] = df[param].astype(str).str.replace(',', '.', regex=True)
            df[param] = df[param].astype(float)

    def change_dataset_index(df):
        df.index = df['Date']


    def replace_nullvalues_with_mean(df):
        pass

    def normalize_data_values(param):
        pass

    def inverse_normalized_data_values(param):
        pass

    def convert_xlsx2csv(NEW_DATA_PATH, df):
        df.to_csv(NEW_DATA_PATH+'test.csv', index=False)



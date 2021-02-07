





from typing import Tuple, Generator
import pandas as pd



def parse_csv_output(
        df:pd.Dataframe,
        filename:str,
        encoding: str,
        starts_with_row:int,
        delimeter:str,
        header:str,
        max_field_length:str,
        quote:str
) -> Generator[Tuple[str,str],None,None]

    temp_file = csv_compose(
        df,
        filename,
        encoding,
        starts_with_row,
        delimeter,
        header,
        max_field_length,

    )
    yield filename,temp_file


def csv_compose(
        df:pd.Dataframe,
        filename:str,
        encoding: str,
        starts_with_row:int,
        delimeter:str,
        header:str,
        max_field_length:str,
        quote:str
):
    df =df_types_to_string(df)
    if max_field_length:
        df = truncate_df(df, max_field_length)
    with tempfile.NamedTemporaryFile
        (
            suffix:".csv",mode = "w+",encoding="encoding",delete= False

        ) as f:
    for _ in range(1,starts_with_row):
        f.write("\n")
        f.close()
        sp.cleanup_files.append(f.name)
    if quote:
        df.to_csv(
            f.name,
            index=False,
            header=header,
            mode="a",
            sep= delemeter,
            quotechar=quote,
            encoding=encoding,
            quoting=csv.QUOTE_NONNUMERIC

        )
    else:
        df.to_csv(
            f.name,
            index=False,
            header=header,
            mode="a",
            sep= delemeter,
            encoding=encoding,

        )
    return f.name






def count_rows(input_path):
    print(f"Counting number of rows in {input_path}...")

    import csv

    with open(input_path) as f:
        reader = csv.reader(f)
        row_count = sum(1 for row in reader)
        print(f"Number of rows in {input_path}: {row_count}")


def create_data_profiling_report(input_path, report_output_path):
    import pandas as pd
    from pandas_profiling import ProfileReport

    df = pd.read_csv(input_path)
    profile = ProfileReport(df, title="Pandas Profiling Report")
    profile.to_file(report_output_path)
    print(f"Created data profiling report to {report_output_path}")


def create_clean_copy(input_path, column_name, type, output_path):
    import pandas as pd

    df = pd.read_csv(input_path)
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
    df.dropna(subset=[column_name], inplace=True)
    df[column_name] = df[column_name].astype(type)
    print(f"Dropping rows in column {column_name} with NA values")
    df.to_csv(output_path, index=False)


def create_report_data(input_path, pivot_index, output_path):
    import pandas as pd

    df = pd.read_csv(input_path)
    df = df.groupby([pivot_index,'gender'])['count'].sum().reset_index()
    df = df.pivot(index=pivot_index, columns='gender', values='count')
    df['percent_female'] = (df['female'] / (df['female'] + df['male'])).round(2)
    df.sort_values(by ='percent_female', ascending=False, inplace=True)
    df.to_csv(output_path)
    print(f"Created report to {output_path}")


def create_bar_chart(input_path, output_path, stacked="true"):
    import pandas as pd

    df = pd.read_csv(input_path)
    figure = df['percent_female'].plot.bar(stacked=stacked)
    figure.get_figure().savefig(output_path)

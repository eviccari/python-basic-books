import os


def extract_name(filename):
    return filename.split(".")[0]


def read_lines(filename):
    _file = open(os.path.join("data/meta-data", filename), "rt")
    data = _file.read().split("\n")
    _file.close()
    return data


def read_metadata(filename):
    metadata = []
    for column in read_lines(filename):
        if column:
            values = column.split("\t")
            nome = values[0]
            tipo = values[1]
            desc = values[2]
            metadata.append((nome, tipo, desc))
    return metadata


def main():
    meta = {}
    for meta_data_file in os.listdir("data/meta-data"):
        table_name = extract_name(meta_data_file)
        meta[table_name] = read_metadata(meta_data_file)

    for key, value in meta.items():
        print(f"Entidade {key}")
        print(f"Atributos: ")
        for col in value:
            print(f"   {col[1]}: {col[0]}")


if __name__ == "__main__":
    main()

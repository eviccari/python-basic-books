# coding: utf-8

import os
import sys


def extract_name(filename):
    return filename.split(".")[0]


def read_lines(filename):
    _file = open(os.path.join("data/meta-data", filename), "rt")
    data = _file.read().split("\n")
    _file.close()
    return data


def read_meta_data(filename):
    metadata = []
    for column in read_lines(filename):
        if column:
            metadata.append(tuple(column.split("\t")[:3]))
    return metadata


def prompt():
    print("\nO que deseja ver?")
    print("(l) Listar entidades")
    print("(d) Exibir atributos da entidade")
    print("(r) Exibir referências de uma entidade")
    print("(s) Sair do programa")
    return input("")


def main():
    # dicionario nome entidade -> atributos
    meta = {}

    # dicionario identificador -> nome entidade
    keys = {}

    # dicionario de relacionamentos
    relationships = {}

    for meta_data_file in os.listdir("data/meta-data"):
        table_name = extract_name(meta_data_file)
        attributes = read_meta_data(meta_data_file)
        identifier = attributes[0][0]

        meta[table_name] = attributes
        keys[identifier] = table_name

    for key, val in meta.items():
        for col in val:
            if col[0] in keys:
                if not col[0] == meta[key][0][0]:
                    relationships[key] = keys[col[0]]

    option = prompt()
    while option != "s":
        if option == "l":
            for entity_name in meta.keys():
                print(entity_name)
        elif option == "d":
            entity_name = input("Nome da entidade: ")
            for col in meta[entity_name]:
                print(col)
        elif option == "r":
            entity_name = input("Nome da entidade: ")
            other_entity = relationships[entity_name]
            print(other_entity)
        option = prompt()


if __name__ == "__main__":
    main()
    sys.exit(0)

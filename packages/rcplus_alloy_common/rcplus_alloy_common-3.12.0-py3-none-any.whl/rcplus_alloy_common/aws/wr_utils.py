import yaml

def read_table_from_yaml_schema(file_path, table_name):
    """Reads the YAML schema file and returns tables configuration."""
    with open(file_path, "r") as file:
        schema = yaml.safe_load(file)
    # Assume unique table names within a schema file
        for source in schema["sources"]:
            for table in source["tables"]:
                if table["name"] == table_name:
                    return table

    raise KeyError(f"{table_name} not found from {file_path}")


def get_partition_columns_with_type(schema):
    """Returns dict of partition columns with their types."""
    return {
        col["name"]: col["type"] for col in schema["columns"]
        if col.get("meta", {}).get("partition")
    }


def get_partition_columns_list(schema):
    """Returns list of partition columns."""
    return list(get_partition_columns_with_type(schema))


def get_columns_with_types(schema, include_partition = True):
    """
    Returns dict of columns with their types.
    include_partitions defines whether partitioned columns are included or not.
    """
    if include_partition:
        return {
            col["name"]: col["type"]
            for col in schema["columns"]
        }
    else:
        return {
            col["name"]: col["type"] for col in schema["columns"]
            if not col.get("meta", {}).get("partition")
        }


def get_columns_with_comments(schema):
    """Returns dict of columns with their comments"""
    return {
        col["name"]: col["description"]
        for col in schema["columns"]
    }


def get_sql_columns_with_comments(schema):
    """Returns string of non partition columns with type and comments"""
    result = (
        ", ".join([f"{col['name']} {col['type']} COMMENT '{col['description']}'"
        for col in schema["columns"]])
    )
    return result

def get_sql_partition_columns(schema):
    """Returns string of partition columns with type and comments"""
    result = (
        ", ".join([f"{col['name']}"
        for col in schema["columns"] if col.get("meta", {}).get("partition")])
    )
    return result

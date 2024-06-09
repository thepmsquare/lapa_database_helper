from lapa_database_helper.main import LAPADatabaseHelper

lapa_database_helper = LAPADatabaseHelper()

# Example: Insert Rows
insert_data = [
    {"test_text": "example"},
]
insert_output = lapa_database_helper.insert_rows(
    insert_data, "lapa_testing", "public", "test"
)
print(insert_output)

# Example: Get Rows
get_filters = {}
get_output = lapa_database_helper.get_rows(
    get_filters,
    "lapa_testing",
    "public",
    "test",
    ignore_filters_and_get_all=True,
)
print(get_output)

# Example: Edit Rows
edit_data = {"test_text": "edited"}
edit_filters = {"test_text": "example"}
edit_output = lapa_database_helper.edit_rows(
    edit_data, edit_filters, "lapa_testing", "public", "test"
)
print(edit_output)

# Example: Delete Rows
delete_filters = {"test_text": "edited"}
delete_output = lapa_database_helper.delete_rows(
    delete_filters, "lapa_testing", "public", "test"
)
print(delete_output)

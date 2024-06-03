from lapa_database_helper.main import LAPADatabaseHelper

lapa_database_helper = LAPADatabaseHelper()

# Example: Insert Rows
insert_data = [
    {"device_encrypted_mac_address": "example"},
]
insert_output = lapa_database_helper.insert_rows(
    insert_data, "lapa_testing", "authentication", "device"
)
print(insert_output)

# Example: Get Rows
get_filters = {}
get_output = lapa_database_helper.get_rows(
    get_filters,
    "lapa_testing",
    "authentication",
    "device",
    ignore_filters_and_get_all=True,
)
print(get_output)

# Example: Edit Rows
edit_data = {"device_encrypted_mac_address": "edited"}
edit_filters = {"device_encrypted_mac_address": "example"}
edit_output = lapa_database_helper.edit_rows(
    edit_data, edit_filters, "lapa_testing", "authentication", "device"
)
print(edit_output)

# Example: Delete Rows
delete_filters = {"device_encrypted_mac_address": "edited"}
delete_output = lapa_database_helper.delete_rows(
    delete_filters, "lapa_testing", "authentication", "device"
)
print(delete_output)

from lapa_database_helper.main import LAPADatabaseHelper

lapa_database_helper = LAPADatabaseHelper()

# Example: Insert Rows
insert_data = [
    {"game_name": "example"},
]
insert_output = lapa_database_helper.insert_rows(insert_data, "game", "public", "game")
print(insert_output)

# Example: Get Rows
get_filters = {}
get_output = lapa_database_helper.get_rows(get_filters, "game", "public", "game")
print(get_output)

# Example: Edit Rows
edit_data = {"game_name": "edited"}
edit_filters = {"game_name": "example"}
edit_output = lapa_database_helper.edit_rows(
    edit_data, edit_filters, "game", "public", "game"
)
print(edit_output)

# Example: Delete Rows
delete_filters = {"game_name": "edited"}
delete_output = lapa_database_helper.delete_rows(
    delete_filters, "game", "public", "game"
)
print(delete_output)

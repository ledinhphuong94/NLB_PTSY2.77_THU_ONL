# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QTextEdit
# import json
# app = QApplication([])

# notes = {
#     "note 1": {
#         "text": "hello how are you",
#         "tags": ["Hi", "good"]
#     }
# }

# with open("test_notes.json", "w") as file:
#     json.dump(notes, file)

# # create the application window
# notes_win = QWidget()
# notes_win.setWindowTitle("Smart note app")
# notes_win.resize(900, 600)

# # widget of the application
# list_notes = QListWidget()
# list_notes_label = QLabel("List of notes")
# button_note_create = QPushButton("Create note")
# button_note_del = QPushButton("Delete note")
# button_note_save = QPushButton("Save note")

# field_tag = QLineEdit('')
# field_tag.setPlaceholderText("Enter tag...")
# button_tag_add = QPushButton("Add to note")
# button_tag_del = QPushButton("Untag from note")
# button_tag_search = QPushButton("Search notes by tag")
# list_tags = QListWidget()

# field_text = QTextEdit()

# # arrange the layout
# layout_notes = QHBoxLayout()
# col_1 = QVBoxLayout()
# col_1.addWidget(field_text)

# col_2 = QVBoxLayout()
# col_2.addWidget(list_notes)

# notes_win.show()
# app.exec_()

import json

# with open("testJson.json", "r") as file:
#     data = json.load(file)
#     print(data["note 1"])

notes = {
    "note 1": {
        "text": "hello how are you",
        "tags": ["Hi", "good"]
    }
}
with open("notes.json", "w") as file:
    json.dump(notes, file)
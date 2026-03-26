from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QTextEdit, QInputDialog
import json
app = QApplication([])

notes = {
    "sample note 1": {
        "text": "this is my first note",
        "tags": ["hello", "hi"]
    },
    "sample note 2": {
        "text": "this is my second note",
        "tags": ["ok", "hi"]
    },
}

# App interface
# App window
notes_win = QWidget()
notes_win.setWindowTitle("Smart Notes")
notes_win.resize(900, 600)

# 1. app widgets
# text field
field_text = QTextEdit()

# list notes area
list_notes_label = QLabel("List of notes")
list_notes = QListWidget()
# list notes buttons
button_note_create = QPushButton('Create note')
button_note_del = QPushButton('Delete note')
button_note_save = QPushButton('Save note')

# list tags area
list_tags_label = QLabel("List of tags")
list_tags = QListWidget()
field_tag = QLineEdit('')
field_tag.setPlaceholderText("Enter tag...")
# list tags buttons
button_tag_create = QPushButton('Add to note')
button_tag_del = QPushButton('Untag from note')
button_tag_search = QPushButton('Search notes by tag')

# 2. arrange of widgets by layouts
layout_notes = QHBoxLayout()
# on the left side
col_1 = QVBoxLayout()
col_1.addWidget(field_text)

# on the right side
# ===== add the list notes =====
col_2 = QVBoxLayout()
col_2_notes = QVBoxLayout()
col_2_notes.addWidget(list_notes_label)
col_2_notes.addWidget(list_notes)
# Add buttons
col_2_btn_row_1 = QHBoxLayout()
col_2_btn_row_1.addWidget(button_note_create)
col_2_btn_row_1.addWidget(button_note_del)
col_2_btn_row_2 = QHBoxLayout()
col_2_btn_row_2.addWidget(button_note_save)
col_2_notes.addLayout(col_2_btn_row_1)
col_2_notes.addLayout(col_2_btn_row_2)

# ===== add the list tags =====
col_2_tags = QVBoxLayout()
col_2_tags.addWidget(list_tags_label)
col_2_tags.addWidget(list_tags)
col_2_tags.addWidget(field_tag)
# add buttons for tags
col_2_btn_row_3 = QHBoxLayout()
col_2_btn_row_3.addWidget(button_tag_create)
col_2_btn_row_3.addWidget(button_tag_del)
col_2_btn_row_4 = QHBoxLayout()
col_2_btn_row_4.addWidget(button_tag_search)
col_2_tags.addLayout(col_2_btn_row_3)
col_2_tags.addLayout(col_2_btn_row_4)

# Add list note and list tags into col 2
col_2.addLayout(col_2_notes)
col_2.addLayout(col_2_tags)

# Add col_1 & col_2 
layout_notes.addLayout(col_1)
layout_notes.addLayout(col_2)
notes_win.setLayout(layout_notes)

notes_win.show()

# with open("smartNote.json", "w") as file:
#     json.dump(notes, file, sort_keys=True)

# function show note
def showNote():
    # Get the key selected text in the widget list
    clickedKey = list_notes.selectedItems()[0].text()
    # get text and tags from dictionary notes
    textNote = notes[clickedKey]["text"]
    tags = notes[clickedKey]["tags"]
    # Add the text into field text widget
    field_text.setText(textNote)
    # Clear all the current tags
    list_tags.clear()
    # Add the tags into list widget tags
    list_tags.addItems(tags)

# Event listener 
list_notes.itemClicked.connect(showNote)

# Open the json file and store into "notes" variable
with open("smartNote.json", "r") as file:
    notes = json.load(file)
# make the notes appear in the widget

list_notes.addItems(notes.keys())

app.exec_()

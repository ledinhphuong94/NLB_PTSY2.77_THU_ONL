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


















# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QTextEdit, QInputDialog
# import json
# app = QApplication([])
# notes = {
#     "First note": {
#         "content": "Hello world!",
#         "tags": ["hihi", "hehe"]
#     },
#     "Sencond note": {
#         "content": "Hi world 2!",
#         "tags": ["22", "zzz"]
#     }
# }
# # App interface
# # App window
# notes_win = QWidget()
# notes_win.setWindowTitle("Smart Notes")
# notes_win.resize(900, 600)

# # 1. app widgets
# # text field
# field_text = QTextEdit()

# # list notes area
# list_notes_label = QLabel("List of notes")
# list_notes = QListWidget()
# # list notes buttons
# button_note_create = QPushButton('Create note')
# button_note_del = QPushButton('Delete note')
# button_note_save = QPushButton('Save note')

# # list tags area
# list_tags_label = QLabel("List of tags")
# list_tags = QListWidget()
# field_tag = QLineEdit('')
# field_tag.setPlaceholderText("Enter tag...")
# # list tags buttons
# button_tag_create = QPushButton('Add to note')
# button_tag_del = QPushButton('Untag from note')
# button_tag_search = QPushButton('Search notes by tag')

# # 2. arrange of widgets by layouts
# layout_notes = QHBoxLayout()
# # on the left side
# col_1 = QVBoxLayout()
# col_1.addWidget(field_text)

# # on the right side
# # ============ add the list notes ============
# col_2 = QVBoxLayout()
# col_2_notes = QVBoxLayout()
# col_2_notes.addWidget(list_notes_label)
# col_2_notes.addWidget(list_notes)
# # Add buttons
# col_2_btn_row_1 = QHBoxLayout()
# col_2_btn_row_1.addWidget(button_note_create)
# col_2_btn_row_1.addWidget(button_note_del)
# col_2_btn_row_2 = QHBoxLayout()
# col_2_btn_row_2.addWidget(button_note_save)
# col_2_notes.addLayout(col_2_btn_row_1)
# col_2_notes.addLayout(col_2_btn_row_2)

# #  ============ add the list tags ============
# col_2_tags = QVBoxLayout()
# col_2_tags.addWidget(list_tags_label)
# col_2_tags.addWidget(list_tags)
# col_2_tags.addWidget(field_tag)
# # Add buttons
# col_2_btn_row_3 = QHBoxLayout()
# col_2_btn_row_3.addWidget(button_tag_create)
# col_2_btn_row_3.addWidget(button_tag_del)
# col_2_btn_row_4 = QHBoxLayout()
# col_2_btn_row_4.addWidget(button_tag_search)
# col_2_tags.addLayout(col_2_btn_row_3)
# col_2_tags.addLayout(col_2_btn_row_4)


# # Add list note and list tags into col 2
# col_2.addLayout(col_2_notes)
# col_2.addLayout(col_2_tags)

# # Add col_1 & col_2 
# layout_notes.addLayout(col_1)
# layout_notes.addLayout(col_2)
# notes_win.setLayout(layout_notes)

# # function
# # Add note
# def show_note():
#     title = list_notes.selectedItems()[0].text()
#     content = notes[title]["content"]
#     tags = notes[title]["tags"]
#     field_text.setText(content)
#     list_tags.clear()
#     list_tags.addItems(tags)

# def create_note():
#     name, isOk = QInputDialog.getText(notes_win, "Add note", "Note name: ")
#     if name != '' and isOk:
#         notes[name] = {
#             "content": "",
#             "tags": []
#         }
#         list_notes.addItem(name)
#         with open("notes_data.json", "w") as file:
#             json.dump(notes, file, sort_keys=True)

# def delete_note():
#     if not list_notes.selectedItems():
#         print("Please select note first")
#         return
#     note_name = list_notes.selectedItems()[0].text()
#     del notes[note_name]
#     list_notes.clear()
#     list_tags.clear()
#     field_text.clear()
#     list_notes.addItems(notes.keys())
#     with open("notes_data.json", "w") as file:
#         json.dump(notes, file, sort_keys=True)

# def save_note():
#     if not list_notes.selectedItems():
#         print("Please select note first")
#         return
#     note_name = list_notes.selectedItems()[0].text()
#     text = field_text.toPlainText()
#     notes[note_name]["content"] = text
#     with open("notes_data.json", "w") as file:
#         json.dump(notes, file, sort_keys=True)

# def add_tag():
#     if not list_notes.selectedItems():
#         print("Please select note first")
#         return
#     note_name = list_notes.selectedItems()[0].text()
#     tag_name = field_tag.text()
#     if not tag_name in notes[note_name]["tags"]:
#         notes[note_name]["tags"].append(tag_name)
#         list_tags.addItem(tag_name)
#         field_tag.clear()
#         with open("notes_data.json", "w") as file:
#             json.dump(notes, file, sort_keys=True)

# def un_tag():
#     if not list_notes.selectedItems():
#         print("Please select note first")
#         return
#     if not list_tags.selectedItems():
#         print("Please select tag first")
#         return
#     note_name = list_notes.selectedItems()[0].text()
#     tag_name = list_tags.selectedItems()[0].text()
#     notes[note_name]["tags"].remove(tag_name)
#     list_tags.clear()
#     list_tags.addItems(notes[note_name]["tags"])

#     with open("notes_data.json", "w") as file:
#         json.dump(notes, file, sort_keys=True)

# def search_note_by_tag():
#     search_result = {}
#     tag_name = field_tag.text()
#     if tag_name == '':
#         list_notes.clear()
#         list_notes.addItems(notes.keys())
#     else:
#         print("tag_name", tag_name)
#         for key in notes:
#             tagList = notes[key]["tags"]
#             print('tagList', tagList)
#             if tag_name in tagList:
#                 search_result[key] = notes[key]
#                 list_notes.clear()
#                 list_notes.addItems(search_result.keys())
#     field_text.clear()
#     list_tags.clear()

# # Add event listner
# list_notes.itemClicked.connect(show_note)
# button_note_create.clicked.connect(create_note)
# button_note_save.clicked.connect(save_note)
# button_note_del.clicked.connect(delete_note)

# button_tag_create.clicked.connect(add_tag)
# button_tag_del.clicked.connect(un_tag)
# button_tag_search.clicked.connect(search_note_by_tag)

# with open("notes_data.json", "r") as file:
#     notes = json.load(file)
#     print(notes)

# list_notes.addItems(notes.keys())

# notes_win.show()
# app.exec_()
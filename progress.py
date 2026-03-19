from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QTextEdit, QInputDialog
import json
app = QApplication([])

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
button_tag_save = QPushButton('Search notes by tag')

# 2. arrange of widgets by layouts
layout_notes = QHBoxLayout()
# on the left side
col_1 = QVBoxLayout()
col_1.addWidget(field_text)

# on the right side
# add the list notes
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

# add the list tags
col_2_tags = QVBoxLayout()

# Add list note and list tags into col 2
col_2.addLayout(col_2_notes)
col_2.addLayout(col_2_tags)

# Add col_1 & col_2 
layout_notes.addLayout(col_1)
layout_notes.addLayout(col_2)
notes_win.setLayout(layout_notes)

notes_win.show()
app.exec_()
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
builder = Gtk.Builder()
builder.add_from_file("UI/remmindor.ui")

###
### example_structure: ID, "Reminder Name ID", [Reminder Information]

reminders = []          #Local Reminder Structure

selectedReminder = -1   #Current Selected Reminder that gets edited

def getCurrentElementIndex(button):
    for r in reminders:
        if button.get_label() == r[1]:
            selectedReminder = r[0]
            tmp = builder.get_object("nameReminder")
            print(tmp.set_text(button.get_label()))
            break
    pass



def saveReminder(button):
    pass

    


def addReminder(button):
    newestID = len(reminders)
    newReminder = newestID, "New Reminder " + str(newestID + 1), []
    reminders.append(newReminder)

    reminderButton = Gtk.Button(label=newReminder[1])
    reminderButton.connect("clicked", getCurrentElementIndex)


    builder.get_object("reminderBox").add(reminderButton)
    window.show_all()

    selectedReminder = newestID
    print(newestID)


def lockReminder(button):
    pass


class MainApplication(Gtk.Window):
    def __init__(self):
        super().__init__(title="Remmindor")

####??????????????????????????????
    ##Spinner Init cause idk how to do in Cambalache
        adj = Gtk.Adjustment(upper=100, step_increment=1, page_increment=10)
        spinnerMinutes = builder.get_object("timeMinutes")
        spinnerMinutes.set_adjustment(adj)

    def on_value_changed(self, scroll):
        print("Hello World")
        print(self.spinbutton.get_value_as_int())


generalHandlers = {
    "onDestroy": Gtk.main_quit,
    "onSaveClicked": saveReminder,
    "onAddClicked": addReminder,
    "onDeleteClicked": Gtk.main_quit,
}

###

builder.connect_signals(generalHandlers)
window = builder.get_object("MainWindow")
window.show_all()
Gtk.main()
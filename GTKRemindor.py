import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
builder = Gtk.Builder()
builder.add_from_file("UI/remmindor.ui")

###
### example_structure: ID,[Reminder Information]

reminders = []          #Local Reminder Dictionary
selectedReminder = 0
#Current Selected Reminder that gets edited


def lockReminder(button):
    pass


class MainApplication(Gtk.Window):
    def __init__(self):
        super().__init__(title="Remmindor")

    def loadReminder():
        global reminders
        global selectedReminder

        data = dict(reminders[int(selectedReminder)])
        print(data)
        builder.get_object("nameReminder").set_text(data['name'])
        builder.get_object("monday").set_active(bool(data['monday'])),
        # "tuesday" : builder.get_object("tuesday").get_active(),
        # "wednesday" : builder.get_object("wednesday").get_active(),
        # "thursday" : builder.get_object("thursday").get_active(),
        # "friday" : builder.get_object("friday").get_active(),
        # "saturday" : builder.get_object("saturday").get_active(),
        # "sunday" : builder.get_object("sunday").get_active(),
        # "timeHours" : builder.get_object("timeHours").get_text(),
        # "timeMinutes" : builder.get_object("timeMinutes").get_text(),
        # "isRepeat" : builder.get_object("isRepeat").get_active(),
        # "reminderText" : builder.get_object("reminderText").get_buffer(),

    def getCurrentElementIndex(button):
        global selectedReminder
        selectedReminder = button.get_name()
        if reminders[int(selectedReminder)]:
            MainApplication.loadReminder()
            ##button.set_label(builder.get_object("nameReminder").get_text())
            return
        else:
            MainApplication.deselect()
        
        tmp = builder.get_object("nameReminder")
        tmp.set_text(button.get_label())


    def deselect():
        builder.get_object("monday").set_active(False)
        builder.get_object("tuesday").set_active(False)
        builder.get_object("wednesday").set_active(False)
        builder.get_object("thursday").set_active(False)
        builder.get_object("friday").set_active(False)
        builder.get_object("saturday").set_active(False)
        builder.get_object("sunday").set_active(False)
        builder.get_object("timeHours").set_text("0")
        builder.get_object("timeMinutes").set_text("0")
        builder.get_object("isRepeat").set_active(False)
        builder.get_object("reminderText").set_buffer(Gtk.TextBuffer())

    def saveReminder(button):
        global selectedReminder
        global reminders

        for btn in builder.get_object('reminderBox'):
            if btn.get_name() == selectedReminder:
                btn.set_label(builder.get_object("nameReminder").get_text())

        data = {
            "name": builder.get_object("nameReminder").get_text(),
            "monday" : builder.get_object("monday").get_active(),
            "tuesday" : builder.get_object("tuesday").get_active(),
            "wednesday" : builder.get_object("wednesday").get_active(),
            "thursday" : builder.get_object("thursday").get_active(),
            "friday" : builder.get_object("friday").get_active(),
            "saturday" : builder.get_object("saturday").get_active(),
            "sunday" : builder.get_object("sunday").get_active(),
            "timeHours" : builder.get_object("timeHours").get_text(),
            "timeMinutes" : builder.get_object("timeMinutes").get_text(),
            "isRepeat" : builder.get_object("isRepeat").get_active(),
            "reminderText" : builder.get_object("reminderText").get_buffer(),
        }
        
        reminders[int(selectedReminder)] = list(data.items())
        

    def addReminder(button):
        global reminders
        global selectedReminder

        newestID = len(reminders)
        newReminder = []
        reminders.append(newReminder)

        reminderButton = Gtk.Button(label="New Reminder " + str(newestID + 1), name=newestID)
        reminderButton.connect("clicked", MainApplication.getCurrentElementIndex)


        builder.get_object("reminderBox").add(reminderButton)
        window.show_all()

        selectedReminder = newestID
        print(reminders)


generalHandlers = {
    "onDestroy": Gtk.main_quit,
    "onSaveClicked": MainApplication.saveReminder,
    "onAddClicked": MainApplication.addReminder,
    "onDeleteClicked": Gtk.main_quit,
}

###

builder.connect_signals(generalHandlers)
window = builder.get_object("MainWindow")
window.show_all()
Gtk.main()
import gi, json

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from pathlib import Path
builder = Gtk.Builder()
builder.add_from_file("UI/remmindor.ui")

reminders = []          #Local Reminder Dictionary
selectedReminder = -1    #Current Selected Reminder that gets edited

def lockReminder(button):
    pass


class Remmindor(Gtk.Window):
    def __init__(self):
        super().__init__(title="Remmindor")

    def loadReminder():
        global reminders
        global selectedReminder

        data = dict(reminders[int(selectedReminder)])

        text = Gtk.TextBuffer().new()
        text.set_text(data['reminderText'])

        builder.get_object("nameReminder").set_text(data['name'])
        builder.get_object("monday").set_active(bool(data['monday'])),
        builder.get_object("tuesday").set_active(bool(data['tuesday'])),
        builder.get_object("wednesday").set_active(bool(data['wednesday'])),
        builder.get_object("thursday").set_active(bool(data['thursday'])),
        builder.get_object("friday").set_active(bool(data['friday'])),
        builder.get_object("saturday").set_active(bool(data['saturday'])),
        builder.get_object("sunday").set_active(bool(data['sunday'])),
        builder.get_object("timeHours").set_text(data['timeHours']),
        builder.get_object("timeMinutes").set_text(data['timeMinutes']),
        builder.get_object("isRepeat").set_active(bool(data['isRepeat'])),
        builder.get_object("reminderText").set_buffer(text),

    def getCurrentElementIndex(button):
        global selectedReminder
        selectedReminder = button.get_name()
        if reminders[int(selectedReminder)]:
            Remmindor.loadReminder()
            ##button.set_label(builder.get_object("nameReminder").get_text())
            return
        else:
            Remmindor.deselect()
        
        tmp = builder.get_object("nameReminder")
        tmp.set_text(button.get_label())

    def deselect():
        global selectedReminder
        builder.get_object("nameReminder").set_text("")
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
        #selectedReminder = -1

    def saveReminder(button):
        global selectedReminder
        global reminders

        if selectedReminder == -1:
            return

        for btn in builder.get_object('reminderBox'):
            if btn.get_name() == selectedReminder:
                btn.set_label(builder.get_object("nameReminder").get_text())

        buffer = builder.get_object("reminderText").get_buffer()

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
            "reminderText" : buffer.get_text(buffer.get_start_iter(), buffer.get_end_iter(), True)
        }
        reminders[int(selectedReminder)] = list(data.items())

        Remmindor.save()

    def save():
        # Serializing json
        json_object = json.dumps(reminders, indent=None)
        
        # Writing to sample.json
        with open("data/data.rem","w") as outfile:
            outfile.write(json_object)

        #print(reminders)
        
    def addReminder(button):
        global reminders
        global selectedReminder

        newestID = len(reminders)
        newReminder = []
        reminders.append(newReminder)

        reminderButton = Gtk.Button(label="New Reminder " + str(newestID + 1), name=newestID)
        reminderButton.connect("clicked", Remmindor.getCurrentElementIndex)

        builder.get_object("reminderBox").add(reminderButton)

        window.show_all()

        selectedReminder = newestID
        #print(reminders)

    def loadSavedReminders():
        global reminders
        file = Path("data/data.rem")
        if not file.exists():
            return

        reminders = json.load(open('data/data.rem'))
        index = 0
        for r in reminders:
            if not r:
                btn = Gtk.Button(label="New Reminder "+ str(index), name=index)
                
            else:
                btnname = r[0][1]
                btn = Gtk.Button(label=btnname, name=index)
            btn.connect("clicked", Remmindor.getCurrentElementIndex)
            builder.get_object("reminderBox").add(btn)
            index +=1

    def deleteReminder(button):
        global reminders
        global selectedReminder

        if selectedReminder == -1:
            return 

        print(reminders)

        reminders.pop(int(selectedReminder))
        Remmindor.save()

        l = builder.get_object("reminderBox")

        for child in l:
            l.remove(child)

        Remmindor.loadSavedReminders()
        window.show_all()
        Remmindor.deselect()
        selectedReminder = -1


generalHandlers = {
    "onDestroy": Gtk.main_quit,
    "onSaveClicked": Remmindor.saveReminder,
    "onAddClicked": Remmindor.addReminder,
    "onDeleteClicked": Remmindor.deleteReminder,
}

###

Remmindor.loadSavedReminders()

builder.connect_signals(generalHandlers)
window = builder.get_object("MainWindow")
window.show_all()
Gtk.main()
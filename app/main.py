import pickle
from tkinter import *
from tkinter import messagebox 
from tkinter import filedialog
from datetime import datetime
from abc import ABC, abstractmethod
try:
    from tkcalendar import Calendar
except:
    warning = "In order to use the set deadline button, install tkcalendar by typing \"pip install tkcalendar\" in your terminal."
    print(warning)
    messagebox.showwarning("Warning", warning) 

class Date(object):
    def get_date_diff(self, deadline):
        #get today's date
        today = datetime.now().strftime("%d/%m/%Y")

        #convert string to date object
        d1 = datetime.strptime(today, "%d/%m/%Y")
        try:
            d2 = datetime.strptime(deadline, "%d/%m/%Y")
        except:
            return float("inf")
        
        difference = d2 - d1
        return difference.days
    

class StatsWindow(ABC, Toplevel):
    def __init__(self, parent, title, stats):
        super().__init__(parent)
        self.parent = parent
        self.title(title)
        self.geometry("550x200")
        self.minsize(550, 200)
        self.stats = stats

        #create margins
        self.margin_top = Frame(self, height=15)
        self.margin_1 = Frame(self, width=15)
        self.margin_2 = Frame(self, width=15)
        self.margin_3 = Frame(self, width=15)
        self.margin_bottom = Frame(self, height=15)
        self.margin_top.grid(row=1, column=1, columnspan=7)
        self.margin_1.grid(row=2, column=1, sticky=W)
        self.margin_2.grid(row=2, column=3)
        self.margin_3.grid(row=2, column=5, sticky=E)
        self.margin_bottom.grid(row=3, column=1, columnspan=7)

        #expand margins
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(3, weight=1)

    @abstractmethod
    def create_stats(self):
        pass

    def create_stat_labels(self, frame, labels):
        row = 2
        for label in labels:
            label_name = label["name"]
            label_text = label["text"]
            label_value = Label(frame, text=label_text, background="#faf5ef")
            label_value.grid(row=row, column=1, sticky=W)
            value = Label(frame, text=self.stats.get(label_name, "-"), background="#faf5ef")
            value.grid(row=row, column=2, sticky=E)
            row += 1

        #expand widgets in frame
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)


class GeneralStatsWindow(StatsWindow):
    def __init__(self, parent, title, stats):
        super().__init__(parent, title, stats)
        self.geometry("280x150")
        self.minsize(280, 150)

        self.create_stats()
        self.margin_3.grid_forget()

    def create_stats(self):
        gen_frame = Frame(
            self,
            highlightbackground="black",
            highlightthickness=2,
            padx=15,
            pady=15,
            background="#faf5ef"
        )
        gen_frame.grid(row=2, column=2, sticky=EW)
        # expand frame horizontally
        self.grid_columnconfigure(2, weight=1)

        gen_label = Label(
            gen_frame, text="General Statistics", width=30, 
            font=("Helvetica", 9, "bold"), background="#faf5ef"
        )
        gen_label.grid(row=1, column=1, columnspan=2, pady=(0, 10))

        labels = [
            {"name": "active", "text": "Active:"},
            {"name": "completed", "text": "Completed:"},
            {"name": "total", "text": "Total:"}
        ]
        self.create_stat_labels(gen_frame, labels)


class PriorityStatsWindow(StatsWindow):
    def __init__(self, parent, title, stats):
        super().__init__(parent, title, stats)
        self.create_stats()
        # expand frames horizontally
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(4, weight=1)

    def create_stats(self):
        active_frame = Frame(
            self,
            highlightbackground="black",
            highlightthickness=2,
            padx=15,
            pady=15,
            background="#faf5ef"
        )
        active_frame.grid(row=2, column=2, sticky=EW)

        prio_label = Label(
            active_frame, text="Current Priority Statistics", width=30, 
            font=("Helvetica", 9, "bold"), background="#faf5ef"
        )
        prio_label.grid(row=1, column=1, columnspan=2, pady=(0, 10))

        labels = [
            {"name": "prio_high", "text": "High:"},
            {"name": "prio_medium", "text": "Medium:"},
            {"name": "prio_low", "text": "Low:"},
            {"name": "prio_none", "text": "None:"}
        ]
        self.create_stat_labels(active_frame, labels)

        total_frame = Frame(
            self,
            highlightbackground="black",
            highlightthickness=2,
            padx=15,
            pady=15,
            background="#faf5ef"
        )
        total_frame.grid(row=2, column=4, sticky=EW)

        prio_label = Label(
            total_frame, text="Total Priority Statistics", width=30, 
            font=("Helvetica", 9, "bold"), background="#faf5ef"
        )
        prio_label.grid(row=1, column=1, columnspan=2, pady=(0, 10))

        labels = [
            {"name": "prio_high_all", "text": "High:"},
            {"name": "prio_medium_all", "text": "Medium:"},
            {"name": "prio_low_all", "text": "Low:"},
            {"name": "prio_none_all", "text": "None:"}
        ]
        self.create_stat_labels(total_frame, labels)


class TagsStatsWindow(StatsWindow):
    def __init__(self, parent, title, stats):
        super().__init__(parent, title, stats)
        self.create_stats()
        # expand frames horizontally
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(4, weight=1)

    def create_stats(self):
        active_frame = Frame(
            self,
            highlightbackground="black",
            highlightthickness=2,
            padx=15,
            pady=15,
            background="#faf5ef"
        )
        active_frame.grid(row=2, column=2, sticky=EW)

        tags_label = Label(
            active_frame, text="Current Tags Statistics", width=30, 
            font=("Helvetica", 9, "bold"), background="#faf5ef"
        )
        tags_label.grid(row=1, column=1, columnspan=2, pady=(0, 10))

        labels = [
            {"name": "tag_personal", "text": "Personal:"},
            {"name": "tag_family", "text": "Family:"},
            {"name": "tag_friend", "text": "Friend:"},
            {"name": "tag_work", "text": "Work:"},
            {"name": "tag_entertainment", "text": "Entertainment:"}
        ]
        self.create_stat_labels(active_frame, labels)

        total_frame = Frame(
            self,
            highlightbackground="black",
            highlightthickness=2,
            padx=15,
            pady=15,
            background="#faf5ef"
        )
        total_frame.grid(row=2, column=4, sticky=EW)

        tags_all_label = Label(
            total_frame, text="Total Tags Statistics", width=30, 
            font=("Helvetica", 9, "bold"), background="#faf5ef"
        )
        tags_all_label.grid(row=1, column=1, columnspan=2, pady=(0, 10))

        labels = [
            {"name": "tag_personal_all", "text": "Personal:"},
            {"name": "tag_family_all", "text": "Family:"},
            {"name": "tag_friend_all", "text": "Friend:"},
            {"name": "tag_work_all", "text": "Work:"},
            {"name": "tag_entertainment_all", "text": "Entertainment:"}
        ]
        self.create_stat_labels(total_frame, labels)


class TaskCreator(Frame, Date):
    def __init__(self, parent, task_display):
        super().__init__(parent)
        self.parent = parent
        self.task_display = task_display

        #frame decoration
        self.config(
            highlightbackground="black", 
            highlightthickness=2, 
            background="#faf5ef",
            padx=15, 
            pady=10
        )

        #title
        title = Label(self, text="Create Task", background="#faf5ef", font=("Berlin Sans FB Demi", 12, "bold"))
        title.grid(row=0, column=1, columnspan=6, pady=(0, 10))

        #task input section
        task_label = Label(
            self, text="Insert Task", background="#fff1e6", width=8,
            highlightbackground="gray", highlightthickness=1
        )
        task_label.grid(row=1, column=1, sticky=NW, padx=(0, 5))
        self.task_input = Text(self, width=40, height=3)
        self.task_input.grid(row=1, column=2, columnspan=5)

        #deadline section
        self.deadline = StringVar(value="")
        deadline_label = Label(
            self, text="Deadline", background="#fff1e6", width=8,
            highlightbackground="gray", highlightthickness=1
        )
        deadline_button = Button(self, text="Set Deadline", bg="#ffcbd1", bd=1, command=self.open_calendar)
        deadline_display = Label(self, background="#faf5ef", textvariable=self.deadline, width=8)
        deadline_remove = Button(
            self, text=" X ", bg="#ED2939", fg="white", bd=1, command=lambda: self.deadline.set("")
        )
        deadline_label.grid(row=2, column=1, sticky=W, padx=(0,5), pady=10)
        deadline_button.grid(row=2, column=2, sticky=W, pady=10)
        deadline_display.grid(row=2, column=3, columnspan=3, sticky=W, padx=5)
        deadline_remove.grid(row=2, column=6, sticky=W, padx=(25,0))

        #priority section(default is None)
        priority_label = Label(
            self, text="Priority", background="#fff1e6", width=8,
            highlightbackground="gray", highlightthickness=1
        )
        priority_label.grid(row=3, column=1, sticky=W)
        text_to_value = {
            "None": "gray",
            "Low": "blue",
            "Medium": "#FFD700",
            "High": "red"
        }
        self.radio_var_priority = StringVar(value="gray")
        for i, (text, value) in enumerate(text_to_value.items()):
            radio = Radiobutton(
                self, 
                text=text, 
                variable=self.radio_var_priority, 
                value=value,
                fg=value,
                background="#faf5ef"
            )
            radio.grid(row=3, column=i+2, sticky=W)

        #color section(default is black)
        text_color_label = Label(
            self, text="Text Color", background="#fff1e6", width=8,
            highlightbackground="gray", highlightthickness=1
        )
        text_color_label.grid(row=4, column=1, sticky=W)
        color_to_value = {
            "Black": "black",
            "Blue": "#271571",
            "Red": "#960018"
        }
        self.radio_var_color = StringVar(value="black")
        for i, (color, value) in enumerate(color_to_value.items()):
            radio = Radiobutton(
                self, 
                text=color, 
                variable=self.radio_var_color, 
                value=value,
                fg=value,
                background="#faf5ef"
            )
            radio.grid(row=4, column=i+2, sticky=W)

        #tags section
        tags_label = Label(
            self, text="Tags", background="#fff1e6", width=8,
            highlightbackground="gray", highlightthickness=1
        )
        tags_label.grid(row=5, column=1, sticky=W)
        self.checkboxes = {}
        tags = ["Personal", "Family", "Friend", "Work", "Entertainment"]
        for i, tag in enumerate(tags):
            self.on_off = IntVar()
            checkbox = Checkbutton(
                self, text=tag, background="#faf5ef", variable=self.on_off, onvalue=1, offvalue=0
                )
            if i < 3:
                checkbox.grid(row=5, column=i+2, sticky=W)
            elif tag == "Entertainment":
                checkbox.grid(row=6, column=i-1, columnspan=2, sticky=W)
            else:
                checkbox.grid(row=6, column=i-1, sticky=W)
            self.checkboxes[tag] = self.on_off

        #task button section
        create_task_button = Button(
            self, text="Create Task", bg="#ffcf07", highlightbackground="black", highlightthickness=1,
            bd=1, anchor=CENTER, command=self.create_activity
        )
        create_task_button.grid(row=7, column=3, pady=(10, 0))

        #undo button
        undo_button = Button(
            self, text="Undo", fg="white", bg="#4361EE", bd=1, command=self.undo
        )
        undo_button.grid(row=7, column=6, pady=(10, 0), sticky=E)

    def create_activity(self):
        task = self.get_task_input()
        prio = self.get_priority_input()
        color = self.get_color_input()
        tags = self.get_tags_input()
        deadline = self.get_deadline()
        if task == "":
            messagebox.showerror("Error", "Please enter a task.")
            return

        self.task_display.add_activity(task, prio, color, tags, deadline)
        self.reset_form()

    def open_calendar(self):
        calendar = CalendarWindow(self)
        self.parent.wait_window(calendar)

    def get_task_input(self):
        return self.task_input.get("1.0", "end-1c")

    def get_priority_input(self):
        return self.radio_var_priority.get()

    def get_color_input(self):
        return self.radio_var_color.get()
    
    def get_tags_input(self):
        checkboxes_true_values = {}
        for tag in self.checkboxes:
            checkboxes_true_values[tag] = self.checkboxes[tag].get()

        return checkboxes_true_values
    
    def get_deadline(self):
        return self.deadline.get()
    
    def reset_form(self):
        self.task_input.delete("1.0", END)
        self.radio_var_priority.set(value="gray")
        self.radio_var_color.set(value="black")
        for tag in self.checkboxes:
            self.checkboxes[tag].set(0)
        self.deadline.set("")

    def undo(self):
        try:
            frame = self.task_display.completed
            if frame[-1].cget("highlightthickness") != 2:
                messagebox.showerror("Error", "Cannot undo loaded tasks.")
                return
            completed_frame = frame.pop()
            self.task_display.activities.append(completed_frame)
            self.task_display.activities.sort(key=lambda frame: frame.sorting_key)
            self.task_display.arrange_activities()
            self.task_display.update_scrollwheel()
        except IndexError:
            messagebox.showerror("Error", "No tasks to undo.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to undo: {str(e)}")


class TaskDisplay(Frame, Date):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        #frame decoration
        self.config(
            highlightbackground="black",
            highlightthickness=2, 
            background="#faf5ef"
        )

        self.activityLabel = Label(self, text="Activities", background="#faf5ef", font=("Berlin Sans FB Demi", 12, "bold"))
        self.activityLabel.pack(pady=(10, 0))

        self.canvas = Canvas(self, width=352, height=500, background="#faf5ef", highlightthickness=0)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True, padx=(15, 0))

        self.scrollbar = Scrollbar(self, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set, background="#faf5ef")
        self.canvas.bind("<Configure>", self.update_scrollwheel)

        self.task_list_frame_inner = Frame(self.canvas, background="#faf5ef")
        self.task_list_frame_inner.pack(fill=BOTH, expand=True)
        self.canvas.create_window((0, 0), window=self.task_list_frame_inner, anchor=NW)

        self.activities = []
        self.completed = []

    def on_mousewheel(self, event):
        x, y = event.x_root, event.y_root
        if (self.canvas.winfo_rootx() <= x <= (self.canvas.winfo_rootx() + self.canvas.winfo_width()) and 
            self.canvas.winfo_rooty() <= y <= (self.canvas.winfo_rooty() + self.canvas.winfo_height()) and 
            len(self.activities) > 0
        ):
            self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def add_activity(self, task, prio, color, tags, deadline):
        #add container frame
        new_frame = Frame(
            self.task_list_frame_inner,
            highlightbackground=prio,
            highlightthickness=2,
            background="#fff1e6"
        )
        new_frame.grid(column=1, pady=2)

        #add task
        task_label = Label(
            new_frame,
            text=task,
            width=47,
            wraplength=330,
            justify=LEFT,
            anchor=W,
            fg=color,
            highlightbackground="black",
            highlightthickness=1,
            background="#ffffff"
        )
        task_label.grid(row=1, column=1, columnspan=5, padx=5, pady=5, sticky=W)

        #add deadline
        if deadline != "":
            deadline_label = Label(new_frame, text=deadline, fg="red", background="#fff1e6")
            deadline_label.grid(row=2, column=1, padx=5, sticky=W)

        #add tags
        if any(value == 1 for value in tags.values()):
            all_tags = ""
            for tag in tags:
                if tags[tag] == 1:
                    all_tags += f"#{tag}  "
            tag_label = Label(new_frame, text=all_tags, fg="orange", background="#fff1e6")
            tag_label.grid(row=3, column=1, padx=5, sticky=W)

        #add complete button
        complete_button = Button(
            new_frame,
            text="Complete",
            bg="#ffcf07",
            bd=1,
            command=lambda frame=new_frame: self.complete_activity(frame),
        )
        complete_button.grid(row=4, column=1, columnspan=5, pady=5)
        new_frame.grid_columnconfigure(1, weight=1)

        #add remove button
        remove_button = Button(
            new_frame,
            text=" X ",
            bg="#ED2939", 
            fg="white",
            bd=1,
            command=lambda frame=new_frame: self.remove_task(frame)
        )
        remove_button.grid(row=4, column=2, sticky=E, padx=5)

        #store each frame's data
        sorting_key = (self.get_date_diff(deadline), self.get_priority_value(prio))
        new_frame.sorting_key = sorting_key
        new_frame.task_label = task_label
        new_frame.deadline_label = deadline_label if deadline != "" else None
        new_frame.prio = prio
        new_frame.tags = tags
        self.activities.append(new_frame)

        #sort and update activities
        self.activities.sort(key=lambda frame: frame.sorting_key)
        self.arrange_activities()
        self.update_scrollwheel()

    def complete_activity(self, frame):
        self.completed.append(frame)
        self.activities.remove(frame)
        frame.grid_forget()
        self.task_list_frame_inner.configure(background="#faf5ef")
        self.arrange_activities()
        self.update_scrollwheel()

    def arrange_activities(self):
        for i, frame in enumerate(self.activities):
            frame.grid(row=i, column=1, sticky="ew")
    
    def get_priority_value(self, priority):
        priority_values = {
            "gray": 3,
            "blue": 2,
            "#FFD700": 1,
            "red": 0
        }
        return priority_values[priority]
    
    def remove_task(self, frame):
        frame.grid_forget()
        self.activities.remove(frame)
        self.task_list_frame_inner.configure(background="#faf5ef")
        self.arrange_activities()
        self.update_scrollwheel()

    def update_scrollwheel(self, event=None):
        #update scrollability
        self.task_list_frame_inner.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        canvas_height = self.canvas.winfo_height()
        canvas_frame_height = self.task_list_frame_inner.winfo_reqheight()

        if canvas_frame_height > canvas_height:
            self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)
        else:
            self.canvas.unbind_all("<MouseWheel>")


class CalendarWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Calendar")
        self.geometry("300x250")
        self.minsize(300, 250)
        
        self.cal = Calendar(self, firstweekday="sunday", date_pattern="dd/mm/yyyy")
        self.cal.pack(pady=10)
        select_button = Button(self, text = "Get Deadline", bg="white", bd=1, command=self.get_deadline)
        select_button.pack()

    def get_deadline(self):
        date = self.cal.get_date()
        self.parent.deadline.set(date)
        self.destroy()


class MenuBar(Menu):
    def __init__(self, parent, stats, task_display):
        super().__init__(parent)
        self.parent = parent
        self.stats = stats
        self.task_display = task_display

        #file menu
        file_menu = Menu(self, tearoff=0)
        file_menu.add_command(label="Save", command=self.save_tasks)
        file_menu.add_command(label="Load", command=self.load_tasks)
        file_menu.add_command(label="Clear", command=self.confirm_clear_tasks)
        self.add_cascade(label="File", menu=file_menu)

        #statistics menu
        stats_menu = Menu(self, tearoff=0)
        stats_menu.add_command(label="General", command=self.show_general_stats)
        stats_menu.add_command(label="Priorities", command=self.show_priority_stats)
        stats_menu.add_command(label="Tags", command=self.show_tags_stats)
        self.add_cascade(label="Statistics", menu=stats_menu)

        #refresh
        self.add_command(label="Refresh", command=self.refresh)

    def save_tasks(self):
        try:
            #extract data from self.activities and self.completed
            task_data = {
                "active": [],
                "completed": []
            }

            for frame in self.task_display.activities:
                task_data["active"].append({
                    "task": frame.task_label.cget("text"),
                    "deadline": frame.deadline_label.cget("text") if frame.deadline_label else "",
                    "priority": frame.prio,
                    "color": frame.task_label.cget("fg"),
                    "tags": frame.tags
                })

            for frame in self.task_display.completed:
                try:
                    info = {
                        "task": frame.task_label.cget("text"),
                        "deadline": frame.deadline_label.cget("text") if frame.deadline_label else "",
                        "priority": frame.prio,
                        "color": frame.task_label.cget("fg"),
                        "tags": frame.tags
                    }
                except:
                    info = {
                        "task": frame.task,
                        "deadline": frame.deadline,
                        "priority": frame.prio,
                        "color": frame.color,
                        "tags": frame.tags
                    }
                task_data["completed"].append(info)

            #save to file
            file_path = filedialog.asksaveasfilename(
                defaultextension=".pkl", 
                initialfile="tasks.pkl",
                filetypes=[("Pickle Files", "*.pkl")]
            )
            if file_path:
                with open(file_path, "wb") as file:
                    pickle.dump(task_data, file)
                messagebox.showinfo("Save", "Tasks saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save tasks: {str(e)}")

    def confirm_clear_tasks(self):
        choice = messagebox.askyesno("Clear", "Are you sure you want to clear all tasks?")
        if choice:
            self.clear_tasks()

    def clear_tasks(self):
        for task in self.task_display.activities:
            self.task_display.complete_activity(task)
        self.task_display.activities.clear()
        self.task_display.completed.clear()
        self.task_display.task_list_frame_inner.destroy()
        self.task_display.task_list_frame_inner = Frame(self.task_display.canvas)
        self.task_display.task_list_frame_inner.pack(fill=BOTH, expand=True)
        self.task_display.canvas.create_window((0, 0), window=self.task_display.task_list_frame_inner, anchor=NW)
        self.task_display.update_scrollwheel()

    def load_tasks(self):
        try:
            #load from file
            file_path = filedialog.askopenfilename(filetypes=[("Pickle Files", "*.pkl")])
            if file_path:
                with open(file_path, "rb") as file:
                    task_data = pickle.load(file)
                #clear existing data
                self.clear_tasks()

                #load completed tasks
                for task_info in task_data.get("completed", []):
                    frame = Frame()
                    frame.task = task_info["task"]
                    frame.deadline = task_info.get("deadline", "")
                    frame.prio = task_info["priority"]
                    frame.color = task_info["color"]
                    frame.tags = task_info["tags"]
                    self.task_display.completed.append(frame)

                #load active tasks
                for task_info in task_data.get("active", []):
                    task = task_info["task"]
                    deadline = task_info.get("deadline", "")
                    prio = task_info["priority"]
                    color = task_info["color"]
                    tags = task_info["tags"]
                    self.task_display.add_activity(task, prio, color, tags, deadline)
            
                messagebox.showinfo("Load", "File loaded successfully!")
        except EOFError:
            messagebox.showerror("Load", "File is empty.")
        except FileNotFoundError:
            messagebox.showerror("Load", "File not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load tasks: {str(e)}")

    def show_general_stats(self):
        general_stats = self.stats.get_general_stats()
        self.gen_window = GeneralStatsWindow(self.parent, "General Statistics", general_stats)

    def show_priority_stats(self):
        prio_stats = self.stats.get_priority_stats()
        self.prio_window = PriorityStatsWindow(self.parent, "Priority Statistics", prio_stats)

    def show_tags_stats(self):
        tags_stats = self.stats.get_tags_stats()
        self.tags_window = TagsStatsWindow(self.parent, "Tags Statistics", tags_stats)

    def refresh(self):
        windows = {'gen_window': self.stats.get_general_stats(),
                'prio_window': self.stats.get_priority_stats(),
                'tags_window': self.stats.get_tags_stats()}

        for win_name, win_stats in windows.items():
            window = getattr(self, win_name, None)
            if window:
                window.stats = win_stats
                window.create_stats()


class StatisticsManager(object):
    def __init__(self, task_display):
        self.task_display = task_display

    def get_general_stats(self):
        active = len(self.task_display.activities)
        completed = len(self.task_display.completed)        
        total = active + completed

        return {
            "active": active, 
            "completed": completed, 
            "total": total
        }

    def get_priority_stats(self):
        prio_high = sum(1 for frame in self.task_display.activities if frame.prio == "red") 
        prio_high_complete = sum(1 for frame in self.task_display.completed if frame.prio == "red")
        prio_medium = sum(1 for frame in self.task_display.activities if frame.prio == "#FFD700") 
        prio_medium_complete = sum(1 for frame in self.task_display.completed if frame.prio == "#FFD700")
        prio_low = sum(1 for frame in self.task_display.activities if frame.prio == "blue") 
        prio_low_complete = sum(1 for frame in self.task_display.completed if frame.prio == "blue")
        prio_none = sum(1 for frame in self.task_display.activities if frame.prio == "gray") 
        prio_none_completed = sum(1 for frame in self.task_display.completed if frame.prio == "gray")

        return {
            "prio_high": prio_high, 
            "prio_high_all": prio_high + prio_high_complete,
            "prio_medium": prio_medium, 
            "prio_medium_all": prio_medium + prio_medium_complete,
            "prio_low": prio_low, 
            "prio_low_all": prio_low + prio_low_complete,
            "prio_none": prio_none, 
            "prio_none_all": prio_none + prio_none_completed,
        }

    def get_tags_stats(self):
        tag_personal = sum(1 for frame in self.task_display.activities if frame.tags["Personal"] == 1)
        tag_personal_all = sum(1 for frame in self.task_display.completed if frame.tags["Personal"] == 1)
        tag_family = sum(1 for frame in self.task_display.activities if frame.tags["Family"] == 1)
        tag_family_all = sum(1 for frame in self.task_display.completed if frame.tags["Family"] == 1)
        tag_friend = sum(1 for frame in self.task_display.activities if frame.tags["Friend"] == 1)
        tag_friend_all = sum(1 for frame in self.task_display.completed if frame.tags["Friend"] == 1)
        tag_work = sum(1 for frame in self.task_display.activities if frame.tags["Work"] == 1)
        tag_work_all = sum(1 for frame in self.task_display.completed if frame.tags["Work"] == 1)
        tag_entertainment = sum(1 for frame in self.task_display.activities if frame.tags["Entertainment"] == 1)
        tag_entertainment_all = sum(1 for frame in self.task_display.completed if frame.tags["Entertainment"] == 1)

        return {
            "tag_personal": tag_personal, 
            "tag_personal_all": tag_personal + tag_personal_all,
            "tag_family": tag_family, 
            "tag_family_all": tag_family + tag_family_all,
            "tag_friend": tag_friend, 
            "tag_friend_all": tag_friend + tag_friend_all,
            "tag_work": tag_work, 
            "tag_work_all": tag_work + tag_work_all,
            "tag_entertainment": tag_entertainment, 
            "tag_entertainment_all": tag_entertainment + tag_entertainment_all,
        }


class ToDoList(object):
    def __init__(self):
        root = Tk()
        root.title("To-do List")
        root.geometry("900x600")
        root.minsize(900, 600)

        #create margins
        margin_top = Frame(root, width=500, height=15)
        margin_left = Frame(root, height=300, width=15)
        margin_mid = Frame(root, height=300, width=15)
        margin_right = Frame(root, height=300, width=15)
        margin_bottom = Frame(root, width=500, height=15)
        margin_top.grid(row=1, column=1, columnspan=5)
        margin_left.grid(row=2, column=1, sticky=W)
        margin_mid.grid(row=2, column=3)
        margin_right.grid(row=2, column=5, sticky=E)
        margin_bottom.grid(row=3, column=1, columnspan=5)

        #expand margins
        root.grid_rowconfigure(1, weight=1)
        root.grid_rowconfigure(3, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(5, weight=1)

        #create main working frames
        self.task_display = TaskDisplay(root)
        self.task_display.grid(row=2, column=4, sticky=N)

        self.task_creator = TaskCreator(root, self.task_display)
        self.task_creator.grid(row=2, column=2, sticky=N)

        self.statistics = StatisticsManager(self.task_display)
        self.menu_bar = MenuBar(root, self.statistics, self.task_display) 

        root.bind("<Control-s>", lambda event: self.menu_bar.save_tasks())
        root.bind("<Control-l>", lambda event: self.menu_bar.load_tasks())
        root.bind("<Control-g>", lambda event: self.menu_bar.show_general_stats())
        root.bind("<Control-p>", lambda event: self.menu_bar.show_priority_stats())
        root.bind("<Control-t>", lambda event: self.menu_bar.show_tags_stats())
        root.bind("<Control-r>", lambda event: self.menu_bar.refresh())

        root.config(menu=self.menu_bar)

        root.mainloop()


if __name__ == "__main__":
    ToDoList()

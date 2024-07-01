import tkinter as tk
from tkinter import messagebox

#import paramiko

class Maintenance:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("RMRC Maintenance Tool")
        self.root.state('zoomed')

        #self.client = paramiko.SSHClient()
        #self.client.load_system_host_keys()
        #self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.create_connect_frame()
        self.create_maintenance_frame()
        self.on_connect()
        self.root.mainloop()

    def create_connect_frame(self):
        self.connect_frame = tk.Frame(self.root)
        self.hostname_frame = tk.Frame(self.connect_frame)
        self.ip_frame = tk.Frame(self.connect_frame)
        self.run_frame = tk.Frame(self.connect_frame)

        self.connect_frame.grid(row=0, column=0, sticky="nswe", pady=100)

        self.hostname_frame.pack(pady=5)
        self.ip_frame.pack(pady=5)
        self.run_frame.pack(pady=5)

        hostname_label = tk.Label(self.hostname_frame, text="Hostname:", font=("Arial", 12))
        hostname_label.pack(side=tk.LEFT, pady=10)

        self.hostname_entry = tk.Entry(self.hostname_frame, font=("Arial", 12))
        self.hostname_entry.pack(side=tk.LEFT, pady=10)
        self.hostname_entry.insert(0, "sam")

        ip_label = tk.Label(self.ip_frame, text="IP Adress:", font=("Arial", 12))
        ip_label.pack(side=tk.LEFT, pady=10)

        self.ip_entry = tk.Entry(self.ip_frame, font=("Arial", 12))
        self.ip_entry.pack(side=tk.LEFT, pady=10)
        self.ip_entry.insert(0, "192.168.1.38")

        self.run_button = tk.Button(self.run_frame, text="Connect", command=self.connect_ssh,
                                    font=("Arial", 12))
        self.run_button.pack(pady=20, padx=50)

    def create_maintenance_frame(self):
        self.maintenance_frame = tk.Frame(self.root)
        self.maintenance_frame.grid(row=0,column=0, sticky="nswe",pady=50,padx=200)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.maintenance_frame.columnconfigure(0, weight=0)
        self.maintenance_frame.columnconfigure(1, weight=1)
        self.maintenance_frame.columnconfigure(2, weight=0)

        setup_frame = tk.Frame(self.maintenance_frame, bg="yellow")
        setup_frame.grid(row=0, column=0, sticky="nsw")

        maintain_frame = tk.Frame(self.maintenance_frame, bg="yellow")
        maintain_frame.grid(row=0, column=1, sticky="nswe")

        run_frame = tk.Frame(self.maintenance_frame, bg="yellow")
        run_frame.grid(row=0, column=2, sticky="nse")

        setup_label = tk.Label(setup_frame, text="Setup", font=("Arial", 14), bg="yellow", padx=20,pady=10)
        setup_label.pack()

        setup_ros_btn = tk.Button(setup_frame, text="Download Ros2", command=self.install_ros2,font=("Arial", 12))
        setup_ros_btn.pack(pady=20, padx=20)

        if self.is_installed_ros2():
            setup_ros_btn.config(bg = "lightgreen")
            setup_ros_btn.config(state=tk.DISABLED)
        else:
            setup_ros_btn.config(bg = "lightcoral")

        setup_edu_btn = tk.Button(setup_frame, text="Download Edu Drive", command=self.install_edu_drive, font=("Arial", 12))
        setup_edu_btn.pack(pady=20, padx=20)
        if self.is_installed_edu_drive():
            setup_edu_btn.config(state=tk.DISABLED)
            setup_edu_btn.config(bg="lightgreen")
        else:
            setup_edu_btn.config(bg="lightcoral")

        maintain_label = tk.Label(maintain_frame, text="Maintain", font=("Arial", 14), bg="yellow", padx=20,pady=10)
        maintain_label.pack()

        pull_btn = tk.Button(maintain_frame, text="Fetch Updates", font=("Arial", 12), bg="#d0d0d0", command=self.fetch_updates)
        pull_btn.pack(pady=20, padx=20)

        build_btn = tk.Button(maintain_frame, text="Build Packages", font=("Arial", 12), bg="#d0d0d0", command=self.build_packages)
        build_btn.pack(pady=20, padx=20)

        run_label = tk.Label(run_frame, text="Deploy", font=("Arial", 14), bg="yellow", padx=20,pady=10)
        run_label.pack()

        deploy_btn = tk.Button(run_frame, text="Deploy Robot", font=("Arial", 12), bg="#d0d0d0", command=self.run_robot)
        deploy_btn.pack(pady=20, padx=20)

        driver_gui_btn = tk.Button(run_frame, text="Open driver_gui", font=("Arial", 12), bg="#d0d0d0", command=self.open_driver_gui)
        driver_gui_btn.pack(pady=20, padx=20)

        shutdown_btn = tk.Button(run_frame, text="Close Connection", font=("Arial", 12), bg="#d0d0d0", command=self.disconnect)
        shutdown_btn.pack(pady=100, padx=20)



    def open_driver_gui(self):
        pass
    def disconnect(self):
        pass

    def fetch_updates(self):
        pass

    def build_packages(self):
        pass

    def run_robot(self):

        pass

    def install_ros2(self):
        #return to ssh_con after sudo_reboot
        pass

    def install_edu_drive(self):
        pass

#except paramiko.SSHException as e:

    def is_installed_ros2(self):
        #stdin, stdout, stderr = self.client.exec_command("which ros2")
        #return len(stdout.read().decode().strip()) > 0
        return True

    def is_installed_edu_drive(self):
        #stdin, stdout, stderr = self.client.exec_command("[-d /home/sam/ros2_ws/src/edu_drive_ros2 ] && echo "installed" || echo "uninstalled")
        #return stdout.read().decode().strip() == "installed"
        return False


    def on_connect(self):
        self.maintenance_frame.grid_forget()
        self.connect_frame.grid(row=0,column=0, sticky="nswe",pady=100)

    def on_maintain(self):
        self.connect_frame.grid_forget()
        self.maintenance_frame.grid(row=0,column=0, sticky="nswe",pady=50,padx=200)

    def connect_ssh(self):
        #try:
        #self.client.connect(self.ip_entry.get(), username=self.hostname_entry.get(), password="techrobot")
        #on_maintain()
        #except paramiko.ssh_exception.AuthenticationException as e:
        #messagebox.showerror("Connection", f"Failed to connect: {e}")
        self.on_maintain()
        pass


m = Maintenance()

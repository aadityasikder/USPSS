import tkinter as tk, paramiko, os
from tkinter import messagebox

def terminate_video_stream(hostname, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname, username=username, password=password)
        ssh.exec_command('cd USPSS/experiment/')
        ssh.exec_command('pkill -f csv_log_face.py')
        transfer_csv_file(ssh)
        messagebox.showinfo("Success", "Video stream terminated successfully.")
    except paramiko.AuthenticationException:
        messagebox.showerror("Error", "Authentication failed. Please check your credentials.")
    except paramiko.SSHException as ssh_exc:
        messagebox.showerror("Error", f"SSH error: {ssh_exc}")
    finally:
        ssh.close()

def transfer_csv_file(ssh):
    sftp = ssh.open_sftp()
    remote_path = 'USPSS/experiment/face_log.csv'
    local_path = os.path.join(os.getcwd(), 'face_log.csv')  # Save to current directory
    sftp.get(remote_path, local_path)
    sftp.close()

def terminate_stream():
    hostname = hostname_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    terminate_video_stream(hostname, username, password)

root = tk.Tk()
root.title("Video Stream Terminator")

tk.Label(root, text="Hostname:").grid(row=0, column=0, padx=18, pady=5, sticky="e")
hostname_entry = tk.Entry(root)
hostname_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Username:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Password:").grid(row=2, column=0, padx=18, pady=5, sticky="e")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

terminate_button = tk.Button(root, text="Terminate Stream", command=terminate_stream)
terminate_button.grid(row=3, columnspan=2, pady=10)

root.mainloop()


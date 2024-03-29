import paramiko
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window

class SSHManager:
    def __init__(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self, hostname, username, password):
        try:
            self.ssh.connect(hostname, username=username, password=password, timeout=5)
            return True
        except paramiko.AuthenticationException:
            self.show_alert("Authentication Failed", "Please check your credentials.")
        except paramiko.SSHException as ssh_exc:
            self.show_alert("SSH Error", f"SSH error: {ssh_exc}")
        except TimeoutError:
            self.show_alert("Connection Timeout", "Unable to connect to the host. Please check the hostname.")
        return False

    def terminate_video_stream(self):
        try:
            stdin, stdout, stderr = self.ssh.exec_command('pkill -f csv_log_face.py')
            self.show_alert("Video Stream Terminated", "Video stream terminated successfully.")
        finally:
            self.ssh.close()

    def transfer_file_to_pc(self):
        try:
            sftp = self.ssh.open_sftp()
            sftp.get("USPSS/experiment/face_log.csv", "face_log.csv")
            self.show_alert("File Transfer", "File transferred successfully.")
        except FileNotFoundError:
            self.show_alert("File Not Found", "The file 'face_log.csv' does not exist on the Jetson Nano.")
        except Exception as e:
            self.show_alert("File Transfer Error", f"Error occurred during file transfer: {e}")
        finally:
            if 'sftp' in locals():
                sftp.close()

    def show_alert(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(Window.width * 0.8, Window.height * 0.4))
        popup.open()

class MyGUI(App):
    def __init__(self):
        super().__init__()
        self.hostname_input = TextInput(text='', hint_text='Hostname')
        self.username_input = TextInput(text='', hint_text='Username')
        self.password_input = TextInput(text='', hint_text='Password', password=True)
        self.ssh_manager = SSHManager()

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(self.hostname_input)
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        
        terminate_button = Button(text='Terminate Video Stream', size_hint_y=None, height=Window.height * 0.1)
        terminate_button.bind(on_press=self.terminate_video_stream)
        layout.add_widget(terminate_button)
        
        transfer_button = Button(text='Transfer File to PC', size_hint_y=None, height=Window.height * 0.1)
        transfer_button.bind(on_press=self.transfer_file_to_pc)
        layout.add_widget(transfer_button)
        
        return layout

    def terminate_video_stream(self, instance):
        hostname = self.hostname_input.text
        username = self.username_input.text
        password = self.password_input.text
        if self.ssh_manager.connect(hostname, username, password):
            self.ssh_manager.terminate_video_stream()

    def transfer_file_to_pc(self, instance):
        hostname = self.hostname_input.text
        username = self.username_input.text
        password = self.password_input.text
        if self.ssh_manager.connect(hostname, username, password):
            self.ssh_manager.transfer_file_to_pc()

if __name__ == "__main__":
    MyGUI().run()



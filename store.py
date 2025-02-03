import tkinter as tk
from tkinter import ttk, messagebox, Frame, Canvas
import subprocess

class MegaAppStore:
    def __init__(self, root):
        self.root = root
        self.root.title("Mega App Installer")
        self.root.geometry("1000x800")
        
        # Список приложений (сокращенный пример - можно дополнить)
        self.apps = [
            {
                "category": "Разработка", 
                "apps": [
                    {"name": "VS Code", "pkg": "code", "desc": "Редактор кода (требует репозиторий)"},
                    {"name": "PyCharm", "pkg": "pycharm-community", "desc": "Python IDE"},
                    {"name": "IntelliJ IDEA", "pkg": "intellij-idea-community", "desc": "Java IDE"},
                    {"name": "Git", "pkg": "git", "desc": "Система контроля версий"},
                    {"name": "Docker", "pkg": "docker.io", "desc": "Контейнеризация"},
                    {"name": "Node.js", "pkg": "nodejs", "desc": "JavaScript runtime"},
                    {"name": "Postman", "pkg": "postman", "desc": "API тестирование"},
                    {"name": "Eclipse", "pkg": "eclipse", "desc": "Универсальная IDE"},
                    {"name": "Android Studio", "pkg": "android-studio", "desc": "Разработка под Android"},
                    {"name": "MySQL Workbench", "pkg": "mysql-workbench", "desc": "Управление базами данных"},
                    {"name": "PHPStorm", "pkg": "phpstorm", "desc": "PHP IDE (требует репозиторий)"},
                    {"name": "Sublime Text", "pkg": "sublime-text", "desc": "Текстовый редактор"},
                    {"name": "Atom", "pkg": "atom", "desc": "Редактор кода"},
                    {"name": "CMake", "pkg": "cmake", "desc": "Система сборки"},
                    {"name": "GCC", "pkg": "gcc", "desc": "Компилятор C/C++"},
                    {"name": "Python3", "pkg": "python3", "desc": "Интерпретатор Python"},
                    {"name": "Ruby", "pkg": "ruby-full", "desc": "Язык программирования Ruby"},
                    {"name": "Go", "pkg": "golang", "desc": "Язык программирования Go"},
                    {"name": "Rust", "pkg": "rustc", "desc": "Язык программирования Rust"},
                    {"name": "JDK", "pkg": "default-jdk", "desc": "Java Development Kit"},
                ]
            },
            {
                "category": "Графика", 
                "apps": [
                    {"name": "GIMP", "pkg": "gimp", "desc": "Редактор изображений"},
                    {"name": "Inkscape", "pkg": "inkscape", "desc": "Векторная графика"},
                    {"name": "Blender", "pkg": "blender", "desc": "3D моделирование"},
                    {"name": "Krita", "pkg": "krita", "desc": "Цифровая живопись"},
                    {"name": "Darktable", "pkg": "darktable", "desc": "Обработка RAW-фото"},
                    {"name": "Digikam", "pkg": "digikam", "desc": "Управление фотоколлекцией"},
                    {"name": "Shotwell", "pkg": "shotwell", "desc": "Просмотр и организация фото"},
                    {"name": "Figma", "pkg": "figma-linux", "desc": "Дизайн интерфейсов"},
                    {"name": "Scribus", "pkg": "scribus", "desc": "Верстка документов"},
                    {"name": "RawTherapee", "pkg": "rawtherapee", "desc": "Обработка фотографий"},
                ]
            },
            {
                "category": "Офис", 
                "apps": [
                    {"name": "LibreOffice", "pkg": "libreoffice", "desc": "Офисный пакет"},
                    {"name": "Evince", "pkg": "evince", "desc": "Просмотр PDF"},
                    {"name": "Okular", "pkg": "okular", "desc": "Просмотр документов"},
                    {"name": "Calibre", "pkg": "calibre", "desc": "Управление электронными книгами"},
                    {"name": "GnuCash", "pkg": "gnucash", "desc": "Финансовый менеджмент"},
                    {"name": "MasterPDF", "pkg": "master-pdf-editor", "desc": "Редактор PDF"},
                    {"name": "OnlyOffice", "pkg": "onlyoffice-desktopeditors", "desc": "Офисный пакет"},
                    {"name": "XMind", "pkg": "xmind", "desc": "Создание ментальных карт"},
                ]
            },
            {
                "category": "Интернет", 
                "apps": [
                    {"name": "Firefox", "pkg": "firefox", "desc": "Веб-браузер"},
                    {"name": "Chrome", "pkg": "google-chrome-stable", "desc": "Браузер Google"},
                    {"name": "Thunderbird", "pkg": "thunderbird", "desc": "Почтовый клиент"},
                    {"name": "Telegram", "pkg": "telegram-desktop", "desc": "Мессенджер"},
                    {"name": "Skype", "pkg": "skypeforlinux", "desc": "Видеозвонки"},
                    {"name": "Zoom", "pkg": "zoom", "desc": "Видеоконференции"},
                    {"name": "Discord", "pkg": "discord", "desc": "Голосовой чат"},
                    {"name": "qBittorrent", "pkg": "qbittorrent", "desc": "Торрент-клиент"},
                    {"name": "FileZilla", "pkg": "filezilla", "desc": "FTP-клиент"},
                    {"name": "Transmission", "pkg": "transmission", "desc": "Торрент-клиент"},
                ]
            },
            {
                "category": "Мультимедиа", 
                "apps": [
                    {"name": "VLC", "pkg": "vlc", "desc": "Медиаплеер"},
                    {"name": "Audacity", "pkg": "audacity", "desc": "Аудиоредактор"},
                    {"name": "Spotify", "pkg": "spotify-client", "desc": "Музыкальный стриминг"},
                    {"name": "OBS Studio", "pkg": "obs-studio", "desc": "Запись экрана"},
                    {"name": "Kdenlive", "pkg": "kdenlive", "desc": "Видеоредактор"},
                    {"name": "HandBrake", "pkg": "handbrake", "desc": "Конвертер видео"},
                    {"name": "Clementine", "pkg": "clementine", "desc": "Музыкальный плеер"},
                    {"name": "Pitivi", "pkg": "pitivi", "desc": "Видеоредактор"},
                    {"name": "LMMS", "pkg": "lmms", "desc": "Создание музыки"},
                    {"name": "Ardour", "pkg": "ardour", "desc": "Цифровая звуковая рабочая станция"},
                ]
            },
            {
                "category": "Система", 
                "apps": [
                    {"name": "GParted", "pkg": "gparted", "desc": "Управление дисками"},
                    {"name": "Timeshift", "pkg": "timeshift", "desc": "Бэкап системы"},
                    {"name": "htop", "pkg": "htop", "desc": "Монитор процессов"},
                    {"name": "GNOME Tweak Tool", "pkg": "gnome-tweaks", "desc": "Настройки GNOME"},
                    {"name": "Synaptic", "pkg": "synaptic", "desc": "Менеджер пакетов"},
                    {"name": "BleachBit", "pkg": "bleachbit", "desc": "Очистка системы"},
                    {"name": "Stacer", "pkg": "stacer", "desc": "Оптимизация системы"},
                    {"name": "Grub Customizer", "pkg": "grub-customizer", "desc": "Настройка загрузчика"},
                    {"name": "GSmartControl", "pkg": "gsmartcontrol", "desc": "Диагностика дисков"},
                    {"name": "Wine", "pkg": "wine", "desc": "Запуск Windows приложений"},
                ]
            },
            {
                "category": "Игры", 
                "apps": [
                    {"name": "Steam", "pkg": "steam", "desc": "Игровая платформа"},
                    {"name": "Lutris", "pkg": "lutris", "desc": "Менеджер игр"},
                    {"name": "Minecraft", "pkg": "minecraft-launcher", "desc": "Песочница"},
                    {"name": "0AD", "pkg": "0ad", "desc": "Стратегия"},
                    {"name": "SuperTuxKart", "pkg": "supertuxkart", "desc": "Гоночная игра"},
                    {"name": "OpenTTD", "pkg": "openttd", "desc": "Экономическая стратегия"},
                    {"name": "Wesnoth", "pkg": "wesnoth", "desc": "Пошаговая стратегия"},
                    {"name": "Minetest", "pkg": "minetest", "desc": "Строительная игра"},
                ]
            },
            {
                "category": "Образование", 
                "apps": [
                    {"name": "GCompris", "pkg": "gcompris", "desc": "Детские обучающие игры"},
                    {"name": "Stellarium", "pkg": "stellarium", "desc": "Планетарий"},
                    {"name": "Marble", "pkg": "marble", "desc": "Виртуальный глобус"},
                    {"name": "Kalzium", "pkg": "kalzium", "desc": "Периодическая таблица"},
                    {"name": "KGeography", "pkg": "kgeography", "desc": "География"},
                    {"name": "Scratch", "pkg": "scratch", "desc": "Обучение программированию"},
                    {"name": "MuseScore", "pkg": "musescore", "desc": "Нотный редактор"},
                ]
            },
            {
                "category": "Безопасность", 
                "apps": [
                    {"name": "Gufw", "pkg": "gufw", "desc": "Фаервол"},
                    {"name": "ClamAV", "pkg": "clamav", "desc": "Антивирус"},
                    {"name": "KeePassXC", "pkg": "keepassxc", "desc": "Менеджер паролей"},
                    {"name": "VeraCrypt", "pkg": "veracrypt", "desc": "Шифрование данных"},
                    {"name": "Wireshark", "pkg": "wireshark", "desc": "Анализатор сетевого трафика"},
                    {"name": "Nmap", "pkg": "nmap", "desc": "Сканер сети"},
                ]
            },
            {
                "category": "Другое", 
                "apps": [
                    {"name": "VirtualBox", "pkg": "virtualbox", "desc": "Виртуализация"},
                    {"name": "TeamViewer", "pkg": "teamviewer", "desc": "Удаленный доступ"},
                    {"name": "Anydesk", "pkg": "anydesk", "desc": "Удаленный рабочий стол"},
                    {"name": "Remmina", "pkg": "remmina", "desc": "Удаленный доступ"},
                    {"name": "BalenaEtcher", "pkg": "etcher-electron", "desc": "Запись образов"},
                    {"name": "Kazam", "pkg": "kazam", "desc": "Скриншоты и запись экрана"},
                    {"name": "SimpleScreenRecorder", "pkg": "simplescreenrecorder", "desc": "Запись экрана"},
                ]
            }
        ]
        
        # Загрузка установленных пакетов
        self.installed_packages = self.get_installed_packages()
        
        # Создание интерфейса
        self.create_widgets()
    
    def get_installed_packages(self):
        try:
            result = subprocess.check_output(
                "dpkg --get-selections | grep -v deinstall | cut -f1",
                shell=True,
                universal_newlines=True
            )
            return set(result.splitlines())
        except:
            return set()
    
    def create_widgets(self):
        # Контейнер с прокруткой
        container = Frame(self.root)
        canvas = Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        self.scrollable_frame = Frame(canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        container.pack(fill="both", expand=True)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Создание категорий
        for category in self.apps:
            self.create_category_section(category["category"], category["apps"])
    
    def create_category_section(self, category_name, apps):
        frame = ttk.LabelFrame(self.scrollable_frame, text=category_name)
        frame.pack(fill="x", padx=10, pady=5, ipady=5)
        
        for app in apps:
            app_frame = ttk.Frame(frame)
            app_frame.pack(fill="x", pady=2)
            
            ttk.Label(app_frame, text=app["name"], width=25).pack(side="left")
            ttk.Label(app_frame, text=app["desc"], width=60).pack(side="left")
            
            status = "Установлен" if app["pkg"] in self.installed_packages else "Не установлен"
            ttk.Label(app_frame, text=status, width=15).pack(side="left")
            
            btn = ttk.Button(
                app_frame,
                text="Удалить" if status == "Установлен" else "Установить",
                command=lambda p=app["pkg"], s=status: self.toggle_package(p, s)
            )
            btn.pack(side="right")
    
    def toggle_package(self, pkg, current_status):
        if current_status == "Установлен":
            self.uninstall_package(pkg)
        else:
            self.install_package(pkg)
    
    def install_package(self, pkg):
        try:
            subprocess.run(
                ["pkexec", "apt", "install", "-y", pkg],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            self.installed_packages.add(pkg)
            self.refresh_ui()
            messagebox.showinfo("Успех", f"{pkg} успешно установлен!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Ошибка", f"Не удалось установить {pkg}:\n{e.stderr}")
    
    def uninstall_package(self, pkg):
        try:
            subprocess.run(
                ["pkexec", "apt", "remove", "-y", pkg],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            self.installed_packages.discard(pkg)
            self.refresh_ui()
            messagebox.showinfo("Успех", f"{pkg} успешно удален!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Ошибка", f"Не удалось удалить {pkg}:\n{e.stderr}")
    
    def refresh_ui(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        for category in self.apps:
            self.create_category_section(category["category"], category["apps"])

if __name__ == "__main__":
    root = tk.Tk()
    app = MegaAppStore(root)
    root.mainloop()
#imports module wich allows pyton to interact with operating system
import os
import shutil
import datetime

# main path for folder to be sorted
download_folder = r"C:\Users\jansk\Downloads"
items_to_move = os.listdir(download_folder)
recent_dw_folder = os.path.join(download_folder, "Dw_Recent")

#  supported Audio types
audio_extensions = (".m4a", ".flac", "mp3", ".wav", ".wma", ".aac")
#  supported Video types
video_extensions = (".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd")
#  supported Image types
image_extensions = (".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif",
                    ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf",
                    ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico")
# supported Application extensions
installer_extensions = (".exe",)
# supported Compressed types
compressed_extensions = (".zip", ".rar")
# supported Document types
document_extensions = (".pdf",)
# supported Text types
text_extensions = (".doc", ".docx", ".odt", ".txt")
# supported Spreadsheet types
spreadsheet_extensions = (".xls", ".xlsx", ".csv")
# supported Presentation types
presentation_extensions = (".ppt", ".pptx")
# supported Font types
font_extensions = (".ttf",)
# all above extensions
all_extensions = audio_extensions + video_extensions + image_extensions + image_extensions + installer_extensions \
                 + compressed_extensions + document_extensions + text_extensions + spreadsheet_extensions \
                + presentation_extensions + font_extensions
folders = ["Dw_Recent", "Dw_Music", "Dw_Film", "Dw_Image", "Dw_Installer", "Dw_Compressed", "Dw_Pdf", "Dw_Text",
               "Dw_Spreadsheet", "Dw_Presentation", "Dw_Font", "Dw_Other" ]
def create_folders():
    for name in folders:
        if name in items_to_move:
            continue
        else:
            #creates folder for each folder name in folders
            os.mkdir(os.path.join(download_folder, name), mode= 0o666)

def check_modification_time(item_path):
    """
    This function checks if object was modified within 100 hours

    :param item_path:
    path of the object to check
    :return:
    returns True if item was modified within 100 hours
    """
    now = datetime.datetime.now()
    mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(item_path))
    time_difference = now - mod_time
    hours, minutes = divmod(time_difference.total_seconds(), 3600)
    if hours < 100:
        return True

#if check_modification_time(item, item_path) and not os.path.isdir(item):

def recent_files_mover(item, item_path):
    shutil.move(item_path, os.path.join(recent_dw_folder, item))


def recent_files_folder_check():
    for item in os.listdir(recent_dw_folder):
        current_path = os.path.join(recent_dw_folder, item)
        if not check_modification_time(current_path) and os.path.isfile(current_path):
            shutil.move(current_path, os.path.join(download_folder, item))

def sort_audios(item, item_path):
    if item.lower().endswith(audio_extensions):
        shutil.move(item_path, os.path.join(download_folder, "Dw_Music", item))

def sort_videos(item, item_path):
    if item.lower().endswith(video_extensions):
        shutil.move(item_path, os.path.join(download_folder, "Dw_Film", item))

def sort_images(item, item_path):
    if item.lower().endswith(image_extensions):
        shutil.move(item_path, os.path.join(download_folder, "Dw_Image", item))

def sort_installers(item, item_path):
    if item.lower().endswith(installer_extensions):
        shutil.move(item_path, os.path.join(download_folder, "Dw_Installer", item))

def sort_compressed(item, item_path):
    if item.lower().endswith(compressed_extensions):
        shutil.move(item_path, os.path.join(download_folder, "Dw_Compressed", item))

def sort_documents(item, item_path):
    if item.lower().endswith(document_extensions):
        shutil.move(item_path, os.path.join(download_folder, "Dw_Pdf", item))

def sort_texts(item, item_path):
    if item.lower().endswith(text_extensions):
        shutil.move(item_path, os.path.join(download_folder, "Dw_Text", item))

def sort_spreadsheets(item, item_path):
    if item.lower().endswith(spreadsheet_extensions):
        shutil.move(item_path, os.path.join(download_folder, "Dw_Spreadsheet", item))

def sort_presentations(item, item_path):
    if item.lower().endswith(presentation_extensions):
        shutil.move(item_path, os.path.join(download_folder, "Dw_Presentation", item))

def sort_fonts(item, item_path):
    if item.lower().endswith(font_extensions):
        shutil.move(item_path, os.path.join(download_folder, "Dw_Font", item))

def sort_other(item, item_path):
    if os.path.isfile(item_path) and not item.lower().endswith(all_extensions):
        shutil.move(item_path, os.path.join(download_folder, "Dw_Other", item))

def sort_items():
    create_folders()
    recent_files_folder_check()
    items_to_move = os.listdir(download_folder)
    for item in items_to_move:
        item_path = os.path.join(download_folder, item)
        if check_modification_time(item_path) and os.path.isfile(item_path):
            recent_files_mover(item, item_path)
        elif os.path.isfile(item_path) and not os.path.isdir(item_path):
            sort_audios(item, item_path)
            sort_videos(item, item_path)
            sort_images(item, item_path)
            sort_installers(item, item_path)
            sort_compressed(item, item_path)
            sort_documents(item, item_path)
            sort_texts(item, item_path)
            sort_spreadsheets(item, item_path)
            sort_presentations(item, item_path)
            sort_fonts(item, item_path)
            sort_other(item, item_path)

sort_items()
















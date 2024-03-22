import os
import shutil
import textwrap

from tqdm import tqdm
import argparse


def copy_files_with_structure(source_dir, target_dir, extension, copy_file, error_file, move=False):
    progress_bar = tqdm(desc=f'format: {extension}')
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(extension):
                source_file = os.path.join(root, file)
                relative_path = os.path.relpath(root, source_dir)
                target_folder = os.path.join(str(target_dir), str(relative_path))
                os.makedirs(target_folder, exist_ok=True)
                target_file = os.path.join(target_folder, file)
                try:
                    if move:
                        shutil.move(str(source_file), str(target_file))
                    else:
                        shutil.copy2(str(source_file), str(target_file))
                    with open(copy_file, "a+", encoding="utf-8") as f:
                        f.write(source_file + ' |->| ' + target_file + '\n')
                    progress_bar.update(1)
                except PermissionError:
                    with open(error_file, "a+", encoding="utf-8") as f:
                        f.write('PermissionError' + ': ' + str(source_file) + '\n')


def copy_files(source_dir, target_dir, extensions, copy_file, error_file, move):
    os.makedirs(target_dir, exist_ok=True)
    f = open(copy_file, "w", encoding="utf-8")
    f2 = open(error_file, "w", encoding="utf-8")
    f.close()
    f2.close()
    for ext in extensions:
        copy_files_with_structure(source_dir, target_dir, ext, copy_file, error_file, move=move)
        copy_files_with_structure(source_dir, target_dir, ext.upper(), copy_file, error_file, move=move)

    print('Done')


def remove_empty_dirs(dir_path):
    for root, dirs, files in os.walk(dir_path, topdown=False):
        for name in dirs:
            full_dir_path = os.path.join(root, name)
            if not os.listdir(str(full_dir_path)):
                os.rmdir(full_dir_path)
                print(f"Deleted empty folder: {full_dir_path}")


def main(move, del_empty, source_dir=None, target_dir=None, extension=None, fname=None):
    if not fname:
        fname = 'fagr'
    if source_dir and target_dir and extension:
        extensions = {}
        default_exts = {'books': ['.fb2', '.fb2.epub', '.fb2.zip', '.djvu', '.mobi'],
                        'images_videos': ['.jpg', '.png', '.bmp', '.gif', '.jpeg', '.webp', 'tif', '.ico', '.cr2',
                                            '.mp4', '.3gp', '.flv', '.wmv', '.mov', '.webm', '.mpeg'],
                        'music': ['.mp3', '.aac', '.flac', '.ogg', '.wav', '.alac', '.dsd', '.aiff', '.mqa', '.wma'],
                        'films': ['.avi', '.mkv'],
                        'PDF': ['.pdf'],
                        'word': ['.doc', '.docx'],
                        'exel': ['.xls', '.xlsx', '.xlsm', '.csv'],
                        'ppoint': ['.pptx', '.pptm'],
                        'txt': ['.txt'],
                        'python': ['.py'],
                        'jupyter': ['.ipynb']

}
        extensions[extension] = [source_dir, target_dir, default_exts[extension], f'{extension}_log.txt',
                                 f'{extension}_log_errors.txt']
    else:
        if source_dir or target_dir or extension:
            print('You have not entered all the required arguments, should you continue reading from the file? (y/n)')
            while char := input():
                if char == 'n':
                    exit()
                elif char == 'y':
                    break

        if not os.path.isfile('copy_move_files.txt'):
            print("Cofiguration file 'copy_move_files.txt' does not exist")
            f = open('copy_move_files.txt', 'w')
            f.close()
            print("The 'copy_move_files.txt' has been created. Please fill it out and restart the program.")
            input("Press the Enter exit")
            exit()
        else:
            f = open('copy_move_files.txt', 'r')
            lines = f.readlines()
            f.close()
            if len(lines) < 3:
                print("Not enough arguments in file")
                input("Press the Enter exit")
                exit()
            source_dir = lines[0].strip()
            target_dir = lines[1].strip()
            extensions = {}
            extension = 'user'
            extensions[extension] = [source_dir, target_dir, [], f'{fname}_log.txt', f'{fname}_log_errors.txt']
            for i in range(2, len(lines)):
                extensions[extension][2].append(lines[i].strip())

    copy_files(*extensions[extension], move)
    if del_empty:
        print(source_dir)
        remove_empty_dirs(source_dir)
        print('All empty directories are deleted.')


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--move', action='store_true')
    parser.add_argument('--del_empty', action='store_true')
    parser.add_argument('--s', default=None)
    parser.add_argument('--t', default=None)
    parser.add_argument('--e', default=None)
    parser.add_argument('--f')

    args = parser.parse_args()

    main(args.move, args.del_empty, args.s, args.t, args.e, args.f)


if __name__ == "__main__":
    run()

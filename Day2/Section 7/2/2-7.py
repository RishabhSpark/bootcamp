def copy_file(src_path, dest_path):
    with open(src_path, 'r') as src, open(dest_path, 'w') as dest:
        for line in src:
            dest.write(line)

copy_file('large_file.txt', 'copy_of_large_file.txt')

import os
import glob
import re

subpages = [
    'gioi-thieu',
    'linh-vuc-cong-nghe',
    'nong-san-chu-luc',
    'du-an-htx',
    'bao-gia-rfq'
]

root_replacements = {
    'gioi-thieu.html': 'gioi-thieu/',
    'linh-vuc-cong-nghe.html': 'linh-vuc-cong-nghe/',
    'nong-san-chu-luc.html': 'nong-san-chu-luc/',
    'du-an-htx.html': 'du-an-htx/',
    'bao-gia-rfq.html': 'bao-gia-rfq/',
    'trang-chu.html': './',
    'index.html': './'
}

# 1. Update root files
all_root_files = ['index.html', 'trang-chu.html'] + [f'{sp}.html' for sp in subpages]
for root_file in all_root_files:
    with open(root_file, 'r', encoding='utf-8') as f:
        content = f.read()
    for old, new in root_replacements.items():
        content = content.replace(f'href="{old}"', f'href="{new}"')
        content = content.replace(f"href='{old}'", f"href='{new}'")
    with open(root_file, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Generate subpage index.html files
for sp in subpages:
    src_file = f'{sp}.html'
    dest_dir = sp
    os.makedirs(dest_dir, exist_ok=True)
    dest_file = os.path.join(dest_dir, 'index.html')

    with open(src_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Link adjustments
    content = content.replace('href="./"', 'href="../"')
    content = content.replace("href='./'", "href='../'")
    content = content.replace('href="gioi-thieu/"', 'href="../gioi-thieu/"')
    content = content.replace('href="linh-vuc-cong-nghe/"', 'href="../linh-vuc-cong-nghe/"')
    content = content.replace('href="nong-san-chu-luc/"', 'href="../nong-san-chu-luc/"')
    content = content.replace('href="du-an-htx/"', 'href="../du-an-htx/"')
    content = content.replace('href="bao-gia-rfq/"', 'href="../bao-gia-rfq/"')

    # Asset adjustments
    content = content.replace('src="assets/', 'src="../assets/')
    content = content.replace("src='assets/", "src='../assets/")
    content = content.replace('href="assets/', 'href="../assets/')
    content = content.replace("href='assets/", "href='../assets/")
    content = content.replace('url(assets/', 'url(../assets/')
    content = content.replace('url("assets/', 'url("../assets/')
    content = content.replace("url('assets/", "url('../assets/")

    with open(dest_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Created {dest_file} successfully ({os.path.getsize(dest_file)} bytes)')

print('Clean URL processing finished successfully.')

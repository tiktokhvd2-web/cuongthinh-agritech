import re
import glob

def tune_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Add smooth scroll to html if not present
    if 'html {' not in content and 'html{' not in content:
        content = content.replace('<style>', '<style>\n    html { scroll-behavior: smooth; }\n', 1)
    elif 'scroll-behavior' not in content:
        content = re.sub(r'html\s*\{', 'html {\n      scroll-behavior: smooth;', content, count=1)

    # 2. Tune [data-reveal] CSS
    # Replace blur, transition duration, cubic-bezier, and offsets
    content = re.sub(
        r'filter:\s*blur\(10px\);',
        'filter: blur(4px);',
        content
    )
    content = re.sub(
        r'transition:\s*opacity\s*0\.85s\s*cubic-bezier\(0\.16,\s*1,\s*0\.3,\s*1\),\s*\n\s*transform\s*0\.85s\s*cubic-bezier\(0\.16,\s*1,\s*0\.3,\s*1\),\s*\n\s*filter\s*0\.85s\s*cubic-bezier\(0\.16,\s*1,\s*0\.3,\s*1\);',
        'transition: opacity 1.25s cubic-bezier(0.22, 1, 0.36, 1),\n                  transform 1.25s cubic-bezier(0.22, 1, 0.36, 1),\n                  filter 1.25s cubic-bezier(0.22, 1, 0.36, 1);',
        content
    )
    # Also handle single-line transition if any
    content = re.sub(
        r'transition:\s*opacity\s*0\.85s[^;]+filter\s*0\.85s[^;]+;',
        'transition: opacity 1.25s cubic-bezier(0.22, 1, 0.36, 1), transform 1.25s cubic-bezier(0.22, 1, 0.36, 1), filter 1.25s cubic-bezier(0.22, 1, 0.36, 1);',
        content
    )

    # Transform offsets
    content = re.sub(r'\[data-reveal="up"\]\s*\{\s*transform:\s*translateY\(54px\);', '[data-reveal="up"] {\n      transform: translateY(24px);', content)
    content = re.sub(r'\[data-reveal="left"\]\s*\{\s*transform:\s*translateX\(-64px\);', '[data-reveal="left"] {\n      transform: translateX(-28px);', content)
    content = re.sub(r'\[data-reveal="right"\]\s*\{\s*transform:\s*translateX\(64px\);', '[data-reveal="right"] {\n      transform: translateX(28px);', content)
    content = re.sub(r'\[data-reveal="scale"\]\s*\{\s*transform:\s*scale\(0\.92\);', '[data-reveal="scale"] {\n      transform: scale(0.96);', content)

    # 3. Tune Marquee speed from 68s to 130s
    content = re.sub(r'animation:\s*marquee-left\s*68s\s*linear\s*infinite;', 'animation: marquee-left 130s linear infinite;', content)
    content = re.sub(r'animation:\s*marquee-right\s*68s\s*linear\s*infinite;', 'animation: marquee-right 130s linear infinite;', content)

    # 4. Tune Counter speed from 1500 to 2400
    content = re.sub(r'const duration = 1500;', 'const duration = 2400;', content)
    content = re.sub(r'const easeVal = 1 - Math\.pow\(1 - progress, 3\);', 'const easeVal = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);', content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")
    else:
        print(f"No changes matched: {filepath}")

if __name__ == '__main__':
    all_files = [
        'index.html',
        'trang-chu.html',
        'gioi-thieu.html',
        'linh-vuc-cong-nghe.html',
        'nong-san-chu-luc.html',
        'du-an-htx.html',
        'bao-gia-rfq.html',
        'gioi-thieu/index.html',
        'linh-vuc-cong-nghe/index.html',
        'nong-san-chu-luc/index.html',
        'du-an-htx/index.html',
        'bao-gia-rfq/index.html'
    ]
    for target in all_files:
        tune_html(target)

import re

def update_smooth_slow(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Slow down Marquee to 220s
    content = re.sub(r'animation:\s*marquee-left\s*\d+s\s*linear\s*infinite;', 'animation: marquee-left 220s linear infinite;', content)
    content = re.sub(r'animation:\s*marquee-right\s*\d+s\s*linear\s*infinite;', 'animation: marquee-right 220s linear infinite;', content)

    # 2. Smooth and slow down [data-reveal] to 1.6s with gentle cinematic cubic-bezier
    # Easing cubic-bezier(0.16, 1, 0.3, 1) or cubic-bezier(0.25, 1, 0.35, 1)
    content = re.sub(
        r'transition:\s*opacity\s*[\d\.]+s\s*cubic-bezier\([^\)]+\),\s*\n\s*transform\s*[\d\.]+s\s*cubic-bezier\([^\)]+\),\s*\n\s*filter\s*[\d\.]+s\s*cubic-bezier\([^\)]+\);',
        'transition: opacity 1.6s cubic-bezier(0.16, 1, 0.3, 1),\n                  transform 1.6s cubic-bezier(0.16, 1, 0.3, 1),\n                  filter 1.6s cubic-bezier(0.16, 1, 0.3, 1);',
        content
    )
    content = re.sub(
        r'transition:\s*opacity\s*[\d\.]+s[^\;]+filter\s*[\d\.]+s[^\;]+;',
        'transition: opacity 1.6s cubic-bezier(0.16, 1, 0.3, 1), transform 1.6s cubic-bezier(0.16, 1, 0.3, 1), filter 1.6s cubic-bezier(0.16, 1, 0.3, 1);',
        content
    )

    # 3. Soften translateY / translateX to super subtle 18px and 20px
    content = re.sub(r'\[data-reveal="up"\]\s*\{\s*transform:\s*translateY\(\d+px\);', '[data-reveal="up"] {\n      transform: translateY(18px);', content)
    content = re.sub(r'\[data-reveal="left"\]\s*\{\s*transform:\s*translateX\(-\d+px\);', '[data-reveal="left"] {\n      transform: translateX(-20px);', content)
    content = re.sub(r'\[data-reveal="right"\]\s*\{\s*transform:\s*translateX\(\d+px\);', '[data-reveal="right"] {\n      transform: translateX(20px);', content)
    content = re.sub(r'\[data-reveal="scale"\]\s*\{\s*transform:\s*scale\([\d\.]+\);', '[data-reveal="scale"] {\n      transform: scale(0.97);', content)

    # 4. In IntersectionObserver reveal script, add natural gentle stagger delay and rootMargin
    # Adjust rootMargin to trigger smoothly when slightly more in view
    content = re.sub(
        r'threshold:\s*0\.12,\s*\n\s*rootMargin:\s*\'0px 0px -40px 0px\'',
        'threshold: 0.08,\n          rootMargin: \'0px 0px -20px 0px\'',
        content
    )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")
    else:
        print(f"No changes: {filepath}")

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
        update_smooth_slow(target)

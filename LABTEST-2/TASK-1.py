import re
def bump_version(name):
    # Split the filename into base and extension
    if '.' in name:
        base, ext = name.rsplit('.', 1)
        ext = '.' + ext
    else:
        base = name
        ext = ''
    # Regex to find _vNN at the end of the base
    m = re.search(r'(.*)_v(\d+)$', base)
    if m:
        prefix = m.group(1)
        num = m.group(2)
        new_num = int(num) + 1
        # Preserve zero-padding: use same width as original
        width = len(num)
        new_base = f"{prefix}_v{new_num:0{width}d}"
    else:
        # No version, add _v01
        new_base = f"{base}_v01"
    return new_base + ext

if __name__ == "__main__":
    # Read input from console: comma or space separated
    try:
        input_str = input("Enter filenames separated by comma or space: ").strip()
        if ',' in input_str:
            names = [s.strip() for s in input_str.split(',') if s.strip()]
        else:
            names = [s.strip() for s in input_str.split() if s.strip()]
    except Exception:
        names = []
    bumped = [bump_version(name) for name in names]
    print(bumped)

# Test cases (for reference, not executed in main)
# print(bump_version('report_v1.csv'))   # report_v02.csv
# print(bump_version('summary.csv'))     # summary_v01.csv
# print(bump_version('log_v09.txt'))     # log_v10.txt
# print(bump_version('data_v99'))        # data_v100
# print(bump_version('file'))            # file_v01

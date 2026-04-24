import re
import argparse
import sys

def clean_domain(raw_text):
    if any(char in raw_text for char in ['[', ']', '|']) or ( '(' in raw_text and '(?<=' not in raw_text):
        if '|' in raw_text and '(?<=' not in raw_text:
            return None
        if re.search(r'(?<!\(\?<=)\(', raw_text):
            return None

    step1 = re.sub(r'^(\*?://|/(\(\?<=.*?\))?|/)', '', raw_text)
    step2 = step1.split('/')[0]
    step3 = step2.replace('\\', '')
    step4 = re.sub(r'[/).+*?]+$', '', step3)

    ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(ip_pattern, step4):
        return None

    if '.' not in step4 or len(step4) < 4 or any(c in step4 for c in '()[]|*+'):
        return None

    return step4.lower().strip()

def main():
    parser = argparse.ArgumentParser(description="Extract clean domains from text/regex lists.")
    parser.add_argument("input", help="Path to input file")
    parser.add_argument("-o", "--output", help="Path to output file", required=True)

    args = parser.parse_args()
    domains = set()

    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                domain = clean_domain(line)
                if domain:
                    domains.add(domain)

        with open(args.output, 'w', encoding='utf-8') as f_out:
            for d in sorted(list(domains)):
                f_out.write(f"{d}\n")

    except FileNotFoundError:
        print(f"Error: file not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
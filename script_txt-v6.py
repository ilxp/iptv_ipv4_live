import requests

def fetch_and_filter():
    #url = 'https://raw.githubusercontent.com/yuanzl77/IPTV/refs/heads/main/live.txt'
    url = 'https://raw.githubusercontent.com/ilxp/YKTV/main/live.txt'
    # 获取文件内容
    response = requests.get(url)
    content = response.text
    
    # 过滤掉包含 "ipv4" 的行
    filtered_lines = [line for line in content.splitlines() if 'ipv4' not in line.lower()]
    
    # 保存到新文件
    with open('ipv6.txt', 'w') as file:
        file.write('\n'.join(filtered_lines))

if __name__ == "__main__":
    fetch_and_filter()
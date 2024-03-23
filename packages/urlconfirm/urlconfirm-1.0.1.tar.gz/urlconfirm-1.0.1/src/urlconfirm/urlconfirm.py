import re


def is_link_or_text(url):
    # 링크 패턴을 확인하는 정규표현식
    link_pattern = re.compile(
        r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)')

    # 입력된 데이터가 링크 패턴과 일치하는지 확인
    if link_pattern.match(url):
        return "Link"
    else:
        return "Text"
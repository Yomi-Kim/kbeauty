from django import template

register = template.Library()

@register.filter
def trim_zeros(value):
    """
    가격 표시 시 맨 끝의 0을 제거하는 필터.
    - 1.00 → 1
    - 1.20 → 1.2
    - 1.22 → 1.22 (유지)
    - 10.00 → 10
    - 99.90 → 99.9
    """
    value = str(value)  # 문자열 변환
    if '.' in value:
        value = value.rstrip('0').rstrip('.')  # 맨 끝 '0'과 '.' 제거
    return value

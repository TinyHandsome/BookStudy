from django.shortcuts import render
from funcs.func1.extract_built_sql import extract_built_sql
from supports.str_funcs import is_None_or_nullstr
from supports.topc_title_search import search_title


def func1(request):
    """处理获得的sql"""
    data = {
        'title': search_title(request),
        'sql': '',
        'result1': '',
        'result2': '',
        'result': ''
    }

    if request.method == 'POST':
        sql = request.POST.get('sql')
        data['sql'] = sql

        if is_None_or_nullstr(sql):
            data['result'] = '你啥也没输入，想干啥？'
            return render(request, 'func1_mysql2hive/func1.html', context=data)

        result1, result2 = extract_built_sql(sql)
        data['result1'] = result1
        data['result2'] = result2

        # 如果输入的sql格式不对
        if result1 == '':
            data['result'] = 'sql无法识别，请检查sql，或者联系管理员@李英俊小朋友'
        else:
            data['result'] = '计算完成'

    elif request.method == 'GET':
        ...
    else:
        data['result'] = '请联系管理员...'

    return render(request, 'func1_mysql2hive/func1.html', context=data)

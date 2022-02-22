import traceback

from django.shortcuts import render

from funcs.func1.extract_build_hana import analyse_sql
from supports.topc_title_search import search_title


def func2(request):
    """处理获得的sql"""

    data = {
        'title': search_title(request),
        'result1': '',
        'result2': '',
        'result': '',
    }

    if request.method == 'POST':
        sql = request.POST.get('sql')
        view = request.POST.get('view')
        hive_db = request.POST.get('hive_db')
        view_name = request.POST.get('view_name')
        view_desc = request.POST.get('view_desc')

        data['sql'] = sql
        data['view'] = view
        data['hive_db'] = hive_db
        data['view_name'] = view_name
        data['view_desc'] = view_desc

        if sql is None or sql == '':
            data['result'] = '你啥也没输入，想干啥？'
            return render(request, 'func2_hana2hive/func2.html', context=data)
        try:
            result1, result2 = analyse_sql(sql, view, hive_db, view_name, view_desc)
        except Exception as e:
            traceback.print_exc()
            result1, result2 = '', ''

        # 如果输入的sql格式不对
        if result1 == '':
            data['result'] = 'sql无法识别，请检查sql，或者联系管理员@李英俊小朋友'
        else:
            data['result1'] = result1
            data['result2'] = result2
            data['result'] = '计算完成'

    elif request.method == 'GET':
        ...
    else:
        data['result'] = "请联系管理员..."

    return render(request, 'func2_hana2hive/func2.html', context=data)

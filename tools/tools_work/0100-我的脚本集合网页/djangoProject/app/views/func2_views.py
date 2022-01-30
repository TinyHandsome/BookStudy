import traceback

from django.http import HttpResponse
from django.shortcuts import render

from funcs.func1.extract_build_hana import analyse_sql


def func2(request):
    """处理获得的sql"""
    if request.method == 'POST':
        sql = request.POST.get('sql')
        view = request.POST.get('view')
        hive_db = request.POST.get('hive_db')
        view_name = request.POST.get('view_name')
        view_desc = request.POST.get('view_desc')

        data = {
            'sql': sql,
            'result1': '',
            'result2': '',
            'view': view,
            'result': '',
            'hive_db': hive_db,
            'view_name': view_name,
            'view_desc': view_desc,
        }
        if sql is None or sql == '':
            data['result'] = '你啥也没输入，想干啥？'
            return render(request, 'func2/func2.html', context=data)
        try:
            result1, result2 = analyse_sql(sql, view, hive_db, view_name, view_desc)
        except Exception as e:
            traceback.print_exc()
            result1, result2 = -1, -1

        # 如果输入的sql格式不对
        if result1 == -1:
            data['result'] = 'sql无法识别，请检查sql，或者联系管理员@李英俊小朋友'
        else:
            data['result1'] = result1
            data['result2'] = result2
            data['result'] = '计算完成'

        return render(request, 'func2/func2.html', context=data)
    elif request.method == 'GET':
        return render(request, 'func2/func2.html')
    else:
        return HttpResponse("请联系管理员...")

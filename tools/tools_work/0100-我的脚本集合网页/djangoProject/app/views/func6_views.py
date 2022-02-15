import traceback

from django.http import HttpResponse
from django.shortcuts import render

from funcs.func1.extract_build_oracle import analyse_sql


def func6(request):
    """处理获得的sql"""
    if request.method == 'POST':
        sql = request.POST.get('sql')

        data = {
            'sql': sql,
            'result1': '',
            'result2': '',
            'result': '',
        }
        if sql is None or sql == '':
            data['result'] = '你啥也没输入，想干啥？'
            return render(request, 'func6_oracle2hive/func6.html', context=data)
        try:
            result1, result2 = analyse_sql(sql)
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

        return render(request, 'func6_oracle2hive/func6.html', context=data)
    elif request.method == 'GET':
        return render(request, 'func6_oracle2hive/func6.html')
    else:
        return HttpResponse("请联系管理员...")

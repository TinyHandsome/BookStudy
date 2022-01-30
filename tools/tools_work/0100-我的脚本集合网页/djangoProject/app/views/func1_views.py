from django.http import HttpResponse
from django.shortcuts import render
from funcs.func1.extract_built_sql import extract_built_sql


def func1(request):
    """处理获得的sql"""
    if request.method == 'POST':
        sql = request.POST.get('sql')
        if sql is None or sql == '':
            data = {
                'sql': sql,
                'result1': '',
                'result2': '',
                'result': '你啥也没输入，想干啥？'
            }
            return render(request, 'func1/func1.html', context=data)

        result1, result2 = extract_built_sql(sql)
        # 如果输入的sql格式不对
        if result1 == -1:
            data = {
                'sql': sql,
                'result1': '',
                'result2': '',
                'result': 'sql无法识别，请检查sql，或者联系管理员@李英俊小朋友'
            }
        else:
            data = {
                'sql': sql,
                'result1': result1,
                'result2': result2,
                'result': '计算完成'
            }

        return render(request, 'func1/func1.html', context=data)
    elif request.method == 'GET':
        return render(request, 'func1/func1.html')
    else:
        return HttpResponse("请联系管理员...")

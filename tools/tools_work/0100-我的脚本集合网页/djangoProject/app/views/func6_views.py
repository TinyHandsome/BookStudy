import traceback

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from funcs.func1.extract_build_oracle import analyse_sql
from funcs.func3.leaphd_deal import generate_new_precedure_defjson, save_hd_taskschedule


def func6(request):
    """处理获得的sql"""
    if request.method == 'POST':
        sql = request.POST.get('sql')
        result1 = request.POST.get('result1')
        result2 = request.POST.get('result2')
        my_cookie = request.POST.get('my_cookie').strip()

        data = {
            'sql': sql,
            'result1': result1,
            'result2': result2,
            'my_cookie': my_cookie,
            'result': '',
            'schema_table_name': '',
            'schedule_name': '',
        }
        if sql is None or sql == '':
            data['result'] = '你啥也没输入，想干啥？'
            return render(request, 'func6_oracle2hive/func6.html', context=data)
        try:
            result1, result2, schema_table_name = analyse_sql(sql)
        except Exception as e:
            traceback.print_exc()
            result1 = 'error'

        # 如果输入的sql格式不对
        if result1 == 'error':
            data['result'] = 'sql无法识别，请检查sql，或者联系管理员@李英俊小朋友'
        else:
            data['result1'] = result1
            data['result2'] = result2
            data['schema_table_name'] = schema_table_name
            data['schedule_name'] = schema_table_name.replace('.', '_').upper()
            data['result'] = '计算完成'

        return render(request, 'func6_oracle2hive/func6.html', context=data)
    elif request.method == 'GET':
        return render(request, 'func6_oracle2hive/func6.html')
    else:
        return HttpResponse("请联系管理员...")


@csrf_exempt
def func6_generate_new_hive_schedule(request):
    """生成新的hive流程"""
    my_cookie = request.POST.get("my_cookie").strip()
    result1 = request.POST.get("result1")
    result2 = request.POST.get("result2")
    schema_table_name = request.POST.get("schema_table_name")

    try:
        new_defjson = generate_new_precedure_defjson(my_cookie, schema_table_name, result1, result2)
        save_hd_taskschedule(my_cookie, new_defjson, None)
    except:
        new_defjson = ''
        traceback.print_exc()

    return HttpResponse(new_defjson)
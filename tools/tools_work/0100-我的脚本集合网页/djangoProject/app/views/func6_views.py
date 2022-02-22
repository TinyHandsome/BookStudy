import traceback

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from funcs.func1.extract_build_oracle import analyse_sql
from funcs.func3.leaphd_deal import generate_new_precedure_defjson, save_hd_taskschedule
from supports.str_funcs import is_None_or_nullstr
from supports.topc_title_search import search_title


def func6(request):
    """处理获得的sql"""

    data = {
        'title': search_title(request),
        'result': '',
        'schema_table_name': '',
        'schedule_name': '',
    }

    if request.method == 'POST':
        sql = request.POST.get('sql')
        result1 = request.POST.get('result1')
        result2 = request.POST.get('result2')
        my_cookie = request.POST.get('my_cookie').strip()

        data['sql'] = sql
        data['result1'] = result1
        data['result2'] = result2
        data['my_cookie'] = my_cookie

        if is_None_or_nullstr(sql):
            data['result'] = '你啥也没输入，想干啥？'
            return render(request, 'func6_oracle2hive/func6.html', context=data)
        try:
            result1, result2, schema_table_name = analyse_sql(sql)
            data['result1'] = result1
            data['result2'] = result2
            data['schema_table_name'] = schema_table_name
            data['schedule_name'] = schema_table_name.replace('.', '_').upper()
            data['result'] = '计算完成'
        except Exception as e:
            traceback.print_exc()
            data['result'] = 'sql无法识别，请检查sql，或者联系管理员@李英俊小朋友'

    elif request.method == 'GET':
        ...
    else:
        data['result'] = "请联系管理员..."
    return render(request, 'func6_oracle2hive/func6.html', context=data)


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
        new_defjson = '-1'
        traceback.print_exc()

    return HttpResponse(new_defjson)

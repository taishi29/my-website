from django.shortcuts import render
from django.http import HttpResponse
from .utils import web_analysis, get_date, generate_class_name, get_trash_kinds_name, line_notify


def trash_notify(request):
    '''
    ～メイン処理の簡単な流れ～
    1. HTMLデータを解析
    2. 取得したいごみ収集日を設定
    3. 2を基に、HTMLのclass属性を設定
    4. 3のHTMLのclass属性で取得したいごみ収集日の情報をスクレイピングし、そこからごみ収集内容を取得
    5. LINEで通知するメッセージを作成し、実際に送信する
    '''
    # 1. HTMLデータを解析
    html_requests = web_analysis()
    if not html_requests.success:
        params = {
            'error_msg': html_requests.error_msg,
        }
        return render(request, 'trash_notifier/trash_notifier.html', params)
    
    # 2. 日付の取得
    date_result = get_date()
    if not date_result.success:
        params = {
            'error_msg': date_result.error_msg,
        }
        return render(request, 'trash_notifier/trash_notifier.html', params)
    
    # 3. HTMLクラス属性の設定
    td_class_result = generate_class_name(date_result.date)
    if not td_class_result.success:
        params = {
            'error_msg': td_class_result.error_msg,
        }
        return render(request, 'trash_notifier/trash_notifier.html', params)

     # 4. ごみ収集内容の取得
    trash_kinds_result = get_trash_kinds_name(html_requests.soup, td_class_result.td_class)
    if not trash_kinds_result.success:
        params = {
            'error_msg': trash_kinds_result.error_msg,
        }
        return render(request, 'trash_notifier/trash_notifier.html', params)
    
    # 5. LINEで通知するメッセージの作成と送信
    msg = "\n本日は、\n"
    for trash_kind in trash_kinds_result.trash_kinds:
        msg += f"「{trash_kind}」" + "\n"
    msg += "の日です！"
    
    # LINEに通知を送信
    line_notify(msg)
    
    # 成功時のメッセージ表示
    params = {
        'msg': msg,
    }
    return render(request, 'trash_notifier/trash_notifier.html', params)
    
    

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from .models import Company, CompanyImage
import random
import math

# 企業をランダムに表示するビュー（既に表示した企業を除外）
def show_company(request, index):
    # セッションから既に表示された企業のIDリストを取得、なければ空リスト
    shown_companies = request.session.get('shown_companies', [])

    # 既に表示された企業を除外してランダムな順序で取得
    companies = Company.objects.exclude(id__in=shown_companies).order_by('?')

    if companies.exists():
        company = companies.first()

        # 現在の企業IDをセッションに保存
        shown_companies.append(company.id)
        request.session['shown_companies'] = shown_companies
        request.session.modified = True  # セッションの変更を明示

        # 企業に関連する画像を取得
        images = CompanyImage.objects.filter(company=company)

        return render(request, 'match/company.html', {'company': company, 'images': images, 'index': index})
    else:
        # もう表示する企業がない場合、結果ページにリダイレクト
        return redirect('show_result')

# Good/Bad評価を処理するビュー
def evaluate_company(request):
    if request.method == 'POST':
        company_id = request.POST.get('company_id')
        choice = request.POST.get('choice')  # 'good' または 'bad'
        index = int(request.POST.get('index', 0))

        # Goodを選択した場合、セッションに保存
        if choice == 'good':
            if 'good_companies' not in request.session:
                request.session['good_companies'] = []
            request.session['good_companies'].append(int(company_id))  # 会社IDを整数で保存
            request.session.modified = True  # セッションが変更されたことを示す

        # 次の企業に進む
        if index < 6:  # 7回目まで
            return redirect('show_company', index=index+1)
        else:
            return redirect('show_result')

# 結果を表示するビュー
def show_result(request):
    good_company_ids = request.session.get('good_companies', [])
    good_companies = Company.objects.filter(id__in=good_company_ids)

    # パラメータの平均を計算する
    avg_params = {
        'avg_work_life_balance': good_companies.aggregate(Avg('work_life_balance_rating'))['work_life_balance_rating__avg'] or 0,
        'avg_compensation': good_companies.aggregate(Avg('compensation_rating'))['compensation_rating__avg'] or 0,
        'avg_career_advancement': good_companies.aggregate(Avg('career_advancement_rating'))['career_advancement_rating__avg'] or 0,
        'avg_management_relationship': good_companies.aggregate(Avg('management_relationship_rating'))['management_relationship_rating__avg'] or 0,
        'avg_work_environment': good_companies.aggregate(Avg('work_environment_rating'))['work_environment_rating__avg'] or 0,
    }

    # 全企業を取得し、ユークリッド距離で最適な企業を計算
    companies = Company.objects.all()
    best_match = None
    best_distance = float('inf')

    for company in companies:
        # ユークリッド距離の計算
        distance = math.sqrt(
            (company.work_life_balance_rating - avg_params['avg_work_life_balance'])**2 +
            (company.compensation_rating - avg_params['avg_compensation'])**2 +
            (company.career_advancement_rating - avg_params['avg_career_advancement'])**2 +
            (company.management_relationship_rating - avg_params['avg_management_relationship'])**2 +
            (company.work_environment_rating - avg_params['avg_work_environment'])**2
        )
        if distance < best_distance:
            best_distance = distance
            best_match = company

    # 最適な企業に関連する画像を取得
    best_match_images = CompanyImage.objects.filter(company=best_match)

    return render(request, 'match/result.html', {
        'best_match': best_match,
        'images': best_match_images,
        'distance': best_distance,
        'avg_params': avg_params
    })
'''
このビュー関数 show_result は、ユーザーが「Good」と評価した企業を基に、ユークリッド距離を使って最適な企業を見つけ、結果を表示するための処理を行っている。以下がその簡単な説明である。

1. ユーザーの評価データ取得: セッションからユーザーが「Good」と評価した企業のIDを取得し、その企業情報をデータベースから取得する。

2. 平均値の計算: 「Good」と評価された企業群について、各評価項目（ワークライフバランス、待遇、昇進、上司との関係、職場環境）の平均値を計算する。

3. 全企業との距離計算: すべての企業を対象に、計算された平均値とのユークリッド距離を計算し、最も距離が小さい（すなわち平均に最も近い）企業を見つける。

4. 最適な企業とその画像を取得: 最も距離が近い企業（最適な企業）に関連する画像を取得し、テンプレートに渡す。

5. テンプレートへのデータ渡し: 最適な企業、関連画像、距離、平均値をテンプレートに渡し、結果ページを表示する。
'''
# 新しいマッチングを開始するためのビュー
def reset_match(request):
    request.session.flush()  # セッションをリセットして新しいマッチングを開始
    return redirect('show_company', index=0)

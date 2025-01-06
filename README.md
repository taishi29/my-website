# ホームページの作成
このリポジトリは、私がDjangoで作成したホームページ兼ポートフォリオの作成を記録した、リポジトリです。  
私の自己紹介や制作物、お問い合わせフォーム等が記載されています。もし、お暇ならのぞきに来てください！  
作成されたホームページのリンクは、以下のリンクから飛ぶことができます！  
まだまだ未完成です(´;ω;｀)
https://taishi-sushi.com  

## デプロイ先について
本プロジェクトのデプロイは、AWS EC2インスタンスを利用して行いました。  
WebサーバーにはNginx、アプリケーションサーバーにはuWSGIを採用しています。  
また、セキュリティ対策としてAWS Certificate Manager (ACM) を活用し、SSL/TLS証明書を取得および設定することで、HTTPS通信を実現しました。
(QiitaにAWSのデプロイ方法を載せる予定です！今作成してるので、投稿にはだいぶ時間かかります！。。私が躓いた点がわかるように解説していきます！私の勝手な解釈で解説しているので参考程度にお願いします！)


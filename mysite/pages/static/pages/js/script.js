/* scroll_effect */
// getBoundingClientRect().top：要素の上端がビューポートの上端からどれくらいの距離にあるか。
// window.innerHeight：ビューポートの高さを取得。
$(document).ready(function () {
    // 要素の取得
    var scrollAnimationElm = document.querySelectorAll('.scroll_up, .scroll_left, .scroll_right, .animate');

    // アニメーションを実行する関数
    var scrollAnimationFunc = function () {
        for (var i = 0; i < scrollAnimationElm.length; i++) {
            var triggerMargin = 100;
            if (window.innerHeight > scrollAnimationElm[i].getBoundingClientRect().top + triggerMargin) {
                scrollAnimationElm[i].classList.add('on');
            }
        }
    };

    // ページが読み込まれた時点でアニメーションを実行
    scrollAnimationFunc();

    // スクロール時にもアニメーションを実行
    $(window).on('scroll', scrollAnimationFunc);
});


$(document).ready(function () {
    // 要素の取得
    var scrollAnimationElm = document.querySelectorAll('.extinction, .page-title');
    var englishMessageElm = $('.welcome');

    var scrollAnimationFunc = function () {
        for (var i = 0; i < scrollAnimationElm.length; i++) {
            var triggerMargin = 625;

            // 要素がビューポート内に入ったときの処理
            if (window.innerHeight > scrollAnimationElm[i].getBoundingClientRect().top + triggerMargin) {
                scrollAnimationElm[i].classList.add('on');

                // 英語のメッセージを表示
                englishMessageElm.removeClass('hidden').addClass('visible');
            } else {
                // 要素がビューポート外に出たときの処理
                scrollAnimationElm[i].classList.remove('on');

                // 英語のメッセージを非表示
                englishMessageElm.removeClass('visible').addClass('hidden');
            }
        }
    };

    // ページが読み込まれた時点でアニメーションを実行
    scrollAnimationFunc();

    // スクロール時にもアニメーションを実行
    $(window).on('scroll', scrollAnimationFunc);
});

